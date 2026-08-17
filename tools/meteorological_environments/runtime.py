from __future__ import annotations

import importlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time
from typing import Any

import numpy as np

from .catalog import EnvironmentSpec, get_environment


class NotApplicableError(ValueError):
    pass


def _find_executable(name: str) -> str | None:
    direct = shutil.which(name)
    if direct:
        return str(Path(direct).resolve())
    if name == "gfortran":
        root = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/WinGet/Packages"
        matches = sorted(root.glob("BrechtSanders.WinLibs*/mingw64/bin/gfortran.exe")) if root.exists() else []
        if matches:
            return str(matches[-1].resolve())
    return None


def _probe_items(spec: EnvironmentSpec) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if spec.probe_kind.startswith("python_modules"):
        for name in spec.probes:
            available = importlib.util.find_spec(name) is not None
            version = None
            if available:
                module = importlib.import_module(name)
                version = getattr(module, "__version__", None)
            rows.append({"name": name, "available": available, "version": version})
    else:
        for name in spec.probes:
            path = _find_executable(name)
            rows.append({"name": name, "available": path is not None, "path": path})
    return rows


def probe_environment(condition_id: str) -> dict[str, Any]:
    spec = get_environment(condition_id)
    rows = _probe_items(spec)
    if spec.probe_kind.endswith("_any"):
        available = any(row["available"] for row in rows)
    else:
        available = all(row["available"] for row in rows)
    return {
        "condition_id": condition_id,
        "status": "available" if available else "unavailable",
        "emulated": False,
        "runtime": spec.runtime,
        "probe": rows,
    }


def resolve_evidence_paths(package_dir: Path, relative_files: list[str]) -> list[Path]:
    root = package_dir.resolve()
    resolved: list[Path] = []
    for value in relative_files:
        candidate = Path(value)
        if candidate.is_absolute():
            raise ValueError("evidence paths must be package-relative")
        target = (root / candidate).resolve()
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"evidence path escapes package: {value}") from exc
        if not target.is_file():
            raise ValueError(f"evidence file does not exist: {value}")
        resolved.append(target)
    return resolved


def _unavailable(spec: EnvironmentSpec, probe: dict[str, Any], evidence: list[str]) -> dict[str, Any]:
    return {
        "ok": False,
        "status": "unavailable",
        "output": None,
        "warnings": [f"{spec.display_name} is not installed in this runtime"],
        "evidence_files": evidence,
        "provenance": {"condition_id": spec.condition_id, "emulated": False, "probe": probe["probe"]},
    }


def _summary(values: Any, unit: str) -> dict[str, Any]:
    array = np.asarray(values, dtype=float)
    if array.ndim != 1 or array.size == 0 or not np.all(np.isfinite(array)):
        raise ValueError("values must be a non-empty finite one-dimensional array")
    return {
        "count": int(array.size),
        "total": float(array.sum()),
        "mean": float(array.mean()),
        "maximum": float(array.max()),
        "minimum": float(array.min()),
        "unit": unit,
    }


def _numeric_result(value: Any) -> Any:
    array = np.asarray(getattr(value, "values", value), dtype=float)
    if array.ndim == 0:
        return float(array)
    return array.tolist()


def _scalar_result(value: Any, name: str) -> float:
    array = np.asarray(getattr(value, "values", value), dtype=float)
    if array.size != 1:
        raise ValueError(f"{name} produced {array.size} values; expected one aggregated value")
    return float(array.reshape(-1)[0])


def _compile_fortran(scratch_dir: Path) -> tuple[str, str]:
    compiler = _find_executable("gfortran")
    if not compiler:
        raise RuntimeError("gfortran is unavailable")
    source = Path(__file__).resolve().parent / "fortran" / "diagnostics.f90"
    digest = str(source.stat().st_mtime_ns)
    cache = scratch_dir / "fortran_cache"
    cache.mkdir(parents=True, exist_ok=True)
    executable = cache / f"diagnostics_{digest}.exe"
    if not executable.is_file():
        completed = subprocess.run(
            [compiler, "-O2", "-std=f2008", str(source), "-o", str(executable)],
            capture_output=True,
            text=True,
            timeout=120,
            shell=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(f"Fortran compilation failed: {completed.stderr.strip()}")
    return compiler, str(executable)


def _execute_fortran(operation: str, args: dict[str, Any], scratch_dir: Path) -> dict[str, Any]:
    compiler, executable = _compile_fortran(scratch_dir)
    if operation == "precipitation_summary":
        values = np.asarray(args.get("values"), dtype=float)
        if values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values)):
            raise ValueError("values must be a non-empty finite one-dimensional array")
        stdin = f"{operation}\n{values.size}\n" + " ".join(f"{value:.17g}" for value in values) + "\n"
        keys = ("total", "maximum", "minimum", "mean")
    elif operation == "kinematics":
        names = ("du_dx_s1", "dv_dy_s1", "dv_dx_s1", "du_dy_s1")
        stdin = operation + "\n" + " ".join(str(float(args[name])) for name in names) + "\n"
        keys = ("divergence_s1", "relative_vorticity_s1", "stretching_deformation_s1", "shearing_deformation_s1", "total_deformation_s1")
    elif operation == "moisture_transport":
        arrays = [np.asarray(args[name], dtype=float) for name in ("pressure_hpa", "specific_humidity_kg_kg", "u_wind_m_s", "v_wind_m_s")]
        if any(array.size != 2 for array in arrays):
            raise ValueError("Fortran moisture_transport requires exactly two pressure levels")
        values = [arrays[0][0], arrays[0][1], arrays[1][0], arrays[1][1], arrays[2][0], arrays[2][1], arrays[3][0], arrays[3][1]]
        stdin = operation + "\n" + " ".join(f"{value:.17g}" for value in values) + "\n"
        keys = ("precipitable_water_mm", "ivt_u_kg_m_s", "ivt_v_kg_m_s", "ivt_magnitude_kg_m_s")
    else:
        raise NotApplicableError(f"the dedicated Fortran kernel does not implement {operation!r}")
    env = os.environ.copy()
    env["PATH"] = str(Path(compiler).parent) + os.pathsep + env.get("PATH", "")
    completed = subprocess.run(
        [executable], input=stdin, capture_output=True, text=True, timeout=30, shell=False, env=env
    )
    if completed.returncode != 0:
        raise RuntimeError(f"Fortran execution failed: {completed.stderr.strip()}")
    values = [float(token) for token in completed.stdout.split()]
    if len(values) != len(keys):
        raise RuntimeError(f"unexpected Fortran output: {completed.stdout!r}")
    output = dict(zip(keys, values))
    output.update({"compiler": compiler, "executable": executable, "unit": args.get("unit")})
    return output


def _execute_python(
    spec: EnvironmentSpec,
    operation: str,
    args: dict[str, Any],
    evidence_paths: list[Path],
) -> dict[str, Any]:
    if spec.condition_id == "env_metpy" and operation == "precipitation_summary":
        from metpy.units import units

        unit = str(args.get("unit") or "mm")
        quantity = np.asarray(args["values"], dtype=float) * units(unit)
        result = _summary(quantity.magnitude, str(quantity.units))
        result["library_function"] = "metpy.units.units"
        return result
    if spec.condition_id == "env_metpy" and operation == "thermodynamic_profile":
        import metpy.calc as mpcalc
        from metpy.units import units

        pressure = np.asarray(args["pressure_hpa"], dtype=float) * units.hPa
        temperature = np.asarray(args["temperature_c"], dtype=float) * units.degC
        dewpoint = np.asarray(args["dewpoint_c"], dtype=float) * units.degC
        if not (pressure.size == temperature.size == dewpoint.size) or pressure.size < 3:
            raise ValueError("pressure, temperature, and dewpoint profiles must have the same length >= 3")
        lcl_pressure, lcl_temperature = mpcalc.lcl(pressure[0], temperature[0], dewpoint[0])
        parcel = mpcalc.parcel_profile(pressure, temperature[0], dewpoint[0])
        cape, cin = mpcalc.cape_cin(pressure, temperature, dewpoint, parcel)
        return {
            "cape_j_kg": float(cape.to("joule / kilogram").magnitude),
            "cin_j_kg": float(cin.to("joule / kilogram").magnitude),
            "lcl_pressure_hpa": float(lcl_pressure.to("hPa").magnitude),
            "lcl_temperature_c": float(lcl_temperature.to("degC").magnitude),
            "library_function": "metpy.calc.lcl; parcel_profile; cape_cin",
        }
    if spec.condition_id == "env_metpy" and operation == "kinematics":
        import metpy.calc as mpcalc
        from metpy.units import units

        u = np.asarray(args["u_wind_m_s"], dtype=float) * units("m/s")
        v = np.asarray(args["v_wind_m_s"], dtype=float) * units("m/s")
        if u.ndim != 2 or v.shape != u.shape or min(u.shape) < 3:
            raise ValueError("u and v must be matching two-dimensional grids with at least 3x3 cells")
        dx = float(args["dx_m"]) * units.m
        dy = float(args["dy_m"]) * units.m
        divergence = mpcalc.divergence(u, v, dx=dx, dy=dy)
        vorticity = mpcalc.vorticity(u, v, dx=dx, dy=dy)
        return {
            "divergence_s1": np.asarray(divergence.to("1/s").magnitude).tolist(),
            "vorticity_s1": np.asarray(vorticity.to("1/s").magnitude).tolist(),
            "mean_divergence_s1": float(np.nanmean(divergence.to("1/s").magnitude)),
            "mean_vorticity_s1": float(np.nanmean(vorticity.to("1/s").magnitude)),
            "library_function": "metpy.calc.divergence; vorticity",
        }
    if spec.condition_id == "env_metpy" and operation == "storm_environment":
        import metpy.calc as mpcalc
        from metpy.units import units

        height = np.asarray(args["height_m"], dtype=float) * units.m
        u = np.asarray(args["u_wind_m_s"], dtype=float) * units("m/s")
        v = np.asarray(args["v_wind_m_s"], dtype=float) * units("m/s")
        pressure = np.asarray(args["pressure_hpa"], dtype=float) * units.hPa
        if not (height.size == u.size == v.size == pressure.size) or height.size < 3:
            raise ValueError("height, wind, and pressure profiles must have the same length >= 3")
        shear_u, shear_v = mpcalc.bulk_shear(pressure, u, v, height=height, depth=float(args.get("shear_depth_m", 6000)) * units.m)
        positive, negative, total = mpcalc.storm_relative_helicity(
            height, u, v, depth=float(args.get("srh_depth_m", 3000)) * units.m
        )
        return {
            "bulk_shear_u_m_s": float(shear_u.to("m/s").magnitude),
            "bulk_shear_v_m_s": float(shear_v.to("m/s").magnitude),
            "bulk_shear_magnitude_m_s": float(np.hypot(shear_u, shear_v).to("m/s").magnitude),
            "positive_srh_m2_s2": float(positive.to("m^2/s^2").magnitude),
            "negative_srh_m2_s2": float(negative.to("m^2/s^2").magnitude),
            "total_srh_m2_s2": float(total.to("m^2/s^2").magnitude),
            "library_function": "metpy.calc.bulk_shear; storm_relative_helicity",
        }
    if spec.condition_id == "env_xclim" and operation == "precipitation_extremes":
        import pandas as pd
        import xarray as xr
        import xclim

        values = np.asarray(args["values"], dtype=float)
        time = pd.date_range(str(args.get("start_date") or "2000-01-01"), periods=values.size, freq="D")
        unit = str(args.get("unit") or "mm/day")
        array = xr.DataArray(values, dims=("time",), coords={"time": time}, attrs={"units": unit})
        window = int(args.get("window_days", 1))
        maximum = xclim.indices.max_n_day_precipitation_amount(array, window=window)
        wetdays = xclim.indices.wetdays(array, thresh=str(args.get("wet_threshold") or "1 mm/day"))
        result = _summary(array.values, unit)
        result.update({
            "max_n_day_precipitation": _scalar_result(maximum, "max_n_day_precipitation_amount"),
            "window_days": window,
            "wet_days": _scalar_result(wetdays, "wetdays"),
        })
        result["library_version"] = getattr(xclim, "__version__", None)
        result["library_function"] = "xclim.indices.max_n_day_precipitation_amount; wetdays"
        return result
    if spec.condition_id == "env_xclim" and operation == "temperature_extremes":
        import pandas as pd
        import xarray as xr
        import xclim

        values = np.asarray(args["values"], dtype=float)
        time = pd.date_range(str(args.get("start_date") or "2000-01-01"), periods=values.size, freq="D")
        array = xr.DataArray(values, dims=("time",), coords={"time": time}, attrs={"units": args.get("unit", "degC")})
        hot = xclim.indices.tx_days_above(array, thresh=str(args.get("threshold") or "35 degC"))
        return {
            **_summary(values, str(array.attrs["units"])),
            "days_above_threshold": _scalar_result(hot, "tx_days_above"),
            "threshold": str(args.get("threshold") or "35 degC"),
            "library_version": getattr(xclim, "__version__", None),
            "library_function": "xclim.indices.tx_days_above",
        }
    if spec.condition_id == "env_xclim" and operation == "wet_dry_spells":
        import pandas as pd
        import xarray as xr
        import xclim

        values = np.asarray(args["values"], dtype=float)
        time = pd.date_range(str(args.get("start_date") or "2000-01-01"), periods=values.size, freq="D")
        array = xr.DataArray(values, dims=("time",), coords={"time": time}, attrs={"units": args.get("unit", "mm/day")})
        wet = xclim.indices.maximum_consecutive_wet_days(array, thresh=str(args.get("wet_threshold") or "1 mm/day"))
        dry = xclim.indices.maximum_consecutive_dry_days(array, thresh=str(args.get("wet_threshold") or "1 mm/day"))
        return {
            "maximum_consecutive_wet_days": _scalar_result(wet, "maximum_consecutive_wet_days"),
            "maximum_consecutive_dry_days": _scalar_result(dry, "maximum_consecutive_dry_days"),
            "library_version": getattr(xclim, "__version__", None),
            "library_function": "xclim.indices.maximum_consecutive_wet_days; maximum_consecutive_dry_days",
        }
    if spec.condition_id == "env_xclim" and operation == "climate_index":
        raise NotApplicableError("climate_index requires an explicitly named supported xclim index and its complete inputs")
    if spec.condition_id == "env_climate_indices":
        from climate_indices import compute, eto, indices

        values = np.asarray(args.get("values"), dtype=float)
        if values.ndim != 1 or values.size == 0:
            raise ValueError("climate-indices requires a one-dimensional values series")
        start_year = int(args.get("data_start_year", 2000))
        calibration_start = int(args.get("calibration_start_year", start_year))
        calibration_end = int(args.get("calibration_end_year", start_year + max(0, values.size // 12 - 1)))
        periodicity_name = str(args.get("periodicity") or "monthly")
        periodicity = getattr(compute.Periodicity, periodicity_name)
        if operation == "spi":
            result = indices.spi(
                values,
                scale=int(args.get("scale", 3)),
                distribution=compute.Distribution.gamma,
                data_start_year=start_year,
                calibration_year_initial=calibration_start,
                calibration_year_final=calibration_end,
                periodicity=periodicity,
            )
            return {"spi": _numeric_result(result), "library_function": "climate_indices.indices.spi"}
        if operation == "spei":
            pet = np.asarray(args.get("pet_values"), dtype=float)
            if pet.shape != values.shape:
                raise ValueError("pet_values must match precipitation values")
            result = indices.spei(
                values,
                pet,
                scale=int(args.get("scale", 3)),
                distribution=compute.Distribution.gamma,
                periodicity=periodicity,
                data_start_year=start_year,
                calibration_year_initial=calibration_start,
                calibration_year_final=calibration_end,
            )
            return {"spei": _numeric_result(result), "library_function": "climate_indices.indices.spei"}
        if operation == "pet":
            latitude = float(args["latitude_degrees"])
            result = eto.eto_thornthwaite(values, latitude, start_year)
            return {"pet_mm": _numeric_result(result), "library_function": "climate_indices.eto.eto_thornthwaite"}
        raise NotApplicableError("PDSI requires precipitation, PET, and available-water-capacity series with a valid calibration period")
    if spec.condition_id == "env_pyet":
        import pandas as pd
        import pyet

        methods = {
            "penman_monteith": "pm",
            "penman": "penman",
            "hargreaves": "hargreaves",
        }
        requested = list(methods) if operation == "method_comparison" else [operation]
        raw_inputs = args.get("inputs")
        if not isinstance(raw_inputs, dict):
            raise ValueError("PyET requires an inputs object matching the selected method")
        kwargs: dict[str, Any] = {}
        for name, value in raw_inputs.items():
            if isinstance(value, list):
                kwargs[str(name)] = pd.Series(np.asarray(value, dtype=float))
            else:
                kwargs[str(name)] = value
        outputs: dict[str, Any] = {}
        for method in requested:
            function = getattr(pyet, methods[method])
            outputs[method] = _numeric_result(function(**kwargs))
        return {"pet_mm_day": outputs, "library_functions": [f"pyet.{methods[name]}" for name in requested]}
    if spec.condition_id == "env_thermofeel":
        import thermofeel

        functions = {
            "utci": "calculate_utci",
            "heat_index": "calculate_heat_index_adjusted",
            "wind_chill": "calculate_wind_chill",
        }
        requested = list(functions) if operation == "thermal_suite" else [operation]
        inputs = args.get("inputs")
        if not isinstance(inputs, dict):
            raise ValueError("thermofeel requires an inputs object using the library's physical argument names")
        kwargs = {
            str(name): np.asarray(value, dtype=float) if isinstance(value, list) else float(value)
            for name, value in inputs.items()
        }
        outputs: dict[str, Any] = {}
        for name in requested:
            function = getattr(thermofeel, functions[name])
            outputs[name] = _numeric_result(function(**kwargs))
        return {"thermal_indices_k": outputs, "library_functions": [f"thermofeel.{functions[name]}" for name in requested]}
    if spec.condition_id == "env_pyextremes":
        import pandas as pd
        from pyextremes import EVA

        values = np.asarray(args.get("values"), dtype=float)
        if values.ndim != 1 or values.size < 10:
            raise ValueError("pyextremes requires at least ten observations")
        frequency = str(args.get("frequency") or "D")
        index = pd.date_range(str(args.get("start_date") or "2000-01-01"), periods=values.size, freq=frequency)
        model = EVA(pd.Series(values, index=index, name="value"))
        if operation in {"block_maxima", "return_level", "model_compare"}:
            model.get_extremes(method="BM", extremes_type="high", block_size=str(args.get("block_size") or "365.2425D"))
            model.fit_model(model=str(args.get("model") or "MLE"), distribution=args.get("distribution"))
        else:
            model.get_extremes(
                method="POT",
                extremes_type="high",
                threshold=float(args["threshold"]),
                r=str(args.get("declustering_window") or "24h"),
            )
            model.fit_model(model=str(args.get("model") or "MLE"), distribution=args.get("distribution"))
        output: dict[str, Any] = {
            "extreme_count": int(len(model.extremes)),
            "extremes": _numeric_result(model.extremes),
            "distribution": str(model.distribution),
            "library_function": "pyextremes.EVA.get_extremes; fit_model",
        }
        if operation in {"return_level", "model_compare"}:
            periods = args.get("return_periods", [2, 5, 10])
            return_values = model.get_return_value(return_period=periods, alpha=float(args.get("alpha", 0.95)))
            output["return_values"] = [_numeric_result(value) for value in return_values]
            output["return_periods"] = periods
        return output
    if spec.condition_id == "env_xskillscore":
        import xarray as xr
        import xskillscore as xs

        observations = xr.DataArray(np.asarray(args["observations"], dtype=float), dims=("time",))
        forecasts_raw = np.asarray(args["forecasts"], dtype=float)
        if operation == "crps":
            if forecasts_raw.ndim != 2 or forecasts_raw.shape[0] != observations.size:
                raise ValueError("CRPS forecasts must have shape [time, member]")
            forecasts = xr.DataArray(forecasts_raw, dims=("time", "member"))
            result = xs.crps_ensemble(observations, forecasts, member_dim="member", dim="time")
            function = "xskillscore.crps_ensemble"
        else:
            if forecasts_raw.shape != observations.shape:
                raise ValueError("forecast and observation series must have matching shapes")
            forecasts = xr.DataArray(forecasts_raw, dims=("time",))
            if operation == "rmse":
                result = xs.rmse(observations, forecasts, dim="time")
                function = "xskillscore.rmse"
            elif operation == "correlation":
                result = xs.pearson_r(observations, forecasts, dim="time")
                function = "xskillscore.pearson_r"
            else:
                result = xs.brier_score(observations.astype(bool), forecasts, dim="time")
                function = "xskillscore.brier_score"
        return {"score": _numeric_result(result), "library_function": function}
    if spec.condition_id == "env_satpy" and operation == "inspect_scene":
        from satpy import Scene

        if not evidence_paths:
            raise ValueError("Satpy inspect_scene requires native source_files")
        reader = args.get("reader")
        scene = Scene(filenames=[str(path) for path in evidence_paths], reader=reader)
        return {
            "reader": reader,
            "scene_class": Scene.__name__,
            "available_dataset_names": sorted(str(name) for name in scene.available_dataset_names())[:300],
            "all_dataset_names": sorted(str(name) for name in scene.all_dataset_names())[:300],
        }
    if spec.condition_id == "env_satpy":
        raise NotApplicableError(f"Satpy operation {operation!r} requires reader-specific dataset and area parameters")
    if spec.condition_id == "env_radar" and operation == "inspect_volume":
        available = [name for name in ("pyart", "wradlib", "xradar") if importlib.util.find_spec(name)]
        if not evidence_paths:
            raise ValueError("radar inspect_volume requires a native radar source file")
        if "pyart" in available:
            import pyart

            radar = pyart.io.read(str(evidence_paths[0]))
            return {
                "library": "pyart",
                "available_radar_libraries": available,
                "fields": sorted(radar.fields),
                "sweeps": int(radar.nsweeps),
                "rays": int(radar.nrays),
                "gates": int(radar.ngates),
            }
        if "wradlib" in available:
            import wradlib as wrl

            dataset = wrl.io.open_radar_dataset(str(evidence_paths[0]))
            return {"library": "wradlib", "available_radar_libraries": available, "dimensions": dict(dataset.sizes), "variables": sorted(dataset.data_vars)}
        raise NotApplicableError("installed radar environment has no supported reader for inspect_volume")
    if spec.condition_id == "env_radar":
        raise NotApplicableError(f"radar operation {operation!r} requires format-specific processing parameters")
    raise ValueError(f"unsupported operation {operation!r} for {spec.condition_id}")


def _version_command(spec: EnvironmentSpec, executable: str) -> list[str]:
    name = Path(executable).name.lower()
    if spec.condition_id == "env_ncl":
        return [executable, "-V"]
    if name in {"wrf.exe", "wrf"}:
        return [executable]
    return [executable, "--version"]


def _stage_netcdf(args: dict[str, Any], evidence_paths: list[Path], scratch_dir: Path) -> tuple[Path, str]:
    selected = next((path for path in evidence_paths if path.suffix.lower() in {".nc", ".nc4", ".cdf"}), None)
    variable = str(args.get("variable") or "value")
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", variable):
        raise ValueError("variable must be a simple NetCDF identifier")
    if selected is not None:
        return selected, variable
    if "values" not in args:
        raise NotApplicableError("this operation needs a native NetCDF source or explicit values for deterministic staging")
    import xarray as xr

    values = np.asarray(args["values"], dtype=float)
    if values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values)):
        raise ValueError("values must be a non-empty finite one-dimensional array")
    target = scratch_dir / "staged_input.nc"
    dataset = xr.Dataset(
        {variable: (("time",), values, {"units": str(args.get("unit") or "1")})},
        coords={"time": np.arange(values.size, dtype=np.int32)},
        attrs={"staging_policy": "declared_values_only_no_interpolation"},
    )
    dataset.to_netcdf(target)
    return target, variable


def _read_netcdf_values(path: Path, variable: str) -> dict[str, Any]:
    import xarray as xr

    with xr.open_dataset(path) as dataset:
        if variable not in dataset:
            raise ValueError(f"variable {variable!r} not found in output")
        values = np.asarray(dataset[variable].values, dtype=float)
        return {
            "variable": variable,
            "shape": list(values.shape),
            "values": values.reshape(-1).tolist()[:200],
            "unit": dataset[variable].attrs.get("units"),
        }


def _run_checked(command: list[str], scratch_dir: Path, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(command, cwd=scratch_dir, capture_output=True, text=True, timeout=timeout, shell=False)
    if completed.returncode != 0:
        raise RuntimeError(f"command failed ({completed.returncode}): {(completed.stderr or completed.stdout).strip()}")
    return completed


def _execute_command(
    spec: EnvironmentSpec,
    operation: str,
    args: dict[str, Any],
    evidence_paths: list[Path],
    scratch_dir: Path,
) -> dict[str, Any]:
    probe = probe_environment(spec.condition_id)
    executable = next((row.get("path") for row in probe["probe"] if row.get("available")), None)
    if not executable:
        raise RuntimeError(f"no executable available for {spec.condition_id}")
    if operation == "probe":
        completed = _run_checked(_version_command(spec, executable), scratch_dir, timeout=30)
        return {"executable": executable, "version_output": (completed.stdout or completed.stderr).strip()[:2000]}
    if spec.condition_id == "env_cdo":
        input_path, variable = _stage_netcdf(args, evidence_paths, scratch_dir)
        operator = {
            "time_sum": "timsum", "time_mean": "timmean", "time_max": "timmax",
            "field_mean": "fldmean", "field_max": "fldmax",
        }[operation]
        output_path = scratch_dir / f"cdo_{operator}.nc"
        _run_checked([executable, "-O", operator, str(input_path), str(output_path)], scratch_dir)
        return {"operator": operator, "command": [Path(executable).name, operator], **_read_netcdf_values(output_path, variable)}
    if spec.condition_id == "env_nco":
        input_path, variable = _stage_netcdf(args, evidence_paths, scratch_dir)
        if operation == "inspect":
            completed = _run_checked([_find_executable("ncks") or executable, "-m", "-v", variable, str(input_path)], scratch_dir)
            return {"operator": "ncks", "metadata": completed.stdout[:6000]}
        output_path = scratch_dir / f"nco_{operation}.nc"
        if operation == "record_average":
            command = [_find_executable("ncra") or executable, "-O", "-v", variable, str(input_path), str(output_path)]
        elif operation == "weighted_average":
            dimension = str(args.get("dimension") or "time")
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", dimension):
                raise ValueError("dimension must be a simple NetCDF identifier")
            command = [_find_executable("ncwa") or executable, "-O", "-a", dimension, "-v", variable, str(input_path), str(output_path)]
        else:
            expression = str(args.get("expression") or "")
            if not expression or not re.fullmatch(r"[A-Za-z0-9_+*/().= -]+", expression):
                raise ValueError("derive requires a restricted arithmetic expression")
            command = [_find_executable("ncap2") or executable, "-O", "-s", expression, str(input_path), str(output_path)]
        _run_checked(command, scratch_dir)
        output_variable = str(args.get("output_variable") or variable)
        return {"operator": Path(command[0]).name, **_read_netcdf_values(output_path, output_variable)}
    if spec.condition_id == "env_ncl":
        input_path, variable = _stage_netcdf(args, evidence_paths, scratch_dir)
        if operation != "summary":
            raise NotApplicableError(f"NCL {operation} requires the corresponding gridded atmospheric fields")
        script = scratch_dir / "diagnostic.ncl"
        script.write_text(
            'begin\n f=addfile("' + input_path.as_posix() + '","r")\n x=f->' + variable +
            '\n print("EARTHVERSE_MEAN="+avg(x))\n print("EARTHVERSE_MAX="+max(x))\n print("EARTHVERSE_MIN="+min(x))\nend\n',
            encoding="ascii",
        )
        completed = _run_checked([executable, str(script)], scratch_dir)
        return {"script": script.name, "diagnostic_output": completed.stdout[-6000:]}
    if spec.condition_id == "env_r_climate":
        values = np.asarray(args.get("values"), dtype=float)
        if values.ndim != 1 or values.size < 2:
            raise ValueError("R climate operations require at least two finite values")
        data_path = scratch_dir / "values.csv"
        data_path.write_text("value\n" + "\n".join(str(float(value)) for value in values) + "\n", encoding="ascii")
        script = scratch_dir / "diagnostic.R"
        if operation == "summary":
            body = 'x<-read.csv("values.csv")$value; cat(sprintf("{\\\"mean\\\":%.12g,\\\"sd\\\":%.12g,\\\"max\\\":%.12g}",mean(x),sd(x),max(x)))'
        elif operation == "trend":
            body = 'x<-read.csv("values.csv")$value; m<-lm(x~seq_along(x)); cat(sprintf("{\\\"slope\\\":%.12g,\\\"p_value\\\":%.12g}",coef(m)[2],summary(m)$coefficients[2,4]))'
        elif operation == "gev_fit":
            body = 'library(extRemes); x<-read.csv("values.csv")$value; f<-fevd(x,type="GEV"); p<-f$results$par; cat(sprintf("{\\\"location\\\":%.12g,\\\"scale\\\":%.12g,\\\"shape\\\":%.12g}",p[1],p[2],p[3]))'
        else:
            body = 'library(SPEI); x<-read.csv("values.csv")$value; z<-spi(x,scale=as.integer(Sys.getenv("SPI_SCALE","1"))); cat(sprintf("{\\\"last_spi\\\":%.12g}",tail(z$fitted,1)))'
        script.write_text(body + "\n", encoding="ascii")
        env = os.environ.copy()
        env["SPI_SCALE"] = str(int(args.get("scale", 1)))
        completed = subprocess.run([executable, str(script)], cwd=scratch_dir, capture_output=True, text=True, timeout=120, shell=False, env=env)
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr.strip())
        return {"script": script.name, "result": json.loads(completed.stdout)}
    if spec.condition_id == "env_julia":
        values = np.asarray(args.get("values"), dtype=float)
        if values.ndim != 1 or values.size < 2:
            raise ValueError("Julia operations require at least two finite values")
        literal = ",".join(f"{value:.17g}" for value in values)
        if operation == "summary":
            expression = f'x=[{literal}]; using Statistics; print("{{\\\"mean\\\":"*string(mean(x))*",\\\"std\\\":"*string(std(x))*",\\\"maximum\\\":"*string(maximum(x))*"}}")'
        elif operation == "integrate":
            expression = f'x=[{literal}]; dt={float(args.get("time_step", 1.0))}; print("{{\\\"integral\\\":"*string(sum(x)*dt)*"}}")'
        elif operation == "sensitivity":
            expression = f'x=[{literal}]; using Statistics; print("{{\\\"coefficient_of_variation\\\":"*string(std(x)/abs(mean(x)))*"}}")'
        else:
            raise NotApplicableError("Julia advection requires spatial gradients and wind components")
        completed = _run_checked([executable, "--startup-file=no", "-e", expression], scratch_dir)
        return {"expression_family": operation, "result": json.loads(completed.stdout)}
    if spec.condition_id == "env_hysplit":
        for path in evidence_paths:
            shutil.copy2(path, scratch_dir / path.name)
        completed = _run_checked([executable], scratch_dir, timeout=int(args.get("timeout_seconds", 600)))
        outputs = sorted(path.name for path in scratch_dir.iterdir() if path.is_file())
        return {"executable": executable, "stdout": completed.stdout[-4000:], "output_files": outputs}
    if spec.condition_id == "env_wrf":
        if operation != "idealized_case":
            raise NotApplicableError("WRF output diagnostics require wrf-python; full WRF execution requires idealized_case inputs")
        for path in evidence_paths:
            shutil.copy2(path, scratch_dir / path.name)
        completed = _run_checked([executable], scratch_dir, timeout=int(args.get("timeout_seconds", 1800)))
        return {"executable": executable, "stdout": completed.stdout[-4000:]}
    raise NotApplicableError(f"no command adapter for {spec.condition_id}")


def execute_environment_tool(
    condition_id: str,
    args: dict[str, Any],
    package_dir: Path,
    scratch_dir: Path,
) -> dict[str, Any]:
    spec = get_environment(condition_id)
    evidence = [str(value).replace("\\", "/") for value in args.get("source_files", [])]
    try:
        evidence_paths = resolve_evidence_paths(package_dir, evidence)
    except ValueError as exc:
        return {
            "ok": False,
            "status": "error",
            "output": None,
            "warnings": [str(exc)],
            "evidence_files": [],
            "provenance": {"condition_id": condition_id, "emulated": False},
        }
    probe = probe_environment(condition_id)
    if probe["status"] != "available":
        return _unavailable(spec, probe, evidence)
    operation = str(args.get("operation") or "").strip()
    if operation not in spec.operations and operation != "probe":
        return {
            "ok": False,
            "status": "error",
            "output": None,
            "warnings": [f"unsupported operation {operation!r}; allowed: {', '.join(spec.operations)}"],
            "evidence_files": evidence,
            "provenance": {"condition_id": condition_id, "emulated": False, "probe": probe["probe"]},
        }
    scratch_dir.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    try:
        if spec.runtime == "python":
            output = _execute_python(spec, operation, args, evidence_paths)
        elif spec.runtime == "fortran":
            output = _execute_fortran(operation, args, scratch_dir)
        else:
            output = _execute_command(spec, operation, args, evidence_paths, scratch_dir)
    except NotApplicableError as exc:
        return {
            "ok": False,
            "status": "not_applicable",
            "output": None,
            "warnings": [str(exc)],
            "evidence_files": evidence,
            "provenance": {"condition_id": condition_id, "emulated": False, "probe": probe["probe"]},
        }
    except Exception as exc:
        return {
            "ok": False,
            "status": "error",
            "output": None,
            "warnings": [f"{type(exc).__name__}: {exc}"],
            "evidence_files": evidence,
            "provenance": {"condition_id": condition_id, "emulated": False, "probe": probe["probe"]},
        }
    return {
        "ok": True,
        "status": "ok",
        "output": output,
        "warnings": [],
        "evidence_files": evidence,
        "provenance": {
            "condition_id": condition_id,
            "display_name": spec.display_name,
            "operation": operation,
            "emulated": False,
            "probe": probe["probe"],
            "runtime_seconds": round(time.perf_counter() - started, 6),
        },
    }

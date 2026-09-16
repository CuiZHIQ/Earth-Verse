from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Iterable


@dataclass(frozen=True)
class PackageFeatures:
    stageable: bool = False
    netcdf: bool = False
    grib: bool = False
    wrf: bool = False
    hysplit: bool = False
    satellite_native: bool = False
    radar_native: bool = False


@dataclass(frozen=True)
class EnvironmentSpec:
    condition_id: str
    tier: str
    category: str
    tool_name: str
    display_name: str
    runtime: str
    probes: tuple[str, ...]
    probe_kind: str
    compatibility: str
    purpose: str
    operations: tuple[str, ...]
    implemented_operations: tuple[str, ...] | None = None
    min_calls: int = 2
    target_calls: int = 3
    max_calls: int = 4


_SPECS = (
    EnvironmentSpec(
        "env_metpy", "core", "library", "run_metpy", "MetPy atmospheric diagnostics", "python",
        ("metpy", "xarray", "pint"), "python_modules", "stageable",
        "Thermodynamic, kinematic, storm-environment, and unit-aware precipitation diagnostics.",
        ("precipitation_summary", "thermodynamic_profile", "kinematics", "storm_environment"),
    ),
    EnvironmentSpec(
        "env_xclim", "core", "library", "run_xclim", "xclim hydroclimate diagnostics", "python",
        ("xclim", "xarray"), "python_modules", "stageable",
        "Hydroclimate extremes, duration, drought, heat, fire-weather, and snow indices.",
        ("precipitation_extremes", "temperature_extremes", "wet_dry_spells", "climate_index"),
        ("precipitation_extremes", "temperature_extremes", "wet_dry_spells"),
    ),
    EnvironmentSpec(
        "env_climate_indices", "core", "library", "run_climate_indices", "NOAA/NCEI climate-indices", "python",
        ("climate_indices",), "python_modules", "stageable",
        "Reference SPI, SPEI, PET, and Palmer-family climate diagnostics.",
        ("spi", "spei", "pet", "pdsi"),
        ("spi", "spei", "pet"),
    ),
    EnvironmentSpec(
        "env_pyet", "core", "library", "run_pyet", "PyET evapotranspiration", "python",
        ("pyet", "pandas"), "python_modules", "stageable",
        "Potential evapotranspiration with Penman-Monteith and alternative physical methods.",
        ("penman_monteith", "penman", "hargreaves", "method_comparison"),
    ),
    EnvironmentSpec(
        "env_thermofeel", "core", "library", "run_thermofeel", "ECMWF thermofeel", "python",
        ("thermofeel",), "python_modules", "stageable",
        "Outdoor thermal stress including UTCI, heat index, wind chill, and related indices.",
        ("utci", "heat_index", "wind_chill", "thermal_suite"),
    ),
    EnvironmentSpec(
        "env_pyextremes", "core", "library", "run_pyextremes", "pyextremes EVA", "python",
        ("pyextremes", "pandas"), "python_modules", "stageable",
        "Block-maxima and peaks-over-threshold extreme-value models and return levels.",
        ("block_maxima", "peaks_over_threshold", "return_level", "model_compare"),
    ),
    EnvironmentSpec(
        "env_xskillscore", "core", "library", "run_xskillscore", "xskillscore verification", "python",
        ("xskillscore", "xarray"), "python_modules", "stageable",
        "Deterministic and probabilistic verification across local meteorological products.",
        ("rmse", "correlation", "brier", "crps"),
    ),
    EnvironmentSpec(
        "env_fortran", "core", "environment", "run_fortran_meteorology", "GNU Fortran numerical kernels", "fortran",
        ("gfortran",), "executables", "stageable",
        "Compiled moisture, wind, balance, integration, and parity calculations.",
        ("precipitation_summary", "kinematics", "moisture_transport", "balanced_flow"),
        ("precipitation_summary", "kinematics", "moisture_transport"),
    ),
    EnvironmentSpec(
        "env_cdo", "core", "environment", "run_cdo", "Climate Data Operators", "command",
        ("cdo",), "executables", "stageable",
        "Climate and forecast data aggregation, field statistics, interpolation, and indices.",
        ("time_sum", "time_mean", "time_max", "field_mean", "field_max"),
    ),
    EnvironmentSpec(
        "env_nco", "core", "environment", "run_nco", "NetCDF Operators", "command",
        ("ncks", "ncap2", "ncra", "ncwa"), "executables", "stageable",
        "NetCDF inspection, dimension-aware aggregation, weighted statistics, and field derivation.",
        ("inspect", "record_average", "weighted_average", "derive"),
    ),
    EnvironmentSpec(
        "env_ncl", "core", "environment", "run_ncl", "NCAR Command Language", "command",
        ("ncl",), "executables", "stageable",
        "Atmospheric diagnostics, vertical interpolation, EOF, wavelet, and spectral analysis.",
        ("summary", "vorticity_divergence", "vertical_interpolation", "spectrum"),
        ("summary",),
    ),
    EnvironmentSpec(
        "env_r_climate", "core", "environment", "run_r_climate", "R climate statistics", "command",
        ("Rscript",), "executables", "stageable",
        "SPEI, climate extremes, extreme-value fits, trends, and uncertainty intervals.",
        ("summary", "spei", "gev_fit", "trend"),
    ),
    EnvironmentSpec(
        "env_julia", "core", "environment", "run_julia_meteorology", "Julia numerical meteorology", "command",
        ("julia",), "executables", "stageable",
        "NetCDF analysis, numerical integration, differential equations, and sensitivity calculations.",
        ("summary", "integrate", "advection", "sensitivity"),
        ("summary", "integrate", "sensitivity"),
    ),
    EnvironmentSpec(
        "env_wrf", "specialist", "specialist", "run_wrf", "WRF/WPS", "command",
        ("wrf.exe",), "executables_any", "wrf",
        "WRF native output diagnostics or explicitly configured idealized simulations.",
        ("inspect_output", "diagnose_native_output", "idealized_case"),
    ),
    EnvironmentSpec(
        "env_hysplit", "specialist", "specialist", "run_hysplit", "NOAA HYSPLIT", "command",
        ("hyts_std", "hycs_std"), "executables_any", "hysplit",
        "Trajectory and dispersion calculations using native ARL meteorological inputs.",
        ("trajectory", "dispersion", "inspect_output"),
    ),
    EnvironmentSpec(
        "env_satpy", "specialist", "specialist", "run_satpy", "Satpy", "python",
        ("satpy", "pyresample"), "python_modules", "satellite_native",
        "Native meteorological satellite readers, resampling, corrections, and composites.",
        ("inspect_scene", "load_dataset", "resample", "composite"),
    ),
    EnvironmentSpec(
        "env_radar", "specialist", "specialist", "run_weather_radar", "Py-ART/wradlib/xradar", "python",
        ("pyart", "wradlib", "xradar"), "python_modules_any", "radar_native",
        "Native radar volume reading, quality control, gridding, rainfall, and echo diagnostics.",
        ("inspect_volume", "quality_control", "grid", "rainfall"),
    ),
)


def environment_specs() -> tuple[EnvironmentSpec, ...]:
    return _SPECS


def get_environment(condition_id: str) -> EnvironmentSpec:
    for spec in _SPECS:
        if spec.condition_id == condition_id:
            return spec
    raise KeyError(f"unknown meteorological environment: {condition_id}")


def classify_package(relative_files: Iterable[str]) -> PackageFeatures:
    paths = [PurePosixPath(str(item).replace("\\", "/")) for item in relative_files]
    lowered = [path.as_posix().lower() for path in paths]
    suffixes = {path.suffix.lower() for path in paths}
    stageable = bool(suffixes & {".csv", ".json", ".xml", ".txt", ".nc", ".nc4", ".grb", ".grib", ".grib2"})
    netcdf = bool(suffixes & {".nc", ".nc4", ".cdf"})
    grib = bool(suffixes & {".grb", ".grib", ".grib2"})
    wrf = any("wrfout_" in name or "wrfinput_" in name or "wrfbdy_" in name for name in lowered)
    hysplit = any(
        path.name.lower() in {"tdump", "cdump", "control", "setup.cfg"}
        or path.suffix.lower() == ".arl"
        or "hysplit" in path.as_posix().lower()
        for path in paths
    )
    satellite_extensions = {".nc", ".nc4", ".h5", ".hdf", ".hdf5", ".nat", ".dat", ".bin"}
    satellite_native = any(
        path.suffix.lower() in satellite_extensions
        and any(token in path.as_posix().lower() for token in ("abi-l1b", "ahi_hsd", "seviri", "viirs", "mod021km", "fy4a", "slstr"))
        for path in paths
    )
    radar_native = any(
        token in name
        for name in lowered
        for token in ("nexrad", "odim", "cfradial", "radar_volume", "_v06", "level2")
    )
    return PackageFeatures(stageable, netcdf, grib, wrf, hysplit, satellite_native, radar_native)


def compatible_environments(relative_files: Iterable[str]) -> set[str]:
    features = classify_package(relative_files)
    compatible: set[str] = set()
    for spec in _SPECS:
        if bool(getattr(features, spec.compatibility)):
            compatible.add(spec.condition_id)
    return compatible

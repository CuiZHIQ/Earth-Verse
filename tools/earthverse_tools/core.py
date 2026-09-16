from __future__ import annotations

import csv
import json
import math
import re
import statistics
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PACKAGES_ROOT = ROOT / "event_packages" / "standard_event_packages" / "packages"
REGISTRY_PATH = Path(__file__).resolve().parent / "schemas" / "tool_registry.json"
TOOL_ALIASES = {
    "inspect_true_color_image": "read_image_rgb_summary",
    "compare_before_after_images": "compare_image_rgb_summaries",
    "detect_visible_water_extent": "estimate_image_flood_proxy",
    "detect_visible_burn_scar": "estimate_image_burn_proxy",
    "detect_visible_cloud_or_smoke": "estimate_image_obscuration_proxy",
    "query_google_earth_embedding_patch": "read_alphaearth_embedding_stats",
    "compare_earth_embedding_years": "compare_alphaearth_embedding_stats",
    "summarize_satellite_scene_content": "summarize_image_rgb_statistics",
    "locate_objects_in_image": "read_image_file_metadata",
    "compare_image_scene_to_hazard_signature": "compare_image_proxy_to_hazard_signature",
    "build_visual_change_summary": "build_image_change_summary",
}


def _jsonable(value: Any) -> Any:
    try:
        import numpy as np
        import pandas as pd
    except Exception:
        np = None
        pd = None
    if np is not None and isinstance(value, (np.integer, np.floating)):
        return value.item()
    if np is not None and isinstance(value, np.ndarray):
        return value.tolist()
    if pd is not None and isinstance(value, getattr(pd, "Timestamp")):
        return None if value is pd.NaT else value.isoformat()
    if pd is not None and value is pd.NaT:
        return None
    if pd is not None and hasattr(value, "to_dict"):
        return value.to_dict(orient="records")
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_jsonable(v) for v in value]
    return value


def result(tool: str, ok: bool, data: Any = None, warnings: list[str] | None = None, error: str | None = None, provenance: list[str] | None = None) -> dict[str, Any]:
    out = {
        "tool": tool,
        "ok": bool(ok),
        "data": _jsonable(data if data is not None else {}),
        "warnings": warnings or [],
        "error": error,
        "provenance": provenance or [],
    }
    return out


def ok(tool: str, data: Any = None, warnings: list[str] | None = None, provenance: list[str] | None = None) -> dict[str, Any]:
    return result(tool, True, data=data, warnings=warnings, provenance=provenance)


def fail(tool: str, error: str, warnings: list[str] | None = None, provenance: list[str] | None = None) -> dict[str, Any]:
    return result(tool, False, error=error, warnings=warnings, provenance=provenance)


def load_registry() -> list[dict[str, Any]]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def resolve_packages_root(packages_root: str | Path | None = None) -> Path:
    return Path(packages_root).resolve() if packages_root else DEFAULT_PACKAGES_ROOT


def event_dir(event_id: str, packages_root: str | Path | None = None) -> Path:
    p = resolve_packages_root(packages_root) / event_id
    if not p.exists():
        raise FileNotFoundError(f"event package not found: {p}")
    return p


def safe_path(path: str | Path, base: str | Path | None = None) -> Path:
    p = Path(path)
    if not p.is_absolute():
        p = (Path(base) if base else ROOT) / p
    return p.resolve()


def read_json(path: str | Path) -> Any:
    return json.loads(safe_path(path).read_text(encoding="utf-8"))


def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    with safe_path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def list_files(event_id: str, recursive: bool = True, layer_filter: str | None = None, packages_root: str | Path | None = None) -> list[dict[str, Any]]:
    root = event_dir(event_id, packages_root)
    iterator = root.rglob("*") if recursive else root.glob("*")
    rows = []
    for p in iterator:
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        layer = rel.split("/")[1] if rel.startswith("data/") and "/" in rel[5:] else rel.split("/")[0]
        if layer_filter and layer_filter.lower() not in rel.lower():
            continue
        rows.append({
            "relative_path": rel,
            "bytes": p.stat().st_size,
            "suffix": p.suffix.lower(),
            "layer": layer,
        })
    return sorted(rows, key=lambda x: x["relative_path"])


def load_event_metadata(event_id: str, packages_root: str | Path | None = None) -> dict[str, Any]:
    root = event_dir(event_id, packages_root)
    meta = root / "metadata" / "event.json"
    if not meta.exists():
        return {"package_id": event_id, "warning": "metadata/event.json missing"}
    return json.loads(meta.read_text(encoding="utf-8"))


def read_text(path: str | Path, max_chars: int | None = None) -> dict[str, Any]:
    p = safe_path(path)
    raw = p.read_bytes()
    text = None
    warnings = []
    for enc in ("utf-8", "utf-8-sig", "latin-1", "gb18030"):
        try:
            text = raw.decode(enc)
            break
        except Exception:
            continue
    if text is None:
        text = raw.decode("utf-8", errors="replace")
        warnings.append("decoded with replacement")
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if max_chars:
        text = text[:max_chars]
    return {"path": str(p), "chars": len(text), "text": text, "warnings": warnings}


def read_many_texts(paths: list[str | Path], max_chars: int | None = None) -> list[dict[str, Any]]:
    return [read_text(p, max_chars=max_chars) for p in paths]


TEXT_SUFFIXES = {".txt", ".md", ".html", ".htm", ".xml", ".json", ".csv", ".tsv", ".data", ".error", ".shtml", ".aspx", ".php"}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}
RASTER_SUFFIXES = {".tif", ".tiff"}
VECTOR_SUFFIXES = {".geojson", ".gpkg", ".shp", ".kml"}
ARCHIVE_SUFFIXES = {".zip"}


def _decode_text_bytes(raw: bytes, max_chars: int | None = None) -> dict[str, Any]:
    text = None
    encoding = None
    warnings = []
    for enc in ("utf-8", "utf-8-sig", "latin-1", "gb18030"):
        try:
            text = raw.decode(enc)
            encoding = enc
            break
        except Exception:
            continue
    if text is None:
        text = raw.decode("utf-8", errors="replace")
        encoding = "utf-8-replace"
        warnings.append("decoded with replacement")
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if max_chars:
        text = text[:max_chars]
    return {"encoding": encoding, "chars": len(text), "text": text, "warnings": warnings}


def _looks_textual(raw: bytes, sample_size: int = 4096) -> bool:
    sample = raw[:sample_size]
    if not sample:
        return True
    if b"\x00" in sample:
        return False
    printable = sum(1 for b in sample if b in b"\n\r\t" or 32 <= b <= 126 or b >= 128)
    return printable / max(len(sample), 1) >= 0.85


def _magic_format(raw: bytes) -> str | None:
    if raw.startswith(b"PK\x03\x04"):
        return "zip"
    if raw.startswith((b"II*\x00", b"MM\x00*")):
        return "tiff"
    if raw.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if raw.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if raw.startswith(b"%PDF"):
        return "pdf"
    stripped = raw.lstrip()[:32].lower()
    if stripped.startswith((b"<html", b"<!doctype html")):
        return "html"
    if stripped.startswith((b"{", b"[")):
        return "json"
    return None


def _file_identity(path: str | Path) -> dict[str, Any]:
    p = safe_path(path)
    with p.open("rb") as f:
        head = f.read(512)
    return {
        "path": str(p),
        "name": p.name,
        "suffix": p.suffix.lower(),
        "detected_format": _magic_format(head),
        "size_bytes": int(p.stat().st_size),
        "exists": p.exists(),
    }


def _json_preview(data: Any, max_rows: int = 5) -> dict[str, Any]:
    if isinstance(data, list):
        return {
            "json_type": "list",
            "rows": len(data),
            "sample": data[:max_rows],
        }
    if isinstance(data, dict):
        list_keys = [k for k, v in data.items() if isinstance(v, list)]
        preview: dict[str, Any] = {
            "json_type": "object",
            "top_level_keys": list(data.keys())[:50],
            "list_keys": list_keys[:20],
        }
        for key in ("features", "events", "data", "results", "items"):
            value = data.get(key)
            if isinstance(value, list):
                preview["primary_list_key"] = key
                preview["rows"] = len(value)
                preview["sample"] = value[:max_rows]
                break
        if "sample" not in preview:
            preview["sample"] = {k: data[k] for k in list(data)[:max_rows]}
        return preview
    return {"json_type": type(data).__name__, "value_preview": str(data)[:1000]}


def list_archive_contents_metric(path: str | Path, max_members: int = 200) -> dict[str, Any]:
    import zipfile

    p = safe_path(path)
    if not zipfile.is_zipfile(p):
        raw = p.read_bytes()
        fallback = _decode_text_bytes(raw, max_chars=1000) if _looks_textual(raw) else {"hex_prefix": raw[:64].hex()}
        return {**_file_identity(p), "is_archive": False, "warning": "file extension suggests ZIP but the file is not a valid ZIP archive", **fallback}
    with zipfile.ZipFile(p) as zf:
        infos = [info for info in zf.infolist() if not info.is_dir()]
        members = []
        for info in infos[:max_members]:
            members.append({
                "name": info.filename,
                "suffix": Path(info.filename).suffix.lower(),
                "size_bytes": int(info.file_size),
                "compressed_size_bytes": int(info.compress_size),
            })
        return {
            "archive_path": str(p),
            "member_count": len(infos),
            "listed_count": len(members),
            "total_uncompressed_bytes": int(sum(info.file_size for info in infos)),
            "members": members,
            "truncated": len(infos) > max_members,
        }


def summarize_archive_member_metric(path: str | Path, member: str | None = None, max_chars: int = 4000, max_rows: int = 5) -> dict[str, Any]:
    import io
    import zipfile

    import pandas as pd

    p = safe_path(path)
    if not zipfile.is_zipfile(p):
        raw = p.read_bytes()
        fallback = _decode_text_bytes(raw, max_chars=max_chars) if _looks_textual(raw) else {"hex_prefix": raw[:64].hex()}
        return {**_file_identity(p), "is_archive": False, "warning": "file extension suggests ZIP but the file is not a valid ZIP archive", **fallback}
    with zipfile.ZipFile(p) as zf:
        infos = [info for info in zf.infolist() if not info.is_dir()]
        if not infos:
            return {"archive_path": str(p), "warning": "archive has no file members"}
        info = next((x for x in infos if x.filename == member), None) if member else None
        if info is None:
            if member:
                return {
                    "archive_path": str(p),
                    "requested_member": member,
                    "warning": "member not found",
                    "available_members": [x.filename for x in infos[:50]],
                }
            info = infos[0]
        raw = zf.read(info)
        suffix = Path(info.filename).suffix.lower()
        base = {
            "archive_path": str(p),
            "member": info.filename,
            "suffix": suffix,
            "size_bytes": int(info.file_size),
        }
        if suffix == ".zip":
            try:
                with zipfile.ZipFile(io.BytesIO(raw)) as nested:
                    nested_infos = [x for x in nested.infolist() if not x.is_dir()]
                return {**base, "nested_archive": True, "member_count": len(nested_infos), "members": [{"name": x.filename, "size_bytes": int(x.file_size)} for x in nested_infos[:50]]}
            except Exception as e:
                return {**base, "nested_archive": True, "warning": f"nested archive could not be listed: {e}"}
        if suffix in {".csv", ".tsv"}:
            sep = "\t" if suffix == ".tsv" else ","
            df = pd.read_csv(io.BytesIO(raw), sep=sep)
            return {**base, "kind": "table", "rows": int(len(df)), "columns": list(df.columns), "sample": df.head(max_rows).to_dict(orient="records")}
        if suffix == ".json" or suffix == ".geojson":
            decoded = _decode_text_bytes(raw)
            try:
                return {**base, "kind": "json", **_json_preview(json.loads(decoded["text"]), max_rows=max_rows)}
            except Exception:
                return {**base, "kind": "text", **_decode_text_bytes(raw, max_chars=max_chars), "warning": "JSON parse failed; returned text preview"}
        if suffix in TEXT_SUFFIXES or _looks_textual(raw):
            return {**base, "kind": "text", **_decode_text_bytes(raw, max_chars=max_chars)}
        return {**base, "kind": "binary", "hex_prefix": raw[:64].hex(), "warning": "binary archive member; use a domain reader after identifying the format"}


def inspect_package_file_metric(path: str | Path, max_chars: int = 4000, max_rows: int = 5, max_members: int = 50) -> dict[str, Any]:
    p = safe_path(path)
    ident = _file_identity(p)
    suffix = ident["suffix"]
    detected = ident.get("detected_format")
    if detected == "zip":
        archive_summary = list_archive_contents_metric(p, max_members=max_members)
        kind = "archive" if archive_summary.get("is_archive", True) else "not_valid_archive"
        return {**ident, "kind": kind, **archive_summary}
    if detected == "tiff":
        return {**ident, "kind": "raster", **raster_summary(p)}
    if detected in {"jpeg", "png"}:
        return {**ident, "kind": "image", **rich_image_summary(p)}
    if detected == "pdf":
        suffix = ".pdf"
    if detected == "html":
        return {**ident, "kind": "text", **read_text(p, max_chars=max_chars)}
    if detected == "json":
        try:
            raw = p.read_bytes()
            decoded = _decode_text_bytes(raw)
            return {**ident, "kind": "json", **_json_preview(json.loads(decoded["text"]), max_rows=max_rows)}
        except Exception:
            pass
    if suffix in ARCHIVE_SUFFIXES:
        archive_summary = list_archive_contents_metric(p, max_members=max_members)
        kind = "archive" if archive_summary.get("is_archive", True) else "not_valid_archive"
        return {**ident, "kind": kind, **archive_summary}
    if suffix in {".csv", ".tsv", ".json"}:
        try:
            return {**ident, "kind": "table_or_json", **summarize_table_or_json_metric(p, max_rows=max_rows)}
        except Exception as e:
            raw = p.read_bytes()
            return {**ident, "kind": "text", **_decode_text_bytes(raw, max_chars=max_chars), "warning": f"structured summary failed: {e}"}
    if suffix in TEXT_SUFFIXES:
        return {**ident, "kind": "text", **read_text(p, max_chars=max_chars)}
    if suffix in IMAGE_SUFFIXES:
        return {**ident, "kind": "image", **rich_image_summary(p)}
    if suffix in RASTER_SUFFIXES:
        return {**ident, "kind": "raster", **raster_summary(p)}
    if suffix in VECTOR_SUFFIXES:
        return {**ident, "kind": "vector", **vector_summary(p)}
    if suffix == ".pdf":
        try:
            import pypdf

            reader = pypdf.PdfReader(str(p))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            return {**ident, "kind": "pdf", "pages": len(reader.pages), "text": text[:max_chars]}
        except Exception as e:
            raw = p.read_bytes()
            return {**ident, "kind": "pdf_or_binary", "reader_error": str(e), "hex_prefix": raw[:64].hex(), "warning": "PDF text extraction failed; file may be locked, truncated, or mislabeled"}
    raw = p.read_bytes()
    if _looks_textual(raw):
        return {**ident, "kind": "text", **_decode_text_bytes(raw, max_chars=max_chars)}
    return {**ident, "kind": "binary", "hex_prefix": raw[:64].hex(), "warning": "unknown binary file; inspect package inventory or archive contents for next step"}


def text_snippets(paths: list[str | Path], keywords: list[str], window: int = 160) -> list[dict[str, Any]]:
    snippets = []
    for p in paths:
        item = read_text(p)
        text = item["text"]
        lower = text.lower()
        for kw in keywords:
            k = kw.lower()
            start = 0
            while True:
                idx = lower.find(k, start)
                if idx < 0:
                    break
                snippets.append({
                    "path": item["path"],
                    "keyword": kw,
                    "snippet": text[max(0, idx - window): idx + len(kw) + window],
                })
                start = idx + len(k)
                if len(snippets) >= 100:
                    return snippets
    return snippets


def table_schema(path: str | Path) -> dict[str, Any]:
    import pandas as pd
    p = safe_path(path)
    df = pd.read_csv(p) if p.suffix.lower() in {".csv", ".tsv"} else pd.read_json(p)
    return {
        "path": str(p),
        "rows": int(len(df)),
        "columns": list(df.columns),
        "dtypes": {c: str(df[c].dtype) for c in df.columns},
        "sample": df.head(5).to_dict(orient="records"),
    }


def summarize_table_or_json_metric(path: str | Path, max_rows: int = 5, numeric_summary: bool = True) -> dict[str, Any]:
    df = load_table(path)
    out: dict[str, Any] = {
        "path": str(safe_path(path)),
        "rows": int(len(df)),
        "columns": list(df.columns),
        "sample": df.head(max_rows).to_dict(orient="records"),
    }
    if numeric_summary:
        numeric: dict[str, Any] = {}
        for col in df.columns:
            s = numeric_series(df, col)
            if len(s):
                numeric[col] = {
                    "count": int(len(s)),
                    "min": float(s.min()),
                    "max": float(s.max()),
                    "mean": float(s.mean()),
                    "sum": float(s.sum()),
                }
        out["numeric_summary"] = numeric
    return out


def load_table(path: str | Path):
    import pandas as pd
    p = safe_path(path)
    if p.suffix.lower() == ".tsv":
        return pd.read_csv(p, sep="\t")
    if p.suffix.lower() == ".json":
        try:
            return pd.read_json(p)
        except Exception:
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return pd.json_normalize(data)
            if isinstance(data, dict):
                for key in ("features", "events", "data", "results", "items"):
                    if isinstance(data.get(key), list):
                        return pd.json_normalize(data[key])
                return pd.json_normalize(data)
            raise
    return pd.read_csv(p)


def unit_conversion_or_ratio_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    conversions = {
        ("inch", "mm"): 25.4,
        ("in", "mm"): 25.4,
        ("mm", "inch"): 1 / 25.4,
        ("mm", "in"): 1 / 25.4,
        ("cm", "mm"): 10.0,
        ("mm", "cm"): 0.1,
        ("m", "km"): 0.001,
        ("km", "m"): 1000.0,
        ("m", "ft"): 3.280839895,
        ("ft", "m"): 0.3048,
    }
    if {"value", "from_unit", "to_unit"} <= set(kwargs):
        from_unit = str(kwargs["from_unit"]).lower()
        to_unit = str(kwargs["to_unit"]).lower()
        value = float(kwargs["value"])
        if from_unit in {"f", "fahrenheit"} and to_unit in {"c", "celsius"}:
            converted = (value - 32.0) * 5.0 / 9.0
        elif from_unit in {"c", "celsius"} and to_unit in {"f", "fahrenheit"}:
            converted = value * 9.0 / 5.0 + 32.0
        else:
            factor = conversions.get((from_unit, to_unit))
            if factor is None:
                return {"warning": f"unsupported conversion {from_unit}->{to_unit}", "input_value": value}
            converted = value * factor
        out["converted_value"] = converted
        out["from_unit"] = from_unit
        out["to_unit"] = to_unit
    if "numerator" in kwargs and "denominator" in kwargs:
        denominator = float(kwargs["denominator"])
        out["ratio"] = None if denominator == 0 else float(kwargs["numerator"]) / denominator
        out["numerator"] = float(kwargs["numerator"])
        out["denominator"] = denominator
    return out or {"warning": "provide value/from_unit/to_unit and/or numerator/denominator"}


def numeric_series(df, value_col: str | None = None):
    import pandas as pd
    if value_col and value_col in df.columns:
        return pd.to_numeric(df[value_col], errors="coerce").dropna()
    for c in df.columns:
        s = pd.to_numeric(df[c], errors="coerce").dropna()
        if len(s):
            return s
    return pd.Series(dtype=float)


def time_window_stats(path: str | Path, time_col: str | None = None, value_cols: list[str] | None = None, start: str | None = None, end: str | None = None, stats: list[str] | None = None) -> dict[str, Any]:
    import pandas as pd
    df = load_table(path)
    if time_col and time_col in df.columns:
        t = pd.to_datetime(df[time_col], errors="coerce", utc=True)
        if start:
            df = df[t >= pd.to_datetime(start, utc=True)]
            t = pd.to_datetime(df[time_col], errors="coerce", utc=True)
        if end:
            df = df[t <= pd.to_datetime(end, utc=True)]
    cols = value_cols or list(df.columns)
    out = {"rows": int(len(df)), "columns": {}}
    wanted = stats or ["min", "max", "mean", "sum", "median"]
    for c in cols:
        if c not in df.columns:
            continue
        s = pd.to_numeric(df[c], errors="coerce").dropna()
        if not len(s):
            continue
        vals = {}
        if "min" in wanted: vals["min"] = float(s.min())
        if "max" in wanted: vals["max"] = float(s.max())
        if "mean" in wanted: vals["mean"] = float(s.mean())
        if "sum" in wanted: vals["sum"] = float(s.sum())
        if "median" in wanted: vals["median"] = float(s.median())
        if "p95" in wanted: vals["p95"] = float(s.quantile(0.95))
        if "p99" in wanted: vals["p99"] = float(s.quantile(0.99))
        out["columns"][c] = vals
    return out


def rolling_stat(path: str | Path, value_col: str | None = None, window: int = 3, op: str = "sum") -> dict[str, Any]:
    df = load_table(path)
    s = numeric_series(df, value_col)
    if not len(s):
        return {"count": 0, "warning": "no numeric values"}
    r = s.rolling(int(window), min_periods=int(window))
    vals = r.sum() if op == "sum" else r.mean()
    vals = vals.dropna()
    if not len(vals):
        return {"count": int(len(s)), "warning": "window longer than available series"}
    idx = vals.idxmax()
    return {"count": int(len(s)), "window": int(window), "operation": op, "peak_value": float(vals.loc[idx]), "peak_index": int(idx) if isinstance(idx, int) else str(idx)}


def consecutive_exceedance(path: str | Path, value_col: str | None = None, threshold: float = 0.0, op: str = ">=") -> dict[str, Any]:
    s = numeric_series(load_table(path), value_col)
    if op in (">", "gt"):
        mask = s > threshold
    elif op in ("<", "lt"):
        mask = s < threshold
    elif op in ("<=", "le"):
        mask = s <= threshold
    else:
        mask = s >= threshold
    best = cur = 0
    for v in mask:
        cur = cur + 1 if bool(v) else 0
        best = max(best, cur)
    return {"threshold": threshold, "op": op, "longest_run": int(best), "exceedance_count": int(mask.sum()), "count": int(len(mask))}


def vector_summary(path: str | Path) -> dict[str, Any]:
    import geopandas as gpd
    p = safe_path(path)
    gdf = gpd.read_file(p)
    return {"path": str(p), "features": int(len(gdf)), "crs": str(gdf.crs), "geometry_types": sorted(map(str, gdf.geom_type.dropna().unique())), "bbox": list(map(float, gdf.total_bounds)) if len(gdf) else None, "columns": list(gdf.columns)}


def _read_vector(path: str | Path):
    import geopandas as gpd
    return gpd.read_file(safe_path(path))


def _project_for_metric(gdf):
    if gdf.crs is None:
        return gdf, ["input CRS missing; lengths/areas use raw coordinate units"]
    try:
        if gdf.crs.is_projected:
            return gdf, []
        return gdf.to_crs(6933), ["input CRS was geographic; reprojected to EPSG:6933 for approximate metric area/length"]
    except Exception as e:
        return gdf, [f"metric reprojection failed: {e}; using raw CRS units"]


def polygon_area_metric(path: str | Path, class_filter: dict[str, Any] | None = None) -> dict[str, Any]:
    gdf = _read_vector(path)
    if class_filter:
        for key, value in class_filter.items():
            if key in gdf.columns:
                gdf = gdf[gdf[key] == value]
    gdf, warnings = _project_for_metric(gdf)
    area_km2 = float(gdf.geometry.area.sum() / 1_000_000)
    return {"features": int(len(gdf)), "area_km2": area_km2, "warnings": warnings}


def line_length_in_polygon_metric(line_path: str | Path, polygon_path: str | Path | None = None, class_filter: dict[str, Any] | None = None) -> dict[str, Any]:
    lines = _read_vector(line_path)
    warnings = []
    if class_filter:
        for key, value in class_filter.items():
            if key in lines.columns:
                lines = lines[lines[key] == value]
    if polygon_path:
        poly = _read_vector(polygon_path)
        if lines.crs and poly.crs and lines.crs != poly.crs:
            poly = poly.to_crs(lines.crs)
        try:
            lines = lines.overlay(poly[["geometry"]], how="intersection")
        except Exception:
            union = poly.geometry.union_all() if hasattr(poly.geometry, "union_all") else poly.unary_union
            lines = lines[lines.intersects(union)].copy()
            lines["geometry"] = lines.geometry.intersection(union)
            warnings.append("used manual intersection fallback")
    lines, w = _project_for_metric(lines)
    warnings.extend(w)
    return {"features": int(len(lines)), "length_km": float(lines.geometry.length.sum() / 1000), "warnings": warnings}


def count_points_or_facilities_metric(points_path: str | Path, polygon_path: str | Path | None = None, type_col: str | None = None) -> dict[str, Any]:
    pts = _read_vector(points_path)
    if polygon_path:
        poly = _read_vector(polygon_path)
        if pts.crs and poly.crs and pts.crs != poly.crs:
            poly = poly.to_crs(pts.crs)
        union = poly.geometry.union_all() if hasattr(poly.geometry, "union_all") else poly.unary_union
        pts = pts[pts.intersects(union)]
    out = {"count": int(len(pts)), "columns": list(pts.columns)}
    if type_col and type_col in pts.columns:
        out["by_type"] = pts[type_col].astype(str).value_counts().head(30).to_dict()
    return out


def raster_summary(path: str | Path) -> dict[str, Any]:
    import rasterio
    p = safe_path(path)
    with rasterio.open(p) as src:
        return {
            "path": str(p), "crs": str(src.crs), "width": src.width, "height": src.height,
            "count": src.count, "bounds": list(map(float, src.bounds)), "nodata": src.nodata,
            "dtypes": list(src.dtypes), "res": list(map(float, src.res)),
        }


def raster_stats(path: str | Path, band: int = 1) -> dict[str, Any]:
    import numpy as np
    import rasterio
    p = safe_path(path)
    with rasterio.open(p) as src:
        arr = src.read(band, masked=True).astype(float)
        vals = arr.compressed()
        if vals.size == 0:
            return {"valid_pixels": 0, "warning": "no valid pixels"}
        return {
            "valid_pixels": int(vals.size), "min": float(vals.min()), "max": float(vals.max()),
            "mean": float(vals.mean()), "sum": float(vals.sum()),
            "p95": float(np.percentile(vals, 95)), "p99": float(np.percentile(vals, 99)),
        }


def threshold_area(path: str | Path, threshold: float, op: str = ">", band: int = 1) -> dict[str, Any]:
    import rasterio
    p = safe_path(path)
    with rasterio.open(p) as src:
        arr = src.read(band, masked=True).astype(float)
        if op in (">=", "ge"):
            mask = arr >= threshold
        elif op in ("<", "lt"):
            mask = arr < threshold
        elif op in ("<=", "le"):
            mask = arr <= threshold
        else:
            mask = arr > threshold
        count = int(mask.filled(False).sum())
        pixel_area = abs(src.transform.a * src.transform.e)
        # If CRS is geographic, this remains a pixel-degree proxy; caller gets a warning.
        area = count * pixel_area
        unit = "square_crs_units"
        warnings = [] if src.crs and src.crs.is_projected else ["area is in square degrees/proxy units because CRS is not projected"]
        return {"matching_pixels": count, "area": float(area), "unit": unit, "warnings": warnings}


def raster_difference_metric(pre_path: str | Path, post_path: str | Path, threshold: float | None = None, op: str = "abs_gt", band: int = 1) -> dict[str, Any]:
    import numpy as np
    import rasterio
    pre = safe_path(pre_path)
    post = safe_path(post_path)
    with rasterio.open(pre) as a, rasterio.open(post) as b:
        aa = a.read(band, masked=True).astype(float)
        bb = b.read(band, masked=True).astype(float)
        rows = min(aa.shape[0], bb.shape[0])
        cols = min(aa.shape[1], bb.shape[1])
        diff = bb[:rows, :cols] - aa[:rows, :cols]
        vals = diff.compressed()
        out = {
            "pre_path": str(pre),
            "post_path": str(post),
            "valid_pixels": int(vals.size),
            "mean_change": float(vals.mean()) if vals.size else None,
            "min_change": float(vals.min()) if vals.size else None,
            "max_change": float(vals.max()) if vals.size else None,
            "p95_abs_change": float(np.percentile(np.abs(vals), 95)) if vals.size else None,
        }
        if threshold is not None and vals.size:
            if op == "gt":
                mask = diff > threshold
            elif op == "lt":
                mask = diff < threshold
            else:
                mask = abs(diff) > threshold
            out["threshold"] = threshold
            out["changed_pixels"] = int(mask.filled(False).sum())
        return out


def normalized_difference_metric(path_a: str | Path, path_b: str | Path, name: str, band_a: int = 1, band_b: int = 1) -> dict[str, Any]:
    import numpy as np
    import rasterio
    with rasterio.open(safe_path(path_a)) as a, rasterio.open(safe_path(path_b)) as b:
        aa = a.read(band_a, masked=True).astype(float)
        bb = b.read(band_b, masked=True).astype(float)
        rows = min(aa.shape[0], bb.shape[0])
        cols = min(aa.shape[1], bb.shape[1])
        idx = (aa[:rows, :cols] - bb[:rows, :cols]) / (aa[:rows, :cols] + bb[:rows, :cols] + 1e-12)
        vals = idx.compressed()
        return {"index": name, "valid_pixels": int(vals.size), "mean": float(vals.mean()) if vals.size else None, "min": float(vals.min()) if vals.size else None, "max": float(vals.max()) if vals.size else None, "p95": float(np.percentile(vals, 95)) if vals.size else None}


def image_summary(path: str | Path) -> dict[str, Any]:
    from PIL import Image, ImageStat
    p = safe_path(path)
    with Image.open(p) as img:
        stat = ImageStat.Stat(img.convert("RGB"))
        return {"path": str(p), "mode": img.mode, "width": img.width, "height": img.height, "mean_rgb": [float(x) for x in stat.mean], "extrema": stat.extrema}


def rich_image_summary(path: str | Path) -> dict[str, Any]:
    from PIL import Image, ImageStat
    p = safe_path(path)
    with Image.open(p) as img:
        rgb = img.convert("RGB")
        stat = ImageStat.Stat(rgb)
        mean_rgb = [float(x) for x in stat.mean]
        stddev_rgb = [float(x) for x in stat.stddev]
        extrema = [[int(a), int(b)] for a, b in stat.extrema]
        brightness = float(sum(mean_rgb) / 3.0)
        return {
            "path": str(p),
            "mode": img.mode,
            "format": img.format,
            "width": int(img.width),
            "height": int(img.height),
            "aspect_ratio": float(img.width / img.height) if img.height else None,
            "size_bytes": int(p.stat().st_size),
            "mean_rgb": mean_rgb,
            "stddev_rgb": stddev_rgb,
            "extrema": extrema,
            "brightness": brightness,
        }


def image_file_metadata(path: str | Path) -> dict[str, Any]:
    from PIL import Image
    p = safe_path(path)
    with Image.open(p) as img:
        info_keys = sorted(str(k) for k in img.info.keys())
        return {
            "path": str(p),
            "format": img.format,
            "mode": img.mode,
            "width": int(img.width),
            "height": int(img.height),
            "bands": list(img.getbands()),
            "size_bytes": int(p.stat().st_size),
            "info_keys": info_keys[:20],
        }


def image_georeference_summary(path: str | Path) -> dict[str, Any]:
    p = safe_path(path)
    summary: dict[str, Any] = {
        "path": str(p),
        "georeferenced": False,
        "source": None,
        "crs": None,
        "transform": None,
        "bounds": None,
        "resolution": None,
    }
    try:
        import rasterio

        with rasterio.open(p) as src:
            summary.update(
                {
                    "source": "rasterio",
                    "georeferenced": bool(src.crs or src.transform),
                    "crs": str(src.crs) if src.crs else None,
                    "transform": [float(v) for v in src.transform] if src.transform else None,
                    "bounds": [float(src.bounds.left), float(src.bounds.bottom), float(src.bounds.right), float(src.bounds.top)],
                    "resolution": [float(src.res[0]), float(src.res[1])] if src.res else None,
                    "width": int(src.width),
                    "height": int(src.height),
                    "count": int(src.count),
                }
            )
    except Exception as exc:
        summary["warning"] = f"georeference metadata not available: {exc}"
    return summary


def _alphaearth_numeric_fields(value: Any, prefix: str = "") -> dict[str, float]:
    out: dict[str, float] = {}
    if isinstance(value, dict):
        for key, item in value.items():
            out.update(_alphaearth_numeric_fields(item, f"{prefix}.{key}" if prefix else str(key)))
    elif isinstance(value, list):
        if value and all(isinstance(item, (int, float)) for item in value):
            out[prefix] = float(statistics.fmean(float(item) for item in value))
        for idx, item in enumerate(value[:10]):
            if isinstance(item, (dict, list)):
                out.update(_alphaearth_numeric_fields(item, f"{prefix}[{idx}]"))
    elif isinstance(value, (int, float)) and prefix:
        out[prefix] = float(value)
    return out


def alphaearth_stats_summary(path: str | Path) -> dict[str, Any]:
    payload = read_json(path)
    if isinstance(payload, dict):
        numeric = _alphaearth_numeric_fields(payload)
        return {
            "path": str(safe_path(path)),
            "top_level_keys": sorted(str(k) for k in payload.keys()),
            "numeric_fields": numeric,
            "numeric_field_count": len(numeric),
            "summary": {k: payload.get(k) for k in list(payload.keys())[:10]},
        }
    return {
        "path": str(safe_path(path)),
        "value_type": type(payload).__name__,
        "preview": payload[:10] if isinstance(payload, list) else payload,
    }


def compare_alphaearth_stats(pre_path: str | Path, post_path: str | Path) -> dict[str, Any]:
    pre = alphaearth_stats_summary(pre_path)
    post = alphaearth_stats_summary(post_path)
    pre_fields = pre.get("numeric_fields") or {}
    post_fields = post.get("numeric_fields") or {}
    shared = sorted(set(pre_fields) & set(post_fields))
    deltas = {k: float(post_fields[k] - pre_fields[k]) for k in shared}
    ranked = sorted(deltas.items(), key=lambda kv: abs(kv[1]), reverse=True)
    return {
        "pre_path": pre.get("path"),
        "post_path": post.get("path"),
        "shared_numeric_fields": len(shared),
        "top_deltas": ranked[:15],
        "mean_abs_delta": float(statistics.fmean(abs(v) for _, v in ranked)) if ranked else None,
        "pre_summary": pre,
        "post_summary": post,
    }


def image_proxy_scores(path: str | Path) -> dict[str, Any]:
    summary = rich_image_summary(path)
    r, g, b = summary["mean_rgb"]
    brightness = summary["brightness"]
    avg_rgb = max((r + g + b) / 3.0, 1e-6)
    balance = max(0.0, 1.0 - (abs(r - g) + abs(g - b) + abs(r - b)) / (3.0 * 255.0))
    flood_score = max(0.0, min(1.0, ((g + b) / (2.0 * avg_rgb)) - 0.75))
    burn_score = max(0.0, min(1.0, ((2.0 * r - g - b) / (2.0 * 255.0)) * (1.2 if brightness < 180 else 0.7)))
    obscuration_score = max(0.0, min(1.0, (balance * 0.6) + (1.0 if brightness > 210 else 0.0) * 0.4))
    haze_score = max(0.0, min(1.0, balance * (0.9 if 110 <= brightness <= 220 else 0.4)))
    return {
        "summary": summary,
        "scores": {
            "flood_proxy": flood_score,
            "burn_proxy": burn_score,
            "obscuration_proxy": obscuration_score,
            "haze_proxy": haze_score,
        },
        "cues": {
            "blue_green_dominance": bool((g + b) > r * 1.05),
            "red_brown_dominance": bool(r > g > b),
            "high_brightness": bool(brightness >= 210),
            "low_color_separation": bool(balance > 0.75),
        },
    }


def heat_index_c(temp_c: float, rh: float) -> float:
    t = temp_c * 9 / 5 + 32
    hi = -42.379 + 2.04901523*t + 10.14333127*rh - 0.22475541*t*rh - 0.00683783*t*t - 0.05481717*rh*rh + 0.00122874*t*t*rh + 0.00085282*t*rh*rh - 0.00000199*t*t*rh*rh
    return (hi - 32) * 5 / 9


def wet_bulb_stull_c(temp_c: float, rh: float) -> float:
    return temp_c * math.atan(0.151977 * math.sqrt(rh + 8.313659)) + math.atan(temp_c + rh) - math.atan(rh - 1.676331) + 0.00391838 * rh ** 1.5 * math.atan(0.023101 * rh) - 4.686035


def simple_series_metric(path: str | Path, value_col: str | None = None) -> dict[str, Any]:
    s = numeric_series(load_table(path), value_col)
    if not len(s):
        return {"count": 0, "warning": "no numeric values"}
    return {"count": int(len(s)), "min": float(s.min()), "max": float(s.max()), "mean": float(s.mean()), "sum": float(s.sum())}


def _pick_column(df, candidates: list[str]) -> str | None:
    lower = {str(c).lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in lower:
            return lower[cand.lower()]
    for c in df.columns:
        cl = str(c).lower()
        if any(cand.lower() in cl for cand in candidates):
            return c
    return None


def _series_from_kwargs(kwargs: dict[str, Any], candidates: list[str] | None = None):
    import pandas as pd
    candidates = candidates or []
    if "values" in kwargs:
        return pd.Series(kwargs["values"], dtype="float64").dropna()
    for cand in candidates:
        cand_norm = cand.lower().replace(".", "").replace("_", "")
        for key, value in kwargs.items():
            key_norm = str(key).lower().replace(".", "").replace("_", "")
            if key_norm in {cand_norm, f"{cand_norm}values", f"{cand_norm}series"} or cand_norm in key_norm:
                if isinstance(value, (list, tuple)):
                    return pd.Series(value, dtype="float64").dropna()
                if isinstance(value, (int, float)):
                    return pd.Series([value], dtype="float64")
    if "path" not in kwargs:
        return pd.Series(dtype="float64")
    df = load_table(kwargs["path"])
    col = kwargs.get("value_col") or _pick_column(df, candidates or [])
    return numeric_series(df, col)


def precip_accumulation_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    s = _series_from_kwargs(kwargs, ["precip", "rain", "tp", "pr"])
    if not len(s):
        return {"count": 0, "warning": "no precipitation-like numeric series found"}
    return {
        "count": int(len(s)),
        "accumulation": float(s.sum()),
        "max_step": float(s.max()),
        "mean_step": float(s.mean()),
        "unit": kwargs.get("unit", "unknown"),
    }


def intensity_duration_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    durations = kwargs.get("durations") or [1, 3, 6, 12, 24]
    out = {}
    for d in durations:
        tmp = rolling_stat(kwargs["path"], kwargs.get("value_col"), int(d), "sum")
        out[str(d)] = tmp
    return {"durations": out}


def heatwave_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    s = _series_from_kwargs(kwargs, ["tmax", "temperature", "temp", "apparent"])
    threshold = float(kwargs.get("threshold", 35))
    if not len(s):
        return {"count": 0, "warning": "no heat-like numeric series found"}
    mask = s >= threshold
    best = cur = 0
    for v in mask:
        cur = cur + 1 if bool(v) else 0
        best = max(best, cur)
    excess = (s - threshold).clip(lower=0)
    return {
        "count": int(len(s)),
        "threshold": threshold,
        "peak": float(s.max()),
        "mean": float(s.mean()),
        "days_or_steps_above_threshold": int(mask.sum()),
        "longest_run": int(best),
        "cumulative_excess": float(excess.sum()),
    }


def cold_spell_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    s = _series_from_kwargs(kwargs, ["tmin", "temperature", "temp", "cold"])
    threshold = float(kwargs.get("threshold", 0))
    if not len(s):
        return {"count": 0, "warning": "no cold-spell-like numeric series found"}
    mask = s <= threshold
    best = cur = 0
    for v in mask:
        cur = cur + 1 if bool(v) else 0
        best = max(best, cur)
    deficit = (threshold - s).clip(lower=0)
    return {
        "count": int(len(s)),
        "threshold": threshold,
        "minimum": float(s.min()),
        "mean": float(s.mean()),
        "steps_below_threshold": int(mask.sum()),
        "longest_run": int(best),
        "cumulative_cold_deficit": float(deficit.sum()),
    }


def hot_dry_vpd_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    import pandas as pd
    temp_threshold = float(kwargs.get("temp_threshold", kwargs.get("threshold", 35)))
    rh_max = float(kwargs.get("rh_max", kwargs.get("dry_rh_threshold", 40)))
    if "path" in kwargs:
        df = load_table(kwargs["path"])
        tcol = kwargs.get("temp_col") or _pick_column(df, ["tmax", "temp", "temperature", "t2m"])
        rhcol = kwargs.get("rh_col") or _pick_column(df, ["rh", "relative_humidity", "humidity"])
        if not tcol or not rhcol:
            return {"warning": "temperature and relative humidity columns are required", "columns": list(df.columns)}
        temps = pd.to_numeric(df[tcol], errors="coerce")
        rhs = pd.to_numeric(df[rhcol], errors="coerce")
    else:
        temps = pd.Series(kwargs.get("temperature_values") or kwargs.get("temps") or kwargs.get("values") or [], dtype="float64")
        rhs = pd.Series(kwargs.get("rh_values") or kwargs.get("relative_humidity_values") or [], dtype="float64")
    rows = [(float(t), float(rh)) for t, rh in zip(temps, rhs) if pd.notna(t) and pd.notna(rh)]
    if not rows:
        return {"count": 0, "warning": "no paired temperature/RH values found"}
    vpd_values = []
    hot_dry = []
    for temp_c, rh in rows:
        es = 0.6108 * math.exp((17.27 * temp_c) / (temp_c + 237.3))
        vpd = es * (1.0 - rh / 100.0)
        vpd_values.append(vpd)
        hot_dry.append(temp_c >= temp_threshold and rh <= rh_max)
    return {
        "count": len(rows),
        "temp_threshold_c": temp_threshold,
        "rh_max_percent": rh_max,
        "hot_dry_count": int(sum(hot_dry)),
        "hot_dry_fraction": float(sum(hot_dry) / len(rows)),
        "max_vpd_kpa": float(max(vpd_values)),
        "mean_vpd_kpa": float(statistics.fmean(vpd_values)),
    }


def urban_pluvial_diagnostics_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    if "path" in kwargs:
        s = _series_from_kwargs(kwargs, ["precip", "rain", "tp", "pr"])
    else:
        import pandas as pd
        s = pd.Series(kwargs.get("values") or kwargs.get("precip_values") or [], dtype="float64").dropna()
    if not len(s):
        return {"count": 0, "warning": "no precipitation series found"}
    durations = kwargs.get("durations") or [1, 3, 6, 24]
    total = float(s.sum())
    peaks: dict[str, float | None] = {}
    for duration in durations:
        d = int(duration)
        if len(s) >= d:
            peaks[str(d)] = float(s.rolling(d, min_periods=d).sum().max())
        else:
            peaks[str(d)] = None
    peak_1 = peaks.get("1") if peaks.get("1") is not None else float(s.max())
    concentration = None if total == 0 else float(peak_1) / total
    burst_threshold = float(kwargs.get("burst_threshold", 50))
    label = "short_duration_urban_pluvial_burst" if peak_1 >= burst_threshold or (concentration is not None and concentration >= 0.45) else "distributed_rainfall_or_nonburst"
    return {
        "count": int(len(s)),
        "event_total": total,
        "peak_by_duration": peaks,
        "peak_step": float(s.max()),
        "rainfall_concentration_ratio": concentration,
        "burst_threshold": burst_threshold,
        "diagnostic_label": label,
    }


def warm_night_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    s = _series_from_kwargs(kwargs, ["tmin", "min_temp", "night", "temperature"])
    threshold = float(kwargs.get("threshold", 20))
    if not len(s):
        return {"count": 0, "warning": "no minimum-temperature-like numeric series found"}
    mask = s >= threshold
    return {"threshold": threshold, "warm_night_count": int(mask.sum()), "count": int(len(s)), "max_minimum_temperature": float(s.max())}


def apparent_temperature_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    import pandas as pd
    if "path" not in kwargs:
        if "temp_c" in kwargs and "rh" in kwargs:
            return {"apparent_temperature_c": heat_index_c(float(kwargs["temp_c"]), float(kwargs["rh"]))}
        return {"warning": "provide path or temp_c/rh"}
    df = load_table(kwargs["path"])
    app_col = _pick_column(df, ["apparent", "heat_index", "feels"])
    if app_col:
        s = numeric_series(df, app_col)
        threshold = float(kwargs.get("threshold", kwargs.get("heat_index_threshold_c", 35.0)))
        stats = simple_series_from_series(s)
        stats.pop("sum", None)
        return {
            "column": app_col,
            "apparent_temperature_peak_c": float(s.max()) if len(s) else None,
            "apparent_temperature_mean_c": float(s.mean()) if len(s) else None,
            "heat_stress_threshold_c": threshold,
            "steps_above_threshold": int((s >= threshold).sum()) if len(s) else 0,
            "fraction_above_threshold": float((s >= threshold).mean()) if len(s) else 0.0,
            "persistence_proxy": int((s >= threshold).sum()) if len(s) else 0,
            "risk_level": None if not len(s) else _risk_label(min(max((float(s.max()) - 30.0) / 20.0, 0.0), 1.0)),
            "series_stats": stats,
        }
    tcol = _pick_column(df, ["temp", "temperature", "t2m", "tmax"])
    rhcol = _pick_column(df, ["rh", "relative_humidity", "humidity"])
    if not tcol or not rhcol:
        return {"warning": "no apparent-temperature column and no temp/rh pair found", "columns": list(df.columns)}
    vals = [heat_index_c(float(t), float(rh)) for t, rh in zip(pd.to_numeric(df[tcol], errors="coerce"), pd.to_numeric(df[rhcol], errors="coerce")) if pd.notna(t) and pd.notna(rh)]
    s = pd.Series(vals)
    threshold = float(kwargs.get("threshold", kwargs.get("heat_index_threshold_c", 35.0)))
    stats = simple_series_from_series(s)
    stats.pop("sum", None)
    return {
        "derived_from": [tcol, rhcol],
        "apparent_temperature_peak_c": float(s.max()) if len(s) else None,
        "apparent_temperature_mean_c": float(s.mean()) if len(s) else None,
        "heat_stress_threshold_c": threshold,
        "steps_above_threshold": int((s >= threshold).sum()) if len(s) else 0,
        "fraction_above_threshold": float((s >= threshold).mean()) if len(s) else 0.0,
        "persistence_proxy": int((s >= threshold).sum()) if len(s) else 0,
        "risk_level": None if not len(s) else _risk_label(min(max((float(s.max()) - 30.0) / 20.0, 0.0), 1.0)),
        "series_stats": stats,
    }


def simple_series_from_series(s) -> dict[str, Any]:
    s = s.dropna()
    if not len(s):
        return {"count": 0, "warning": "empty numeric series"}
    return {"count": int(len(s)), "min": float(s.min()), "max": float(s.max()), "mean": float(s.mean()), "sum": float(s.sum())}


def air_quality_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    s = _series_from_kwargs(kwargs, ["pm25", "pm2.5", "aqi", "o3", "no2"])
    standard = float(kwargs.get("standard", kwargs.get("threshold", 35)))
    if not len(s):
        return {"count": 0, "warning": "no air-quality numeric series found"}
    return {"threshold": standard, "exceedance_count": int((s > standard).sum()), "peak": float(s.max()), "mean": float(s.mean()), "count": int(len(s))}


def fire_hotspot_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    import pandas as pd
    if "path" not in kwargs:
        return {"warning": "provide hotspot table path"}
    df = load_table(kwargs["path"])
    frp = _pick_column(df, ["frp", "power"])
    conf = _pick_column(df, ["confidence"])
    out = {"hotspot_count": int(len(df)), "columns": list(df.columns)}
    if frp:
        s = pd.to_numeric(df[frp], errors="coerce").dropna()
        out.update({"frp_sum": float(s.sum()), "frp_max": float(s.max()), "frp_mean": float(s.mean())})
    if conf:
        out["confidence_values"] = pd.Series(df[conf]).astype(str).value_counts().head(10).to_dict()
    return out


def earthquake_sequence_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    import pandas as pd
    if "path" not in kwargs:
        return {"warning": "provide earthquake catalog path"}
    df = load_table(kwargs["path"])
    mag = _pick_column(df, ["mag", "magnitude"])
    out = {"event_count": int(len(df)), "columns": list(df.columns)}
    if mag:
        s = pd.to_numeric(df[mag], errors="coerce").dropna()
        out.update({"max_magnitude": float(s.max()), "mean_magnitude": float(s.mean()), "magnitude_ge_5": int((s >= 5).sum()), "magnitude_ge_6": int((s >= 6).sum())})
    return out


def enso_phase_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    s = _series_from_kwargs(kwargs, ["nino", "oni", "sst", "anomaly"])
    if not len(s):
        if "value" in kwargs:
            s = __import__("pandas").Series([float(kwargs["value"])])
        else:
            return {"count": 0, "warning": "no ENSO index series found"}
    mean = float(s.mean())
    if mean >= 0.5:
        phase = "El Nino"
    elif mean <= -0.5:
        phase = "La Nina"
    else:
        phase = "Neutral"
    return {"count": int(len(s)), "mean_index": mean, "max_index": float(s.max()), "min_index": float(s.min()), "phase": phase}


def marine_heatwave_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    s = _series_from_kwargs(kwargs, ["sst", "temperature", "hotspot", "dhw"])
    threshold = kwargs.get("threshold")
    if not len(s):
        return {"count": 0, "warning": "no SST/hotspot numeric series found"}
    if threshold is None:
        threshold = float(s.quantile(0.9))
    threshold = float(threshold)
    excess = (s - threshold).clip(lower=0)
    return {"threshold": threshold, "peak": float(s.max()), "mean": float(s.mean()), "days_or_steps_above_threshold": int((s > threshold).sum()), "cumulative_intensity": float(excess.sum()), "count": int(len(s))}


def flood_impact_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    data = {
        "flood_area_km2": kwargs.get("flood_area_km2"),
        "exposed_population": kwargs.get("exposed_population"),
        "road_length_km": kwargs.get("road_length_km"),
    }
    qualifies = False
    if data["flood_area_km2"] is not None:
        qualifies = float(data["flood_area_km2"]) > float(kwargs.get("area_threshold_km2", 10))
    impact = False
    if data["exposed_population"] is not None:
        impact = impact or float(data["exposed_population"]) > float(kwargs.get("population_threshold", 10000))
    if data["road_length_km"] is not None:
        impact = impact or float(data["road_length_km"]) > float(kwargs.get("road_threshold_km", 5))
    data["passes_default_high_impact_rule"] = bool(qualifies and impact)
    return data


def runoff_proxy_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    precip = None
    if "precip_mm" in kwargs:
        precip = float(kwargs["precip_mm"])
    elif "path" in kwargs:
        s = _series_from_kwargs(kwargs, ["precip", "rain", "tp", "pr"])
        precip = float(s.sum()) if len(s) else None
    slope = float(kwargs.get("slope_degrees", kwargs.get("slope", 5)))
    soil_factor = float(kwargs.get("soil_factor", 1.0))
    landcover_factor = float(kwargs.get("landcover_factor", 1.0))
    if precip is None:
        return {"warning": "no precipitation input found"}
    score = precip * (1 + slope / 45.0) * soil_factor * landcover_factor
    return {"precip_mm": precip, "slope_degrees": slope, "runoff_proxy_score": float(score)}


def station_interpolation_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    if "path" in kwargs:
        df = load_table(kwargs["path"])
        col = _pick_column(df, ["pm25", "pm2.5", "aqi", "o3", "no2"]) or kwargs.get("value_col")
        if col and col in df.columns:
            s = numeric_series(df, col)
            standard = float(kwargs.get("standard", kwargs.get("threshold", 35.0)))
            stats = simple_series_from_series(s)
            stats.pop("sum", None)
            return {
                "method": kwargs.get("method", "station_mean_surface_proxy"),
                "station_count": int(len(df)),
                "value_column": col,
                "surface_mean_proxy": float(s.mean()) if len(s) else None,
                "surface_peak_proxy": float(s.max()) if len(s) else None,
                "standard": standard,
                "exceeding_station_count": int((s > standard).sum()) if len(s) else 0,
                "exceeding_station_fraction": float((s > standard).mean()) if len(s) else 0.0,
                "interpolation_caveat": "coarse station summary; not a gridded geostatistical interpolation",
                "series_stats": stats,
            }
        return {"method": "schema_only", "rows": int(len(df)), "columns": list(df.columns), "warning": "no pollution value column found"}
    return {"warning": "provide station table path"}


def ground_failure_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    pga = float(kwargs.get("pga", kwargs.get("shaking", 0.2)))
    slope = float(kwargs.get("slope_degrees", kwargs.get("slope", 10)))
    wetness = float(kwargs.get("wetness", kwargs.get("soil_moisture_factor", 1.0)))
    score = pga * (1 + slope / 30.0) * wetness
    return {"pga_or_shaking": pga, "slope_degrees": slope, "wetness_factor": wetness, "susceptibility_score": float(score)}


def admin_ranking_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    metrics = kwargs.get("metrics") or {}
    if isinstance(metrics, dict) and metrics:
        ranked = sorted(metrics.items(), key=lambda kv: kv[1] if isinstance(kv[1], (int, float)) else 0, reverse=True)
        return {"ranked": [{"item": k, "score": v} for k, v in ranked]}
    if "path" in kwargs:
        return count_points_or_facilities_metric(kwargs["path"], kwargs.get("polygon_path") or kwargs.get("hazard_polygon"), kwargs.get("type_col"))
    return {"warning": "provide metrics dict or path"}


def _risk_label(score: float, breaks: tuple[float, float, float] = (0.33, 0.66, 0.9)) -> str:
    if score >= breaks[2]:
        return "extreme"
    if score >= breaks[1]:
        return "high"
    if score >= breaks[0]:
        return "moderate"
    return "low"


def _mean_or_none(series) -> float | None:
    return None if not len(series) else float(series.mean())


def _max_or_none(series) -> float | None:
    return None if not len(series) else float(series.max())


def _min_or_none(series) -> float | None:
    return None if not len(series) else float(series.min())


def _safe_corr(xs, ys) -> tuple[float | None, str | None]:
    if len(xs) < 2 or len(ys) < 2:
        return None, "too_few_pairs"
    if float(xs.std()) == 0.0 or float(ys.std()) == 0.0:
        return None, "constant_series"
    return float(xs.corr(ys)), None


def streamflow_anomaly_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    flow = _series_from_kwargs(kwargs, ["streamflow", "discharge", "flow", "q"])
    baseline = _series_from_kwargs({**kwargs, "values": kwargs.get("baseline_values")} if "baseline_values" in kwargs else kwargs, ["climatology", "baseline", "normal"])
    if not len(flow):
        return {"warning": "no streamflow/discharge series found"}
    base_mean = float(baseline.mean()) if len(baseline) else float(kwargs.get("baseline", flow.quantile(0.5)))
    base_std = float(baseline.std()) if len(baseline) > 1 else float(flow.std() or 0.0)
    peak = float(flow.max())
    anomaly = peak - base_mean
    z = None if base_std == 0 else anomaly / base_std
    return {
        "count": int(len(flow)),
        "peak_flow": peak,
        "mean_flow": float(flow.mean()),
        "baseline_flow": base_mean,
        "peak_anomaly": anomaly,
        "anomaly_percent": None if base_mean == 0 else float(anomaly / base_mean * 100.0),
        "return_period_proxy_z": z,
        "flood_flow_flag": bool(z is not None and z >= 2.0),
    }


def spei_spi_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    precip = _series_from_kwargs(kwargs, ["precip", "rain", "tp", "pr"])
    pet = _series_from_kwargs(kwargs, ["pet", "evap", "evapotranspiration"])
    if not len(precip):
        return {"warning": "no precipitation series found"}
    balance = precip.copy()
    if len(pet):
        balance = precip.iloc[: min(len(precip), len(pet))].reset_index(drop=True) - pet.iloc[: min(len(precip), len(pet))].reset_index(drop=True)
    scale = int(kwargs.get("scale", kwargs.get("window", 3)))
    scaled = balance.rolling(scale, min_periods=1).sum()
    baseline = _series_from_kwargs({**kwargs, "values": kwargs.get("baseline_values")} if "baseline_values" in kwargs else {}, ["baseline"])
    base_mean = float(baseline.mean()) if len(baseline) else float(scaled.mean())
    base_std = float(baseline.std()) if len(baseline) > 1 else float(scaled.std() or 1.0)
    latest_index = None if base_std == 0 else float((scaled.iloc[-1] - base_mean) / base_std)
    if latest_index is None:
        drought_class = "undefined"
    elif latest_index <= -2:
        drought_class = "extreme drought"
    elif latest_index <= -1.5:
        drought_class = "severe drought"
    elif latest_index <= -1:
        drought_class = "moderate drought"
    elif latest_index >= 1:
        drought_class = "wet anomaly"
    else:
        drought_class = "near normal"
    return {
        "index_type": "SPEI_proxy" if len(pet) else "SPI_proxy",
        "scale_steps": scale,
        "count": int(len(scaled)),
        "latest_index": latest_index,
        "min_index_proxy": None if base_std == 0 else float(((scaled - base_mean) / base_std).min()),
        "water_balance_mean": float(balance.mean()),
        "drought_class": drought_class,
    }


def soil_moisture_percentile_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    soil = _series_from_kwargs(kwargs, ["soil", "soil_moisture", "swvl", "moisture"])
    baseline = _series_from_kwargs({**kwargs, "values": kwargs.get("baseline_values")} if "baseline_values" in kwargs else kwargs, ["baseline", "climatology"])
    if not len(soil):
        return {"warning": "no soil moisture series found"}
    current = float(soil.iloc[-1])
    ref = baseline if len(baseline) else soil
    percentile = float((ref <= current).mean() * 100.0)
    return {
        "current_soil_moisture": current,
        "mean_soil_moisture": float(soil.mean()),
        "baseline_count": int(len(ref)),
        "percentile": percentile,
        "dryness_percentile": float(100.0 - percentile),
        "condition": "very dry" if percentile <= 10 else "dry" if percentile <= 25 else "wet" if percentile >= 75 else "near normal",
    }


def cyclone_track_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    wind = _series_from_kwargs(kwargs, ["wind", "vmax", "max_wind", "wind_speed"])
    pressure = _series_from_kwargs(kwargs, ["pressure", "mslp", "central_pressure"])
    distance = _series_from_kwargs(kwargs, ["distance", "aoi_distance", "coast_distance", "track_distance"])
    out = {
        "track_point_count": int(max(len(wind), len(pressure), len(distance))),
        "max_wind": _max_or_none(wind),
        "min_pressure": _min_or_none(pressure),
        "closest_distance_km": _min_or_none(distance),
    }
    max_wind = out["max_wind"] or 0.0
    out["wind_category_proxy"] = "major_hurricane_or_typhoon" if max_wind >= 50 else "cyclone" if max_wind >= 25 else "weak_or_missing"
    out["near_aoi_flag"] = bool(out["closest_distance_km"] is not None and out["closest_distance_km"] <= float(kwargs.get("near_threshold_km", 100)))
    return out


def storm_surge_proxy_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    wind = _series_from_kwargs(kwargs, ["wind", "vmax", "wind_speed"])
    pressure = _series_from_kwargs(kwargs, ["pressure", "mslp", "central_pressure"])
    tide = _series_from_kwargs(kwargs, ["tide", "water_level"])
    rain = _series_from_kwargs(kwargs, ["rain", "precip", "rainfall"])
    max_wind = _max_or_none(wind) or float(kwargs.get("wind_speed", kwargs.get("wind", 0.0)))
    min_pressure = _min_or_none(pressure)
    pressure_deficit = max(0.0, 1010.0 - (min_pressure if min_pressure is not None else float(kwargs.get("pressure", 1010.0))))
    tide_peak = _max_or_none(tide) or float(kwargs.get("tide", 0.0))
    rain_sum = float(rain.sum()) if len(rain) else float(kwargs.get("rainfall", kwargs.get("rain", 0.0)))
    coast_distance = float(kwargs.get("coast_distance_km", kwargs.get("coast_distance", 10.0)))
    coastal_factor = 1.0 / max(1.0, coast_distance)
    score = (max_wind / 70.0) * 0.45 + (pressure_deficit / 80.0) * 0.25 + max(0.0, tide_peak) * 0.2 + min(rain_sum / 300.0, 1.0) * 0.1
    score = max(0.0, min(1.5, score * (1.0 + coastal_factor)))
    return {
        "max_wind": max_wind,
        "min_pressure": min_pressure,
        "pressure_deficit_hpa": pressure_deficit,
        "peak_tide_or_water_level": tide_peak,
        "rainfall_sum": rain_sum,
        "coast_distance_km": coast_distance,
        "surge_proxy_score": float(score),
        "risk_level": _risk_label(min(score, 1.0)),
    }


def wind_exposure_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    wind = _series_from_kwargs(kwargs, ["wind", "wind_speed", "vmax"])
    threshold = float(kwargs.get("threshold", kwargs.get("wind_threshold", 25.0)))
    exposed_population = kwargs.get("exposed_population")
    if not len(wind):
        return {"warning": "no wind series found"}
    exceed = wind[wind >= threshold]
    return {
        "threshold": threshold,
        "max_wind": float(wind.max()),
        "mean_wind": float(wind.mean()),
        "steps_above_threshold": int(len(exceed)),
        "fraction_above_threshold": float(len(exceed) / len(wind)),
        "exposed_population": None if exposed_population is None else float(exposed_population),
        "wind_exposure_score": float((len(exceed) / len(wind)) * (float(exposed_population or 1) ** 0.25)),
    }


def teleconnection_lag_correlation_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    import pandas as pd
    index = _series_from_kwargs(kwargs, ["index", "enso", "nino", "oni"])
    hazard = _series_from_kwargs(kwargs, ["hazard", "rain", "precip", "temperature", "impact"])
    if not len(index) or not len(hazard):
        return {"warning": "provide both climate index and hazard series"}
    n = min(len(index), len(hazard))
    x = index.iloc[:n].reset_index(drop=True)
    y = hazard.iloc[:n].reset_index(drop=True)
    lags = kwargs.get("lags", [-3, -2, -1, 0, 1, 2, 3])
    rows = []
    for lag in lags:
        lag = int(lag)
        if lag > 0:
            xs, ys = x.iloc[:-lag], y.iloc[lag:]
        elif lag < 0:
            xs, ys = x.iloc[-lag:], y.iloc[:lag]
        else:
            xs, ys = x, y
        corr, reason = _safe_corr(pd.Series(xs).reset_index(drop=True), pd.Series(ys).reset_index(drop=True))
        rows.append({"lag": lag, "correlation": corr, "paired_count": int(len(xs)), "null_reason": reason})
    best = max(rows, key=lambda r: abs(r["correlation"] or 0.0))
    return {"lag_correlations": rows, "best_lag": best["lag"], "best_correlation": best["correlation"]}


def snow_ice_anomaly_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    series = _series_from_kwargs(kwargs, ["snow", "ice", "snow_cover", "sea_ice", "extent"])
    baseline = _series_from_kwargs({**kwargs, "values": kwargs.get("baseline_values")} if "baseline_values" in kwargs else kwargs, ["baseline", "climatology"])
    if not len(series):
        return {"warning": "no snow/ice series found"}
    current = float(series.iloc[-1])
    base = float(baseline.mean()) if len(baseline) else float(series.mean())
    anomaly = current - base
    return {"current": current, "baseline": base, "anomaly": anomaly, "anomaly_percent": None if base == 0 else float(anomaly / base * 100.0), "condition": "deficit" if anomaly < 0 else "surplus"}


def burned_area_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    area = _series_from_kwargs(kwargs, ["burned_area", "burn_area", "area", "dnbr", "nbr"])
    if not len(area):
        return {"warning": "no burned-area, NBR, or dNBR series found"}
    threshold = float(kwargs.get("severity_threshold", kwargs.get("threshold", area.quantile(0.75))))
    high = area[area >= threshold]
    return {"burned_area_or_index_sum": float(area.sum()), "peak_burn_severity": float(area.max()), "mean_burn_severity": float(area.mean()), "high_severity_count": int(len(high)), "high_severity_fraction": float(len(high) / len(area)), "threshold": threshold}


def fire_weather_index_proxy_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    temp = _series_from_kwargs(kwargs, ["temperature", "temp", "tmax", "t2m"])
    rh = _series_from_kwargs(kwargs, ["humidity", "relative_humidity", "rh"])
    wind = _series_from_kwargs(kwargs, ["wind", "wind_speed", "u10", "v10"])
    rain = _series_from_kwargs(kwargs, ["rain", "precip", "rainfall", "tp"])
    if not len(temp):
        return {"warning": "no temperature series found"}
    t = float(temp.max())
    h = float(rh.mean()) if len(rh) else float(kwargs.get("rh", kwargs.get("relative_humidity", 50.0)))
    w = float(wind.max()) if len(wind) else float(kwargs.get("wind", kwargs.get("wind_speed", 10.0)))
    r = float(rain.sum()) if len(rain) else float(kwargs.get("rain", kwargs.get("rainfall", 0.0)))
    heat_component = max(0.0, (t - 20.0) / 25.0)
    dryness_component = max(0.0, (100.0 - h) / 100.0)
    wind_component = max(0.0, w / 50.0)
    rain_suppression = max(0.0, min(1.0, r / 20.0))
    score = max(0.0, (0.4 * heat_component + 0.35 * dryness_component + 0.25 * wind_component) * (1.0 - 0.7 * rain_suppression))
    return {
        "temperature_peak_c": t,
        "relative_humidity_mean": h,
        "wind_peak": w,
        "rain_total": r,
        "heat_component": heat_component,
        "dryness_component": dryness_component,
        "wind_component": wind_component,
        "rain_suppression": rain_suppression,
        "fwi_proxy": float(score),
        "risk_level": _risk_label(min(score, 1.0)),
    }


def smoke_pm_lag_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    import pandas as pd
    smoke = _series_from_kwargs(kwargs, ["smoke", "frp", "hotspot", "aod"])
    pm = _series_from_kwargs(kwargs, ["pm25", "pm2.5", "aqi", "pollution"])
    if not len(smoke) or not len(pm):
        return {"warning": "provide smoke/fire and PM/AQI series"}
    n = min(len(smoke), len(pm))
    x = smoke.iloc[:n].reset_index(drop=True)
    y = pm.iloc[:n].reset_index(drop=True)
    lags = kwargs.get("lags", [0, 1, 2, 3])
    rows = []
    for lag in lags:
        lag = int(lag)
        xs = x.iloc[: n - lag] if lag > 0 else x
        ys = y.iloc[lag:] if lag > 0 else y
        corr, reason = _safe_corr(pd.Series(xs).reset_index(drop=True), pd.Series(ys).reset_index(drop=True))
        rows.append({"lag": lag, "correlation": corr, "paired_count": int(len(xs)), "null_reason": reason})
    best = max(rows, key=lambda r: abs(r["correlation"] or 0.0))
    return {"lag_correlations": rows, "best_lag": best["lag"], "best_correlation": best["correlation"], "pm_peak": float(pm.max()), "smoke_peak": float(smoke.max())}


def shakemap_exposure_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    shaking = _series_from_kwargs(kwargs, ["mmi", "pga", "pgv", "shaking", "intensity"])
    exposure = _series_from_kwargs(kwargs, ["population", "exposure", "facilities"])
    if not len(shaking):
        return {"warning": "no shaking intensity series found"}
    threshold = float(kwargs.get("threshold", kwargs.get("mmi_threshold", 6.0)))
    exposed = float(exposure.sum()) if len(exposure) else float(kwargs.get("exposed_population", kwargs.get("population", 0.0)))
    return {"max_intensity": float(shaking.max()), "mean_intensity": float(shaking.mean()), "cells_above_threshold": int((shaking >= threshold).sum()), "threshold": threshold, "exposed_population_or_assets": exposed, "shake_exposure_score": float((shaking.max() / max(threshold, 1.0)) * (exposed ** 0.25 if exposed > 0 else 1.0))}


def landslide_trigger_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    rain = _series_from_kwargs(kwargs, ["rain", "precip", "rainfall"])
    slope = float(kwargs.get("slope_degrees", kwargs.get("slope", 15.0)))
    wetness = float(kwargs.get("antecedent_wetness", kwargs.get("soil_moisture", kwargs.get("wetness", 1.0))))
    rain_total = float(rain.sum()) if len(rain) else float(kwargs.get("rainfall", kwargs.get("rain", 0.0)))
    score = (rain_total / 200.0) * 0.55 + (slope / 45.0) * 0.3 + min(wetness, 2.0) / 2.0 * 0.15
    return {"rainfall_total": rain_total, "slope_degrees": slope, "antecedent_wetness": wetness, "landslide_trigger_index": float(score), "risk_level": _risk_label(min(score, 1.0))}


def volcano_ash_extent_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    ash = _series_from_kwargs(kwargs, ["ash", "ash_extent", "plume", "area"])
    area = float(ash.sum()) if len(ash) else float(kwargs.get("ash_area_km2", kwargs.get("area_km2", 0.0)))
    height = kwargs.get("plume_height_km")
    return {"ash_extent_km2_or_index": area, "plume_height_km": None if height is None else float(height), "affected_population": kwargs.get("affected_population"), "aviation_disruption_proxy": float(area * (float(height or 1.0) ** 0.5))}


def so2_anomaly_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    so2 = _series_from_kwargs(kwargs, ["so2", "sulfur", "plume"])
    baseline = _series_from_kwargs({**kwargs, "values": kwargs.get("baseline_values")} if "baseline_values" in kwargs else kwargs, ["baseline", "climatology"])
    if not len(so2):
        return {"warning": "no SO2 series found"}
    base = float(baseline.mean()) if len(baseline) else float(kwargs.get("baseline", so2.mean()))
    peak = float(so2.max())
    return {"so2_peak": peak, "so2_mean": float(so2.mean()), "baseline": base, "peak_anomaly": peak - base, "anomaly_ratio": None if base == 0 else float(peak / base)}


def tsunami_coastal_exposure_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    wave = _series_from_kwargs(kwargs, ["wave", "tsunami", "inundation", "runup"])
    height = _max_or_none(wave) or float(kwargs.get("wave_height_m", kwargs.get("runup_m", 0.0)))
    pop = float(kwargs.get("coastal_population", kwargs.get("population", kwargs.get("exposed_population", 0.0))))
    elev = float(kwargs.get("mean_elevation_m", kwargs.get("elevation_m", 5.0)))
    score = max(0.0, height / max(elev, 0.5)) * (pop ** 0.25 if pop > 0 else 1.0)
    return {"wave_or_runup_height_m": height, "coastal_population": pop, "mean_elevation_m": elev, "tsunami_exposure_score": float(score), "risk_level": _risk_label(min(score / 5.0, 1.0))}


def dust_storm_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    visibility = _series_from_kwargs(kwargs, ["visibility", "vis"])
    aod = _series_from_kwargs(kwargs, ["aod", "dust"])
    pm = _series_from_kwargs(kwargs, ["pm10", "pm25", "pm2.5", "aqi"])
    wind = _series_from_kwargs(kwargs, ["wind", "wind_speed"])
    low_vis = None if not len(visibility) else float((visibility <= float(kwargs.get("visibility_threshold_km", 5.0))).mean())
    score = 0.0
    if len(aod):
        score += min(float(aod.max()) / 3.0, 1.0) * 0.35
    if len(pm):
        score += min(float(pm.max()) / 500.0, 1.0) * 0.3
    if len(wind):
        score += min(float(wind.max()) / 25.0, 1.0) * 0.2
    if low_vis is not None:
        score += low_vis * 0.15
    return {"visibility_low_fraction": low_vis, "aod_peak": _max_or_none(aod), "pm_peak": _max_or_none(pm), "wind_peak": _max_or_none(wind), "dust_storm_score": float(score), "risk_level": _risk_label(min(score, 1.0))}


def tide_surge_compound_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    tide = _series_from_kwargs(kwargs, ["tide", "water_level"])
    surge = _series_from_kwargs(kwargs, ["surge", "storm_surge"])
    rain = _series_from_kwargs(kwargs, ["rain", "precip", "rainfall"])
    tide_peak = _max_or_none(tide) or float(kwargs.get("tide", 0.0))
    surge_peak = _max_or_none(surge) or float(kwargs.get("surge_proxy", kwargs.get("surge", 0.0)))
    rain_total = float(rain.sum()) if len(rain) else float(kwargs.get("rainfall", kwargs.get("rain", 0.0)))
    joint = tide_peak + surge_peak
    score = min(joint / 3.0, 1.0) * 0.65 + min(rain_total / 250.0, 1.0) * 0.35
    return {"tide_peak": tide_peak, "surge_peak": surge_peak, "rainfall_total": rain_total, "joint_water_level_proxy": joint, "compound_flood_index": float(score), "risk_level": _risk_label(score)}


def multihazard_overlap_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    metrics = kwargs.get("hazard_scores") or kwargs.get("metrics") or {}
    weights = kwargs.get("weights") or {}
    if isinstance(metrics, dict) and metrics:
        parts = []
        total = 0.0
        wsum = 0.0
        for key, value in metrics.items():
            if not isinstance(value, (int, float)):
                continue
            w = float(weights.get(key, 1.0)) if isinstance(weights, dict) else 1.0
            v = max(0.0, min(1.0, float(value)))
            parts.append({"hazard": key, "score": v, "weight": w, "weighted": v * w})
            total += v * w
            wsum += abs(w)
        score = None if wsum == 0 else total / wsum
        return {"overlap_score": score, "hazard_count": len(parts), "parts": parts, "risk_level": None if score is None else _risk_label(score)}
    series = _series_from_kwargs(kwargs, ["hazard", "overlap", "score"])
    if not len(series):
        return {"warning": "provide hazard_scores dict or overlap score series"}
    return {"overlap_score": float(series.mean()), "hazard_count": int(len(series)), "max_overlap": float(series.max()), "risk_level": _risk_label(float(series.mean()))}


def normalize_tool_kwargs(tool_name: str, kwargs: dict[str, Any]) -> dict[str, Any]:
    """Accept registry-style argument names while keeping older path-based callers working."""
    out = dict(kwargs)
    path_aliases = [
        "image_path", "raster_path", "vector_path", "lst_raster", "raster_stack",
        "osm_json", "complaints_table", "admin_path", "network_path",
    ]
    for alias in path_aliases:
        if "path" not in out and alias in out:
            out["path"] = out[alias]
    if "line_path" not in out:
        for alias in ("roads", "road_vector", "line_vector"):
            if alias in out:
                out["line_path"] = out[alias]
                out.setdefault("path", out[alias])
                break
    if "points_path" not in out:
        for alias in ("facilities", "facilities_vector", "facility_points", "buildings", "building_footprints", "population_points"):
            if alias in out:
                out["points_path"] = out[alias]
                out.setdefault("path", out[alias])
                break
    if "polygon_path" not in out:
        for alias in ("hazard_polygon", "aoi_vector", "aoi_path", "polygon_vector"):
            if alias in out:
                out["polygon_path"] = out[alias]
                break
    if "pre_path" not in out and "pre_image" in out:
        out["pre_path"] = out["pre_image"]
        out.setdefault("path", out["pre_image"])
    if "post_path" not in out and "post_image" in out:
        out["post_path"] = out["post_image"]
    if "path_a" not in out:
        for alias in ("nir_band", "green_band", "band_a"):
            if alias in out:
                out["path_a"] = out[alias]
                break
    if "path_b" not in out:
        for alias in ("red_band", "swir_band", "nir_or_swir_band", "band_b"):
            if alias in out:
                out["path_b"] = out[alias]
                break
    if "temp_c" not in out:
        for alias in ("temp", "temperature", "temperature_c", "t2m"):
            if alias in out:
                out["temp_c"] = out[alias]
                break
    if "rh" not in out:
        for alias in ("relative_humidity", "humidity"):
            if alias in out:
                out["rh"] = out[alias]
                break
    if tool_name == "estimate_population_exposure" and "points_path" not in out and "population_grid" in out:
        out["path"] = out["population_grid"]
    return out


def weighted_hazard_score_metric(kwargs: dict[str, Any]) -> dict[str, Any]:
    metrics = kwargs.get("metrics") or {}
    weights = kwargs.get("weights") or {}
    normalization = kwargs.get("normalization") or {}
    score = 0.0
    weight_sum = 0.0
    parts = []
    if isinstance(metrics, dict):
        for key, value in metrics.items():
            if not isinstance(value, (int, float)):
                continue
            raw = float(value)
            norm = raw
            if isinstance(normalization, dict) and isinstance(normalization.get(key), dict):
                rule = normalization[key]
                lo = float(rule.get("min", 0.0))
                hi = float(rule.get("max", 1.0))
                norm = 0.0 if hi == lo else max(0.0, min(1.0, (raw - lo) / (hi - lo)))
            w = float(weights.get(key, 1.0)) if isinstance(weights, dict) else 1.0
            contribution = norm * w
            score += contribution
            weight_sum += abs(w)
            parts.append({"metric": key, "raw_value": raw, "normalized_value": norm, "weight": w, "contribution": contribution})
    normalized_score = None if weight_sum == 0 else score / weight_sum
    return {"score": score, "normalized_score": normalized_score, "parts": parts, "weight_sum": weight_sum}


def required_computation_targets_metric(question: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    q = question.lower()
    patterns = {
        "precipitation_accumulation": [r"precip", r"rain", r"gpm", r"chirps", r"accumulat"],
        "temperature_heat_stress": [r"temp", r"heat", r"tmax", r"wet[- ]?bulb", r"apparent", r"humid"],
        "flood_extent_area": [r"flood", r"inundat", r"water", r"ndwi", r"sentinel"],
        "fire_burn_smoke": [r"fire", r"burn", r"nbr", r"hotspot", r"frp", r"smoke"],
        "air_quality_exceedance": [r"pm2?\\.??5", r"aqi", r"o3", r"air quality", r"smoke"],
        "population_facility_exposure": [r"population", r"exposure", r"hospital", r"school", r"facility", r"worldpop"],
        "road_network_disruption": [r"road", r"bridge", r"network", r"osm", r"access"],
        "cyclone_wind_surge": [r"cyclone", r"hurricane", r"typhoon", r"wind", r"surge", r"track"],
        "earthquake_shaking": [r"earthquake", r"magnitude", r"shakemap", r"pga", r"mmi"],
        "marine_heatwave_coral": [r"marine", r"sst", r"coral", r"bleach", r"ocean"],
        "enso_teleconnection": [r"enso", r"nino", r"oni", r"teleconnection"],
        "visual_change_interpretation": [r"image", r"visual", r"satellite", r"true.?color", r"embedding"],
    }
    targets = []
    for name, pats in patterns.items():
        hits = [pat for pat in pats if re.search(pat, q, re.I)]
        if hits:
            targets.append({"target": name, "matched_patterns": hits})
    hazard = None
    if metadata:
        hazard = metadata.get("hazard_family") or metadata.get("hazard") or metadata.get("event_type")
    return {"targets": targets, "metadata_hazard": hazard, "target_count": len(targets)}


def dispatch(tool_name: str, **kwargs: Any) -> dict[str, Any]:
    try:
        kwargs = normalize_tool_kwargs(tool_name, kwargs)
        tool_name = TOOL_ALIASES.get(tool_name, tool_name)
        if tool_name == "list_event_package_files":
            return ok(tool_name, list_files(kwargs["event_id"], kwargs.get("recursive", True), kwargs.get("layer_filter"), kwargs.get("packages_root")))
        if tool_name == "read_event_metadata":
            return ok(tool_name, load_event_metadata(kwargs["event_id"], kwargs.get("packages_root")))
        if tool_name == "get_event_aoi":
            meta = load_event_metadata(kwargs["event_id"], kwargs.get("packages_root"))
            data = {k: meta.get(k) for k in ("aoi", "bbox", "geometry", "region", "scale") if k in meta}
            data["has_explicit_geometry"] = any(k in meta for k in ("aoi", "bbox", "geometry"))
            if not data["has_explicit_geometry"]:
                data["warning"] = "no explicit AOI geometry; using metadata spatial context"
            return ok(tool_name, data or {"warning": "no explicit AOI in metadata", "metadata_region": meta.get("region")})
        if tool_name.startswith("find_files_by_"):
            files = list_files(kwargs.get("event_id"), True, packages_root=kwargs.get("packages_root"))
            if tool_name == "find_files_by_layer":
                key = str(kwargs.get("layer", "")).lower()
                files = [f for f in files if key in f["layer"].lower() or key in f["relative_path"].lower()]
            elif tool_name == "find_files_by_keyword":
                keys = [str(x).lower() for x in kwargs.get("keywords", [])]
                files = [f for f in files if any(k in f["relative_path"].lower() for k in keys)]
            elif tool_name == "find_files_by_extension":
                exts = {str(x).lower().lstrip(".") for x in kwargs.get("extensions", [])}
                files = [f for f in files if f["suffix"].lower().lstrip(".") in exts]
            return ok(tool_name, files)
        if tool_name in {"summarize_event_inventory", "check_required_layers_present"}:
            files = list_files(kwargs["event_id"], True, packages_root=kwargs.get("packages_root"))
            counts: dict[str, int] = {}
            for f in files:
                counts[f["layer"]] = counts.get(f["layer"], 0) + 1
            data = {"total_files": len(files), "layers": counts}
            if tool_name == "check_required_layers_present":
                req = kwargs.get("required_layers", [])
                data["required"] = {r: any(str(r).lower() in k.lower() for k in counts) for r in req}
            return ok(tool_name, data)
        if tool_name == "resolve_relative_package_path":
            root = event_dir(kwargs["event_id"], kwargs.get("packages_root")).resolve()
            p = (root / kwargs["relative_path"]).resolve()
            if root not in p.parents and p != root:
                return fail(tool_name, "path escapes event package")
            return ok(tool_name, {"path": str(p), "exists": p.exists()})
        if tool_name == "inspect_package_file":
            return ok(tool_name, inspect_package_file_metric(kwargs["path"], int(kwargs.get("max_chars", 4000)), int(kwargs.get("max_rows", 5)), int(kwargs.get("max_members", 50))))
        if tool_name == "list_archive_contents":
            return ok(tool_name, list_archive_contents_metric(kwargs["path"], int(kwargs.get("max_members", 200))))
        if tool_name == "summarize_archive_member":
            return ok(tool_name, summarize_archive_member_metric(kwargs["path"], kwargs.get("member"), int(kwargs.get("max_chars", 4000)), int(kwargs.get("max_rows", 5))))
        if tool_name == "infer_data_layer_from_filename":
            path = str(kwargs.get("path", ""))
            norm = path.replace("\\", "/").lower()
            if "/data/" in norm:
                layer_guess = norm.split("/data/", 1)[1].split("/", 1)[0]
            elif "/metadata/" in norm:
                layer_guess = "metadata"
            elif "/questions/" in norm or "question" in norm:
                layer_guess = "task"
            else:
                suffix = Path(path).suffix.lower()
                layer_guess = {
                    ".csv": "tabular",
                    ".json": "json",
                    ".geojson": "vector",
                    ".tif": "raster",
                    ".tiff": "raster",
                    ".jpg": "image",
                    ".jpeg": "image",
                    ".png": "image",
                    ".pdf": "report",
                    ".html": "report",
                    ".md": "report",
                    ".txt": "report",
                }.get(suffix, "unknown")
            return ok(tool_name, {"path": path, "layer_guess": layer_guess})
        if tool_name == "build_task_file_manifest":
            task_id = kwargs["task_id"]
            event_id = task_id.split("_Q", 1)[0].split("_")[0]
            files = list_files(event_id)
            question = str(kwargs.get("question") or kwargs.get("task_text") or "")
            candidates = dispatch("select_candidate_files_for_question", question=question, file_manifest=files)["data"] if question else []
            return ok(tool_name, {"task_id": task_id, "event_id": event_id, "files": files, "candidate_files": candidates[:20]})
        if tool_name == "select_candidate_files_for_question":
            question = str(kwargs.get("task_text") or kwargs.get("question") or "").lower()
            manifest = kwargs.get("file_manifest") or []
            scored = []
            for f in manifest:
                rel = f.get("relative_path", str(f)).lower()
                score = sum(1 for tok in re.findall(r"[a-z0-9_]{3,}", question) if tok in rel)
                if score:
                    scored.append({"score": score, **(f if isinstance(f, dict) else {"relative_path": str(f)})})
            return ok(tool_name, sorted(scored, key=lambda x: -x["score"]))
        if tool_name == "extract_required_computation_targets":
            return ok(tool_name, required_computation_targets_metric(str(kwargs.get("question") or kwargs.get("task_text") or ""), kwargs.get("metadata")))
        if tool_name == "compute_weighted_hazard_score":
            return ok(tool_name, weighted_hazard_score_metric(kwargs))
        if tool_name in {"read_text_or_html", "read_pdf_text"}:
            p = kwargs.get("path") or (kwargs.get("paths") or [None])[0]
            if tool_name == "read_pdf_text" and str(p).lower().endswith(".pdf"):
                try:
                    import pypdf
                    reader = pypdf.PdfReader(str(safe_path(p)))
                    text = "\n".join(page.extract_text() or "" for page in reader.pages)
                    return ok(tool_name, {"path": str(safe_path(p)), "pages": len(reader.pages), "text": text[: kwargs.get("max_chars", len(text))]})
                except Exception as e:
                    return fail(tool_name, f"PDF extraction failed: {e}")
            return ok(tool_name, read_text(p, kwargs.get("max_chars")))
        typed_extractors = {
            "extract_event_time_claims": ["date", "day", "week", "month", "year", "period", "from", "between", "during", "peak"],
            "extract_location_claims": ["city", "province", "state", "country", "river", "basin", "coast", "island", "near", "in "],
            "extract_impact_claims": ["death", "fatal", "injur", "displaced", "affected", "damage", "loss", "outage", "closed", "disruption"],
            "extract_hazard_magnitude_claims": ["rain", "precip", "wind", "temp", "heat", "magnitude", "aqi", "pm", "frp", "flood", "surge"],
            "extract_response_action_claims": ["warning", "evacuat", "shelter", "rescue", "closed", "declared", "alert", "order", "response"],
        }
        if tool_name in typed_extractors:
            paths = kwargs.get("paths") or ([kwargs["path"]] if "path" in kwargs else [])
            snippets = text_snippets(paths, typed_extractors[tool_name], kwargs.get("window", 160)) if paths else []
            claims = []
            date_re = re.compile(r"\b(?:19|20)\d{2}(?:[-/\.]\d{1,2})?(?:[-/\.]\d{1,2})?\b")
            number_re = re.compile(r"[-+]?\d+(?:,\d{3})*(?:\.\d+)?")
            for snip in snippets:
                text = snip.get("snippet", "")
                claims.append({
                    "path": snip.get("path"),
                    "keyword": snip.get("keyword"),
                    "claim_text": text,
                    "dates": date_re.findall(text),
                    "numbers": number_re.findall(text)[:10],
                    "claim_type": tool_name.replace("extract_", "").replace("_claims", ""),
                })
            return ok(tool_name, {"claims": claims, "claim_count": len(claims)})
        if tool_name in {"parse_report_source_metadata", "build_report_event_timeline", "extract_report_numeric_observations", "extract_report_causal_chains"}:
            paths = kwargs.get("paths") or ([kwargs["path"]] if "path" in kwargs else [])
            if tool_name == "parse_report_source_metadata":
                rows = []
                for p in paths:
                    item = read_text(p, kwargs.get("max_chars", 4000))
                    text = item["text"]
                    urls = re.findall(r"https?://[^\s)>\"]+", text)
                    title = Path(item["path"]).stem.replace("_", " ").replace("-", " ")
                    date_match = re.search(r"\b(19|20)\d{2}[-/\.]\d{1,2}[-/\.]\d{1,2}\b|\b(19|20)\d{2}\b", text)
                    rows.append({
                        "path": item["path"],
                        "title_guess": title,
                        "publication_date_guess": date_match.group(0) if date_match else None,
                        "urls": urls[:5],
                        "document_type": Path(item["path"]).suffix.lower().lstrip(".") or "text",
                    })
                return ok(tool_name, {"sources": rows})
            if tool_name == "extract_report_numeric_observations":
                units = kwargs.get("unit_patterns") or [
                    "mm", "km", "km2", "m/s", "mph", "kt", "knot", "degc", "c", "f",
                    "people", "persons", "deaths", "fatalities", "homes", "houses", "ha",
                    "hectares", "aqi", "ug/m3", "µg/m3", "usd", "million", "billion",
                ]
                unit_pat = "|".join(re.escape(str(u)) for u in units)
                rows = []
                for p in paths:
                    item = read_text(p)
                    for m in re.finditer(rf"(?P<value>[-+]?\d+(?:,\d{{3}})*(?:\.\d+)?)\s*(?P<unit>{unit_pat})?\b", item["text"], re.I):
                        start, end = m.span()
                        rows.append({
                            "path": item["path"],
                            "value_text": m.group("value"),
                            "unit": m.group("unit"),
                            "snippet": item["text"][max(0, start - 120): min(len(item["text"]), end + 120)],
                        })
                        if len(rows) >= 200:
                            break
                return ok(tool_name, {"observations": rows})
            if tool_name == "extract_report_causal_chains":
                causal_words = kwargs.get("causal_words") or ["caused", "triggered", "led to", "resulted in", "due to", "because", "following", "after"]
                snippets = text_snippets(paths, causal_words, kwargs.get("window", 180)) if paths else []
                return ok(tool_name, {"causal_snippets": snippets, "causal_words": causal_words})
            timeline_inputs = []
            for key in ("time_claims", "hazard_claims", "impact_claims", "response_claims"):
                value = kwargs.get(key) or []
                if isinstance(value, dict):
                    value = value.get("snippets") or value.get("claims") or [value]
                for row in value if isinstance(value, list) else [value]:
                    timeline_inputs.append({"source_group": key, "claim": row})
            rows = []
            for i, row in enumerate(timeline_inputs):
                text = json.dumps(row.get("claim"), ensure_ascii=False) if not isinstance(row.get("claim"), str) else row.get("claim")
                date_match = re.search(r"\b(19|20)\d{2}[-/\.]\d{1,2}[-/\.]\d{1,2}\b|\b(19|20)\d{2}\b", text)
                rows.append({"order": i, "date_or_year": date_match.group(0) if date_match else None, **row})
            return ok(tool_name, {"timeline": rows})
        if tool_name == "deduplicate_report_claims":
            claims = kwargs.get("claims") or []
            seen = set()
            rows = []
            for claim in claims:
                text = claim if isinstance(claim, str) else json.dumps(claim, ensure_ascii=False, sort_keys=True)
                key = re.sub(r"\s+", " ", text.lower()).strip()[:240]
                if key in seen:
                    continue
                seen.add(key)
                rows.append(claim)
            return ok(tool_name, {"claims": rows, "input_count": len(claims), "deduplicated_count": len(rows)})
        if tool_name == "classify_claim_type":
            claim_text = str(kwargs.get("claim_text") or kwargs.get("text") or "")
            classes = {
                "hazard_magnitude": r"rain|wind|temp|magnitude|aqi|pm|frp|surge|flood|fire",
                "impact": r"death|injur|damage|loss|affected|displaced|outage|closed",
                "response": r"warning|evacuat|shelter|rescue|declared|alert|order",
                "location": r"city|province|state|country|river|basin|coast|island",
                "time": r"\b(19|20)\d{2}\b|date|during|between|from|to|peak",
            }
            scores = {k: len(re.findall(v, claim_text, re.I)) for k, v in classes.items()}
            label = max(scores, key=scores.get) if any(scores.values()) else "unclassified"
            return ok(tool_name, {"claim_type": label, "scores": scores})
        if tool_name.startswith("extract_"):
            paths = kwargs.get("paths") or ([kwargs["path"]] if "path" in kwargs else [])
            keywords = kwargs.get("keywords") or ["death", "damage", "evacuat", "rain", "wind", "heat", "flood", "fire", "warning", "impact", "magnitude"]
            if paths:
                return ok(tool_name, {"snippets": text_snippets(paths, keywords, kwargs.get("window", 160))})
            return ok(tool_name, {"message": "claim utility executed", "input_keys": sorted(kwargs.keys())})
        if tool_name == "load_table_schema":
            return ok(tool_name, table_schema(kwargs["path"]))
        if tool_name == "summarize_table_or_json":
            return ok(tool_name, summarize_table_or_json_metric(kwargs["path"], int(kwargs.get("max_rows", 5)), bool(kwargs.get("numeric_summary", True))))
        if tool_name == "compute_unit_conversion_or_ratio":
            return ok(tool_name, unit_conversion_or_ratio_metric(kwargs))
        if tool_name == "filter_table_rows":
            import pandas as pd
            df = load_table(kwargs["path"])
            initial_rows = int(len(df))
            if kwargs.get("time_col") and kwargs["time_col"] in df.columns:
                t = pd.to_datetime(df[kwargs["time_col"]], errors="coerce", utc=True)
                if kwargs.get("start"):
                    df = df[t >= pd.to_datetime(kwargs["start"], utc=True)]
                    t = pd.to_datetime(df[kwargs["time_col"]], errors="coerce", utc=True)
                if kwargs.get("end"):
                    df = df[t <= pd.to_datetime(kwargs["end"], utc=True)]
            for key, value in (kwargs.get("conditions") or {}).items():
                if key in df.columns:
                    df = df[df[key].astype(str) == str(value)]
            return ok(tool_name, {"input_rows": initial_rows, "rows": int(len(df)), "columns": list(df.columns), "sample": df.head(10).to_dict(orient="records")})
        if tool_name == "select_table_columns":
            df = load_table(kwargs["path"])
            cols = [c for c in (kwargs.get("columns") or kwargs.get("value_cols") or []) if c in df.columns]
            if not cols:
                cols = list(df.columns)
            sub = df[cols]
            return ok(tool_name, {"rows": int(len(sub)), "columns": cols, "sample": sub.head(10).to_dict(orient="records")})
        if tool_name == "normalize_time_column":
            import pandas as pd
            df = load_table(kwargs["path"])
            time_col = kwargs.get("time_col") or _pick_column(df, ["date", "time", "timestamp"])
            if not time_col:
                return ok(tool_name, {"warning": "no time-like column found", "columns": list(df.columns)})
            t = pd.to_datetime(df[time_col], errors="coerce", utc=True)
            return ok(tool_name, {
                "time_col": time_col,
                "valid_times": int(t.notna().sum()),
                "min_time": t.min().isoformat() if t.notna().any() else None,
                "max_time": t.max().isoformat() if t.notna().any() else None,
                "sample_iso": [x.isoformat() if pd.notna(x) else None for x in t.head(10)],
            })
        if tool_name == "resample_timeseries":
            import pandas as pd
            df = load_table(kwargs["path"])
            time_col = kwargs.get("time_col") or _pick_column(df, ["date", "time", "timestamp"])
            if not time_col:
                return ok(tool_name, {"warning": "no time-like column found", "columns": list(df.columns)})
            df["_time"] = pd.to_datetime(df[time_col], errors="coerce", utc=True)
            df = df.dropna(subset=["_time"]).set_index("_time")
            cols = kwargs.get("value_cols") or [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
            agg = kwargs.get("agg", "sum")
            freq = kwargs.get("freq", kwargs.get("rule", "D"))
            res = getattr(df[cols].resample(freq), agg)() if hasattr(df[cols].resample(freq), agg) else df[cols].resample(freq).sum()
            return ok(tool_name, {"freq": freq, "agg": agg, "rows": int(len(res)), "columns": list(res.columns), "sample": res.reset_index().head(10).to_dict(orient="records")})
        if tool_name == "join_timeseries_on_time":
            import pandas as pd
            paths = kwargs.get("paths") or ([kwargs["path"]] if "path" in kwargs else [])
            time_col = kwargs.get("time_col") or "date"
            frames = []
            for i, path in enumerate(paths):
                df = load_table(path)
                col = time_col if time_col in df.columns else (_pick_column(df, ["date", "time", "timestamp"]) or time_col)
                if col not in df.columns:
                    continue
                df = df.copy()
                df["_time"] = pd.to_datetime(df[col], errors="coerce", utc=True)
                df = df.dropna(subset=["_time"]).add_prefix(f"t{i}_")
                df["_time"] = pd.to_datetime(df[f"t{i}__time"], errors="coerce", utc=True)
                frames.append(df)
            if not frames:
                return ok(tool_name, {"warning": "no joinable time columns found"})
            joined = frames[0]
            for frame in frames[1:]:
                joined = joined.merge(frame, on="_time", how=kwargs.get("how", "outer"))
            return ok(tool_name, {"rows": int(len(joined)), "columns": list(joined.columns), "sample": joined.head(10).to_dict(orient="records")})
        if tool_name == "export_intermediate_table":
            df = load_table(kwargs["path"])
            output_path = kwargs.get("output_path")
            if output_path:
                outp = safe_path(output_path)
                outp.parent.mkdir(parents=True, exist_ok=True)
                df.to_csv(outp, index=False)
                return ok(tool_name, {"rows": int(len(df)), "columns": list(df.columns), "output_path": str(outp)})
            return ok(tool_name, {"rows": int(len(df)), "columns": list(df.columns), "sample": df.head(10).to_dict(orient="records"), "warning": "no output_path provided; table not written"})
        if tool_name == "compute_time_window_stats":
            return ok(tool_name, time_window_stats(kwargs["path"], kwargs.get("time_col"), kwargs.get("value_cols"), kwargs.get("start"), kwargs.get("end"), kwargs.get("stats")))
        if tool_name == "compute_rolling_sum":
            return ok(tool_name, rolling_stat(kwargs["path"], kwargs.get("value_col"), kwargs.get("window", 3), "sum"))
        if tool_name == "compute_rolling_mean":
            return ok(tool_name, rolling_stat(kwargs["path"], kwargs.get("value_col"), kwargs.get("window", 3), "mean"))
        if tool_name == "detect_consecutive_exceedance":
            return ok(tool_name, consecutive_exceedance(kwargs["path"], kwargs.get("value_col"), float(kwargs.get("threshold", 0)), kwargs.get("op", ">=")))
        if tool_name == "compute_lagged_peak":
            import pandas as pd
            df = load_table(kwargs["path"])
            a_col = kwargs.get("driver_col") or kwargs.get("value_col") or _pick_column(df, ["precip", "rain", "frp", "wind", "temp"])
            b_col = kwargs.get("response_col") or _pick_column(df, ["pm25", "streamflow", "flood", "aqi", "impact"])
            if not a_col or not b_col:
                return ok(tool_name, {"warning": "driver_col and response_col are required or must be inferable", "columns": list(df.columns)})
            a = pd.to_numeric(df[a_col], errors="coerce")
            b = pd.to_numeric(df[b_col], errors="coerce")
            a_idx = int(a.idxmax()) if a.notna().any() else None
            b_idx = int(b.idxmax()) if b.notna().any() else None
            return ok(tool_name, {"driver_col": a_col, "response_col": b_col, "driver_peak_index": a_idx, "response_peak_index": b_idx, "lag_steps": None if a_idx is None or b_idx is None else b_idx - a_idx, "driver_peak": float(a.max()), "response_peak": float(b.max())})
        if tool_name == "compare_event_to_baseline_percentile":
            import pandas as pd
            df = load_table(kwargs["path"])
            col = kwargs.get("value_col") or _pick_column(df, ["precip", "rain", "temp", "pm25", "sst", "frp"])
            if not col:
                return ok(tool_name, {"warning": "numeric value column required", "columns": list(df.columns)})
            s = pd.to_numeric(df[col], errors="coerce").dropna()
            event_value = float(kwargs.get("event_value", s.max() if len(s) else 0))
            percentiles = {f"p{p}": float(s.quantile(p / 100.0)) for p in [50, 90, 95, 99]} if len(s) else {}
            return ok(tool_name, {"value_col": col, "event_value": event_value, "baseline_percentiles": percentiles, "exceeds_p90": event_value > percentiles.get("p90", math.inf), "exceeds_p95": event_value > percentiles.get("p95", math.inf), "exceeds_p99": event_value > percentiles.get("p99", math.inf)})
        if tool_name == "detect_event_peak_window":
            df = load_table(kwargs["path"])
            col = kwargs.get("value_col") or _pick_column(df, ["precip", "rain", "temp", "pm25", "sst", "frp"])
            if not col:
                return ok(tool_name, {"warning": "numeric value column required", "columns": list(df.columns)})
            s = numeric_series(df, col)
            window = int(kwargs.get("window", kwargs.get("window_size", 3)))
            roll = s.rolling(window, min_periods=min(window, len(s))).sum()
            idx = roll.idxmax() if len(roll.dropna()) else None
            return ok(tool_name, {"value_col": col, "window": window, "peak_index": int(idx) if isinstance(idx, int) else str(idx), "peak_window_value": float(roll.loc[idx]) if idx is not None else None})
        if tool_name == "compute_anomaly_from_climatology":
            s = _series_from_kwargs(kwargs, ["precip", "rain", "temp", "pm25", "sst", "frp"])
            if not len(s):
                return ok(tool_name, {"warning": "numeric event series required"})
            baseline_mean = float(kwargs.get("baseline_mean", s.mean()))
            baseline_std = float(kwargs.get("baseline_std", s.std() if len(s) > 1 else 0))
            event_value = float(kwargs.get("event_value", s.max()))
            anomaly = event_value - baseline_mean
            z = None if baseline_std == 0 else anomaly / baseline_std
            return ok(tool_name, {"event_value": event_value, "baseline_mean": baseline_mean, "baseline_std": baseline_std, "anomaly": anomaly, "z_score": z})
        if tool_name == "compute_percentile_rank":
            s = _series_from_kwargs(kwargs, ["precip", "rain", "temp", "pm25", "sst", "frp"])
            if not len(s):
                return ok(tool_name, {"warning": "numeric series required"})
            value = float(kwargs.get("value", kwargs.get("event_value", s.max())))
            rank = float((s <= value).sum() / len(s))
            return ok(tool_name, {"value": value, "percentile_rank": rank, "count": int(len(s))})
        if tool_name in {"load_vector_summary"}:
            return ok(tool_name, vector_summary(kwargs["path"]))
        if tool_name == "calculate_polygon_area":
            return ok(tool_name, polygon_area_metric(kwargs.get("polygon_path") or kwargs.get("path"), kwargs.get("class_filter")))
        if tool_name == "calculate_line_length_in_polygon":
            return ok(tool_name, line_length_in_polygon_metric(kwargs.get("line_path") or kwargs.get("path"), kwargs.get("polygon_path"), kwargs.get("class_filter")))
        if tool_name in {"count_points_in_polygon", "count_facilities_exposed"}:
            return ok(tool_name, count_points_or_facilities_metric(kwargs.get("points_path") or kwargs.get("facilities_vector") or kwargs.get("path"), kwargs.get("polygon_path") or kwargs.get("hazard_polygon"), kwargs.get("type_col")))
        if tool_name in {"compute_hospital_exposure_priority", "compute_school_exposure_priority", "compute_power_grid_exposure_proxy", "compute_port_airport_exposure", "compute_building_footprint_exposure", "compute_vulnerable_population_proxy"}:
            return ok(tool_name, count_points_or_facilities_metric(kwargs.get("points_path") or kwargs.get("facilities_vector") or kwargs.get("path"), kwargs.get("polygon_path") or kwargs.get("hazard_polygon"), kwargs.get("type_col")))
        if tool_name in {"compute_road_disruption_proxy", "compute_access_route_risk"}:
            return ok(tool_name, line_length_in_polygon_metric(kwargs.get("line_path") or kwargs.get("path"), kwargs.get("polygon_path") or kwargs.get("hazard_polygon"), kwargs.get("class_filter")))
        if tool_name == "reproject_vector":
            gdf = _read_vector(kwargs["path"])
            target_crs = kwargs.get("target_crs", "EPSG:6933")
            out_gdf = gdf.to_crs(target_crs) if gdf.crs else gdf
            return ok(tool_name, {"features": int(len(out_gdf)), "source_crs": str(gdf.crs), "target_crs": str(out_gdf.crs), "bbox": list(map(float, out_gdf.total_bounds)) if len(out_gdf) else None})
        if tool_name == "clip_vector_to_aoi":
            gdf = _read_vector(kwargs.get("vector_path") or kwargs["path"])
            aoi_path = kwargs.get("polygon_path") or kwargs.get("aoi")
            if not aoi_path:
                return ok(tool_name, {"features": int(len(gdf)), "warning": "no AOI provided; returned source summary", **vector_summary(kwargs.get("vector_path") or kwargs["path"])})
            aoi = _read_vector(aoi_path)
            if gdf.crs and aoi.crs and gdf.crs != aoi.crs:
                aoi = aoi.to_crs(gdf.crs)
            union = aoi.geometry.union_all() if hasattr(aoi.geometry, "union_all") else aoi.unary_union
            clipped = gdf[gdf.intersects(union)].copy()
            try:
                clipped["geometry"] = clipped.geometry.intersection(union)
            except Exception:
                pass
            return ok(tool_name, {"input_features": int(len(gdf)), "clipped_features": int(len(clipped)), "bbox": list(map(float, clipped.total_bounds)) if len(clipped) else None})
        if tool_name == "buffer_geometries":
            gdf = _read_vector(kwargs.get("vector_path") or kwargs["path"])
            distance_km = float(kwargs.get("distance_km", kwargs.get("distance", 1)))
            metric, warnings = _project_for_metric(gdf)
            buffered = metric.copy()
            buffered["geometry"] = metric.geometry.buffer(distance_km * 1000)
            return ok(tool_name, {"features": int(len(buffered)), "distance_km": distance_km, "buffer_area_km2": float(buffered.geometry.area.sum() / 1_000_000), "warnings": warnings})
        if tool_name == "intersect_vectors":
            a_path = kwargs.get("path_a") or kwargs.get("path")
            b_path = kwargs.get("path_b") or kwargs.get("polygon_path")
            if not a_path or not b_path:
                return ok(tool_name, {"warning": "path_a/path_b or path/polygon_path required"})
            a = _read_vector(a_path)
            b = _read_vector(b_path)
            if a.crs and b.crs and a.crs != b.crs:
                b = b.to_crs(a.crs)
            try:
                inter = a.overlay(b[["geometry"]], how="intersection")
            except Exception:
                union = b.geometry.union_all() if hasattr(b.geometry, "union_all") else b.unary_union
                inter = a[a.intersects(union)].copy()
                inter["geometry"] = inter.geometry.intersection(union)
            metric, warnings = _project_for_metric(inter)
            return ok(tool_name, {"features": int(len(inter)), "area_km2": float(metric.geometry.area.sum() / 1_000_000), "warnings": warnings})
        if tool_name == "union_hazard_footprints":
            import geopandas as gpd
            paths = kwargs.get("polygon_paths") or kwargs.get("paths") or ([kwargs["path"]] if "path" in kwargs else [])
            frames = [_read_vector(p) for p in paths]
            if not frames:
                return ok(tool_name, {"warning": "polygon_paths required"})
            base_crs = frames[0].crs
            frames = [f.to_crs(base_crs) if base_crs and f.crs and f.crs != base_crs else f for f in frames]
            merged = gpd.GeoDataFrame(geometry=[geom for f in frames for geom in f.geometry], crs=base_crs)
            union_geom = merged.geometry.union_all() if hasattr(merged.geometry, "union_all") else merged.unary_union
            union_gdf = gpd.GeoDataFrame(geometry=[union_geom], crs=base_crs)
            metric, warnings = _project_for_metric(union_gdf)
            return ok(tool_name, {"input_layers": len(paths), "area_km2": float(metric.geometry.area.sum() / 1_000_000), "warnings": warnings})
        if tool_name == "compute_hazard_aoi_overlap":
            hazard = kwargs.get("hazard_vector") or kwargs.get("path")
            aoi = kwargs.get("aoi_vector") or kwargs.get("polygon_path")
            if not hazard or not aoi:
                return ok(tool_name, {"warning": "hazard_vector and aoi_vector/polygon_path required"})
            h = _read_vector(hazard)
            a = _read_vector(aoi)
            if h.crs and a.crs and h.crs != a.crs:
                a = a.to_crs(h.crs)
            union = a.geometry.union_all() if hasattr(a.geometry, "union_all") else a.unary_union
            inter = h[h.intersects(union)].copy()
            inter["geometry"] = inter.geometry.intersection(union)
            h_metric, hw = _project_for_metric(h)
            i_metric, iw = _project_for_metric(inter)
            hazard_area = float(h_metric.geometry.area.sum() / 1_000_000)
            overlap_area = float(i_metric.geometry.area.sum() / 1_000_000)
            return ok(tool_name, {"hazard_area_km2": hazard_area, "overlap_area_km2": overlap_area, "overlap_ratio": None if hazard_area == 0 else overlap_area / hazard_area, "warnings": hw + iw})
        if tool_name == "compute_network_service_area":
            points = kwargs.get("facility_points") or kwargs.get("points_path") or kwargs.get("path")
            if not points:
                return ok(tool_name, {"warning": "facility points required"})
            gdf = _read_vector(points)
            distance_km = float(kwargs.get("distance_km", kwargs.get("distance", 5)))
            metric, warnings = _project_for_metric(gdf)
            buffers = metric.geometry.buffer(distance_km * 1000)
            return ok(tool_name, {"facility_count": int(len(gdf)), "distance_km": distance_km, "service_area_km2": float(buffers.area.sum() / 1_000_000), "warnings": warnings})
        if tool_name == "make_overview_map":
            layers = kwargs.get("layers") or ([kwargs["path"]] if "path" in kwargs else [])
            summaries = []
            for layer in layers:
                try:
                    summaries.append(vector_summary(layer))
                except Exception as e:
                    summaries.append({"path": str(layer), "error": str(e)})
            return ok(tool_name, {"layer_summaries": summaries, "output_path": kwargs.get("output_path")})
        if tool_name in {"reproject_vector", "clip_vector_to_aoi", "buffer_geometries", "intersect_vectors", "union_hazard_footprints", "count_points_in_polygon", "calculate_line_length_in_polygon", "calculate_polygon_area", "estimate_population_exposure", "count_facilities_exposed", "compute_distance_to_track_or_epicenter", "spatial_join_exposure_attributes", "estimate_admin_unit_exposure", "compute_network_service_area", "compute_hazard_aoi_overlap", "make_overview_map"}:
            if "path" in kwargs:
                return ok(tool_name, vector_summary(kwargs["path"]))
            return ok(tool_name, {"message": "vector operation placeholder executed; provide path-specific arguments for full calculation", "input_keys": sorted(kwargs.keys())}, warnings=["operation uses generic vector fallback"])
        if tool_name == "load_raster_summary":
            return ok(tool_name, raster_summary(kwargs["path"]))
        if tool_name in {"compute_zonal_raster_stats", "compute_raster_histogram", "extract_raster_timeseries"}:
            return ok(tool_name, raster_stats(kwargs["path"], kwargs.get("band", 1)))
        if tool_name == "compute_raster_threshold_area":
            return ok(tool_name, threshold_area(kwargs["path"], float(kwargs.get("threshold", 0)), kwargs.get("op", ">"), kwargs.get("band", 1)))
        if tool_name == "compare_pre_post_rasters":
            return ok(tool_name, raster_difference_metric(kwargs.get("pre_path") or kwargs.get("path_a"), kwargs.get("post_path") or kwargs.get("path_b"), kwargs.get("threshold"), kwargs.get("op", "abs_gt"), kwargs.get("band", 1)))
        if tool_name in {"compute_ndvi", "compute_ndwi", "compute_nbr"} and ("path_a" in kwargs or "nir_band" in kwargs):
            a = kwargs.get("nir_band") or kwargs.get("green_band") or kwargs.get("path_a")
            b = kwargs.get("red_band") or kwargs.get("swir_band") or kwargs.get("nir_or_swir_band") or kwargs.get("path_b")
            return ok(tool_name, normalized_difference_metric(a, b, tool_name.replace("compute_", "").upper(), kwargs.get("band_a", 1), kwargs.get("band_b", 1)))
        if tool_name == "compute_valid_pixel_fraction":
            import rasterio
            p = safe_path(kwargs["path"])
            band = int(kwargs.get("band", 1))
            with rasterio.open(p) as src:
                arr = src.read(band, masked=True)
                total = arr.size
                valid = int(arr.count())
                nodata = int(total - valid)
                return ok(tool_name, {"path": str(p), "band": band, "total_pixels": int(total), "valid_pixels": valid, "nodata_or_masked_pixels": nodata, "valid_fraction": None if total == 0 else valid / total, "nodata_value": src.nodata})
        if tool_name == "sample_raster_at_points":
            import geopandas as gpd
            import rasterio
            raster_path = safe_path(kwargs["path"])
            points_path = kwargs.get("points_path")
            if not points_path:
                return ok(tool_name, {"warning": "points_path required"})
            pts = gpd.read_file(safe_path(points_path))
            with rasterio.open(raster_path) as src:
                if pts.crs and src.crs and pts.crs != src.crs:
                    pts = pts.to_crs(src.crs)
                coords = [(geom.x, geom.y) for geom in pts.geometry if geom.geom_type == "Point"]
                vals = [float(v[0]) for v in src.sample(coords)]
            return ok(tool_name, {"sample_count": len(vals), "values": vals[:100], "min": min(vals) if vals else None, "max": max(vals) if vals else None, "mean": statistics.fmean(vals) if vals else None})
        if tool_name == "compute_lst_summary":
            return ok(tool_name, {"lst_stats": raster_stats(kwargs["path"], kwargs.get("band", 1)), "unit": kwargs.get("unit", "unknown")})
        if tool_name == "export_raster_thumbnail":
            summary = raster_summary(kwargs["path"])
            return ok(tool_name, {"thumbnail_ready": True, "raster_summary": summary, "output_path": kwargs.get("output_path")})
        if tool_name in {"reproject_raster", "clip_raster_to_aoi", "compare_pre_post_rasters", "compute_ndvi", "compute_ndwi", "compute_nbr", "compute_lst_summary", "mask_clouds_from_quality_band", "mosaic_rasters", "sample_raster_at_points", "align_raster_grids", "compute_valid_pixel_fraction", "export_raster_thumbnail"}:
            if "path" in kwargs:
                return ok(tool_name, raster_summary(kwargs["path"]))
            return ok(tool_name, {"message": "raster operation requires concrete raster paths", "input_keys": sorted(kwargs.keys())}, warnings=["operation uses generic raster fallback"])
        if tool_name == "read_image_rgb_summary":
            return ok(tool_name, rich_image_summary(kwargs["path"]))
        if tool_name == "summarize_image_rgb_statistics":
            summary = rich_image_summary(kwargs["path"])
            summary["channel_spread"] = float(max(summary["mean_rgb"]) - min(summary["mean_rgb"]))
            summary["contrast_proxy"] = float(statistics.fmean(summary["stddev_rgb"])) if summary.get("stddev_rgb") else None
            return ok(tool_name, summary)
        if tool_name == "compare_image_rgb_summaries":
            pre = rich_image_summary(kwargs.get("pre_image") or kwargs.get("pre_path") or kwargs.get("path"))
            post = rich_image_summary(kwargs.get("post_image") or kwargs.get("post_path") or kwargs.get("path"))
            diff = [post["mean_rgb"][i] - pre["mean_rgb"][i] for i in range(3)]
            return ok(tool_name, {"pre": pre, "post": post, "mean_rgb_change": diff, "mean_abs_rgb_change": statistics.fmean(abs(x) for x in diff)})
        if tool_name == "estimate_image_flood_proxy":
            proxy = image_proxy_scores(kwargs.get("image_path") or kwargs.get("path"))
            return ok(tool_name, {"image_summary": proxy["summary"], "proxy_score": proxy["scores"]["flood_proxy"], "proxy_method": "simple blue/green RGB dominance", "cues": proxy["cues"], "caveat": "heuristic RGB proxy, not semantic flood detection"})
        if tool_name == "estimate_image_burn_proxy":
            proxy = image_proxy_scores(kwargs.get("image_path") or kwargs.get("path"))
            return ok(tool_name, {"image_summary": proxy["summary"], "proxy_score": proxy["scores"]["burn_proxy"], "proxy_method": "simple red-dark RGB dominance", "cues": proxy["cues"], "caveat": "heuristic RGB proxy, not semantic burn-scar detection"})
        if tool_name == "estimate_image_obscuration_proxy":
            proxy = image_proxy_scores(kwargs.get("image_path") or kwargs.get("path"))
            return ok(tool_name, {"image_summary": proxy["summary"], "proxy_score": proxy["scores"]["obscuration_proxy"], "haze_score": proxy["scores"]["haze_proxy"], "proxy_method": "brightness and channel-balance heuristic", "cues": proxy["cues"], "caveat": "heuristic RGB proxy, not semantic cloud/smoke detection"})
        if tool_name == "read_image_georeference":
            return ok(tool_name, image_georeference_summary(kwargs["path"]))
        if tool_name == "read_alphaearth_embedding_stats":
            stats_path = kwargs.get("stats_path") or kwargs.get("path")
            return ok(tool_name, alphaearth_stats_summary(stats_path))
        if tool_name == "compare_alphaearth_embedding_stats":
            pre_path = kwargs.get("pre_stats_path") or kwargs.get("pre_path") or kwargs.get("path")
            post_path = kwargs.get("post_stats_path") or kwargs.get("post_path") or kwargs.get("path")
            return ok(tool_name, compare_alphaearth_stats(pre_path, post_path))
        if tool_name == "read_image_file_metadata":
            return ok(tool_name, image_file_metadata(kwargs["path"]))
        if tool_name == "compare_image_proxy_to_hazard_signature":
            path = kwargs.get("image_path") or kwargs.get("path")
            hazard_type = str(kwargs.get("hazard_type", "")).lower()
            proxy = image_proxy_scores(path)
            template_map = {
                "flood": "flood_proxy",
                "precip": "flood_proxy",
                "water": "flood_proxy",
                "wildfire": "burn_proxy",
                "fire": "burn_proxy",
                "burn": "burn_proxy",
                "smoke": "obscuration_proxy",
                "dust": "haze_proxy",
                "ash": "obscuration_proxy",
                "cloud": "obscuration_proxy",
                "snow": "obscuration_proxy",
            }
            matched_key = next((v for k, v in template_map.items() if k in hazard_type), None)
            return ok(tool_name, {
                "image_summary": proxy["summary"],
                "hazard_type": hazard_type,
                "proxy_scores": proxy["scores"],
                "cues": proxy["cues"],
                "expected_proxy": matched_key,
                "match_score": proxy["scores"].get(matched_key) if matched_key else None,
                "caveat": "heuristic proxy comparison, not object detection or semantic classification",
            })
        if tool_name == "build_image_change_summary":
            pre_path = kwargs.get("pre_image") or kwargs.get("pre_path") or kwargs.get("path")
            post_path = kwargs.get("post_image") or kwargs.get("post_path") or kwargs.get("path")
            pre = rich_image_summary(pre_path)
            post = rich_image_summary(post_path)
            change = [post["mean_rgb"][i] - pre["mean_rgb"][i] for i in range(3)]
            output = {
                "pre": pre,
                "post": post,
                "mean_rgb_change": change,
                "mean_abs_rgb_change": statistics.fmean(abs(x) for x in change),
                "eo_metrics": kwargs.get("eo_metrics", {}),
            }
            change_stats_path = kwargs.get("alphaearth_change_stats_path") or kwargs.get("alphaearth_change_path")
            if change_stats_path:
                output["alphaearth_change"] = alphaearth_stats_summary(change_stats_path)
            return ok(tool_name, output)
        if tool_name == "compute_heat_index":
            return ok(tool_name, {"heat_index_c": heat_index_c(float(kwargs["temp_c"]), float(kwargs["rh"]))})
        if tool_name == "compute_wet_bulb_temperature":
            return ok(tool_name, {"wet_bulb_c": wet_bulb_stull_c(float(kwargs["temp_c"]), float(kwargs["rh"]))})
        if tool_name == "compute_precip_accumulation":
            return ok(tool_name, precip_accumulation_metric(kwargs))
        if tool_name == "compute_precip_intensity_duration":
            return ok(tool_name, intensity_duration_metric(kwargs))
        if tool_name == "compute_heatwave_duration_intensity":
            return ok(tool_name, heatwave_metric(kwargs))
        if tool_name == "compute_cold_spell_metrics":
            return ok(tool_name, cold_spell_metric(kwargs))
        if tool_name == "compute_hot_dry_vpd_metrics":
            return ok(tool_name, hot_dry_vpd_metric(kwargs))
        if tool_name == "compute_urban_pluvial_diagnostics":
            return ok(tool_name, urban_pluvial_diagnostics_metric(kwargs))
        if tool_name == "compute_warm_night_count":
            return ok(tool_name, warm_night_metric(kwargs))
        if tool_name == "compute_apparent_temperature_stats":
            return ok(tool_name, apparent_temperature_metric(kwargs))
        if tool_name == "compute_flood_impact_metrics":
            return ok(tool_name, flood_impact_metric(kwargs))
        if tool_name == "compute_air_quality_exceedance":
            return ok(tool_name, air_quality_metric(kwargs))
        if tool_name == "compute_fire_hotspot_metrics":
            return ok(tool_name, fire_hotspot_metric(kwargs))
        if tool_name == "compute_earthquake_sequence_metrics":
            return ok(tool_name, earthquake_sequence_metric(kwargs))
        if tool_name == "compute_enso_phase_metrics":
            return ok(tool_name, enso_phase_metric(kwargs))
        if tool_name == "compute_streamflow_anomaly":
            return ok(tool_name, streamflow_anomaly_metric(kwargs))
        if tool_name == "compute_spei_spi":
            return ok(tool_name, spei_spi_metric(kwargs))
        if tool_name == "compute_soil_moisture_percentile":
            return ok(tool_name, soil_moisture_percentile_metric(kwargs))
        if tool_name == "compute_cyclone_track_metrics":
            return ok(tool_name, cyclone_track_metric(kwargs))
        if tool_name == "compute_storm_surge_proxy":
            return ok(tool_name, storm_surge_proxy_metric(kwargs))
        if tool_name == "compute_wind_exposure_metrics":
            return ok(tool_name, wind_exposure_metric(kwargs))
        if tool_name == "compute_teleconnection_lag_correlation":
            return ok(tool_name, teleconnection_lag_correlation_metric(kwargs))
        if tool_name == "compute_snow_ice_anomaly":
            return ok(tool_name, snow_ice_anomaly_metric(kwargs))
        if tool_name in {"compute_marine_heatwave_metrics", "compute_coral_bleaching_alert", "compute_ocean_heat_content_proxy"}:
            return ok(tool_name, marine_heatwave_metric(kwargs))
        if tool_name == "estimate_runoff_proxy":
            return ok(tool_name, runoff_proxy_metric(kwargs))
        if tool_name == "compute_burned_area_metrics":
            return ok(tool_name, burned_area_metric(kwargs))
        if tool_name == "compute_fire_weather_index_proxy":
            return ok(tool_name, fire_weather_index_proxy_metric(kwargs))
        if tool_name == "compute_smoke_pm_lag_metrics":
            return ok(tool_name, smoke_pm_lag_metric(kwargs))
        if tool_name == "compute_shakemap_exposure":
            return ok(tool_name, shakemap_exposure_metric(kwargs))
        if tool_name == "compute_landslide_trigger_index":
            return ok(tool_name, landslide_trigger_metric(kwargs))
        if tool_name == "compute_volcano_ash_extent":
            return ok(tool_name, volcano_ash_extent_metric(kwargs))
        if tool_name == "compute_so2_anomaly":
            return ok(tool_name, so2_anomaly_metric(kwargs))
        if tool_name == "compute_tsunami_coastal_exposure":
            return ok(tool_name, tsunami_coastal_exposure_metric(kwargs))
        if tool_name == "compute_dust_storm_metrics":
            return ok(tool_name, dust_storm_metric(kwargs))
        if tool_name == "compute_tide_surge_compound_index":
            return ok(tool_name, tide_surge_compound_metric(kwargs))
        if tool_name == "compute_multihazard_overlap_score":
            return ok(tool_name, multihazard_overlap_metric(kwargs))
        if tool_name == "interpolate_station_pollution":
            return ok(tool_name, station_interpolation_metric(kwargs))
        if tool_name == "estimate_ground_failure_susceptibility":
            return ok(tool_name, ground_failure_metric(kwargs))
        if tool_name == "rank_admin_units_by_response_need":
            return ok(tool_name, admin_ranking_metric(kwargs))
        if tool_name == "summarize_311_complaints":
            if "path" in kwargs:
                return ok(tool_name, time_window_stats(kwargs["path"], kwargs.get("time_col"), kwargs.get("value_cols")))
            return ok(tool_name, {"message": "provide 311 complaint table path for grouped complaint metrics"})
        if tool_name.startswith("compute_"):
            if "path" in kwargs:
                return ok(tool_name, simple_series_metric(kwargs["path"], kwargs.get("value_col")))
            return ok(tool_name, {"message": "metric tool executed with scalar/metadata inputs", "input_keys": sorted(kwargs.keys())})
        reasoning_tools = {
            "plan_evidence_collection",
            "select_minimal_tool_subset",
            "route_to_hazard_workflow",
            "build_hazard_metric_matrix",
            "synthesize_multisource_evidence",
            "rank_response_priorities",
            "assemble_structured_answer_fields",
            "summarize_key_findings_table",
            "build_decision_brief_sections",
            "compute_weighted_hazard_score",
            "merge_tool_outputs_by_time",
            "normalize_answer_units_and_fields",
            "infer_task_reasoning_axes",
            "build_mechanism_competition_table",
            "reconstruct_event_process_stages",
            "evaluate_physical_consistency",
            "synthesize_compound_hazard_chain",
            "compare_visual_numeric_evidence",
            "calibrate_event_severity_profile",
            "derive_response_priority_rationale",
            "test_option_hypothesis_consistency",
            "extract_required_computation_targets",
            "map_task_to_required_tools",
            "build_metric_dependency_graph",
            "reconcile_point_grid_regional_scale",
            "parse_mcq_options_and_select",
        }
        if tool_name in reasoning_tools:
            question = str(kwargs.get("question") or kwargs.get("task_text") or "")
            text = " ".join(str(kwargs.get(key, "")) for key in ("question", "task_text", "proposed_answer", "answer", "content"))
            axis_patterns = {
                "mechanism": r"mechanism|driver|forcing|trigger|pathway|causal|physical",
                "severity": r"severity|intensity|peak|duration|anomaly|percentile|threshold|return",
                "visual_numeric": r"image|visual|satellite|remote|NDVI|NDWI|NBR|embedding|true[- ]?color",
                "impact_chain": r"impact|exposure|population|road|facility|infrastructure|cascade|health",
                "response_priority": r"response|priority|rescue|warning|evacuation|operational",
                "physical_consistency": r"consistent|formula|process|stage|scale|timing|contradict",
            }
            axes = [name for name, pat in axis_patterns.items() if re.search(pat, text, re.I)]
            if tool_name == "plan_evidence_collection":
                manifest = kwargs.get("manifest") or kwargs.get("file_manifest") or []
                targets = required_computation_targets_metric(question).get("targets", [])
                target_names = [t["target"] for t in targets]
                plan = [{"step": 1, "action": "inspect_manifest", "recommended_tools": ["list_event_package_files", "select_candidate_files_for_question"]}]
                if any("precipitation" in t for t in target_names):
                    plan.append({"step": len(plan) + 1, "action": "compute_precipitation_metrics", "recommended_tools": ["compute_precip_accumulation", "compute_rolling_sum"]})
                if any("temperature" in t for t in target_names):
                    plan.append({"step": len(plan) + 1, "action": "compute_heat_stress_metrics", "recommended_tools": ["compute_heatwave_duration_intensity", "compute_heat_index", "compute_wet_bulb_temperature"]})
                if any("flood" in t for t in target_names):
                    plan.append({"step": len(plan) + 1, "action": "compute_flood_extent_and_exposure", "recommended_tools": ["compute_raster_threshold_area", "estimate_population_exposure", "calculate_line_length_in_polygon"]})
                if any("visual" in t for t in target_names):
                    plan.append({"step": len(plan) + 1, "action": "interpret_visual_context", "recommended_tools": ["read_image_rgb_summary", "compare_image_proxy_to_hazard_signature", "compare_visual_numeric_evidence"]})
                plan.append({"step": len(plan) + 1, "action": "assemble_reasoning_outputs", "recommended_tools": ["build_hazard_metric_matrix", "summarize_key_findings_table"]})
                return ok(tool_name, {"targets": targets, "manifest_file_count": len(manifest), "ordered_plan": plan})
            if tool_name == "select_minimal_tool_subset":
                targets = required_computation_targets_metric(question).get("targets", [])
                target_names = [t["target"] for t in targets]
                selected = ["list_event_package_files", "read_event_metadata", "read_text_or_html", "summarize_table_or_json"]
                mapping = dispatch("map_task_to_required_tools", computation_targets=target_names)["data"].get("tool_map", {})
                for tools in mapping.values():
                    for t in tools:
                        if t not in selected:
                            selected.append(t)
                if not target_names:
                    selected.extend(["compute_time_window_stats", "summarize_key_findings_table"])
                return ok(tool_name, {"selected_tools": selected, "target_count": len(target_names)})
            if tool_name == "route_to_hazard_workflow":
                q = question.lower() + " " + json.dumps(kwargs.get("metadata", {}), ensure_ascii=False).lower()
                workflow_rules = [
                    ("flood_hazard_impact_chain", r"flood|inundat|rain|precip|river"),
                    ("heat_health_persistence", r"heat|tmax|temperature|wet[- ]?bulb|apparent"),
                    ("wildfire_smoke_health", r"wildfire|fire|burn|smoke|frp|pm2"),
                    ("cyclone_compound_wind_rain_surge", r"cyclone|hurricane|typhoon|surge|wind"),
                    ("earthquake_lifeline_response", r"earthquake|shakemap|magnitude|pga|mmi"),
                    ("enso_teleconnection", r"enso|nino|oni|teleconnection"),
                    ("marine_heatwave_coral", r"marine|sst|coral|bleach|ocean"),
                    ("remote_sensing_change_diagnosis", r"image|satellite|ndvi|ndwi|nbr|embedding"),
                    ("urban_feedback_infrastructure", r"urban|311|road|hospital|infrastructure|facility"),
                ]
                matches = [{"workflow": name, "matched": re.findall(pat, q, re.I)} for name, pat in workflow_rules if re.search(pat, q, re.I)]
                workflow = matches[0]["workflow"] if matches else "general_extreme_event_reasoning"
                return ok(tool_name, {"workflow": workflow, "matches": matches})
            if tool_name == "infer_task_reasoning_axes":
                return ok(tool_name, {"axes": axes, "recommended_profile": "core_deep_54" if axes else "minimum_real_17", "input_keys": sorted(kwargs.keys())})
            if tool_name == "build_hazard_metric_matrix":
                metric_groups = kwargs.get("metric_groups") or kwargs.get("metrics") or {}
                rows = []
                if isinstance(metric_groups, dict):
                    for group, metrics in metric_groups.items():
                        if isinstance(metrics, dict):
                            for metric, value in metrics.items():
                                rows.append({"group": group, "metric": metric, "value": value})
                        else:
                            rows.append({"group": group, "metric": "value", "value": metrics})
                return ok(tool_name, {"rows": rows, "dimensions": kwargs.get("dimensions", [])})
            if tool_name == "build_mechanism_competition_table":
                candidates = kwargs.get("candidate_mechanisms") or kwargs.get("options") or []
                rows = [{"candidate": c, "support": [], "contradictions": [], "secondary_or_contextual": [], "decision_note": "requires evidence synthesis"} for c in candidates]
                return ok(tool_name, {"candidates": rows, "axes": axes})
            if tool_name == "reconstruct_event_process_stages":
                stages = ["precursor_or_forcing", "hazard_intensification", "peak_or_failure", "exposure_interaction", "impact_or_response"]
                return ok(tool_name, {"stages": [{"stage": s, "evidence": [], "metrics": []} for s in stages], "input_keys": sorted(kwargs.keys())})
            if tool_name == "evaluate_physical_consistency":
                metrics = kwargs.get("metrics") or {}
                rules = kwargs.get("mechanism_rules") or {}
                failure_modes = []
                checks = []
                if isinstance(metrics, dict):
                    for key, value in metrics.items():
                        if isinstance(value, (int, float)):
                            checks.append({"metric": key, "value": value, "finite": math.isfinite(float(value))})
                            if not math.isfinite(float(value)):
                                failure_modes.append(f"{key} is non-finite")
                if isinstance(rules, dict):
                    for key, rule in rules.items():
                        if key in metrics and isinstance(metrics[key], (int, float)) and isinstance(rule, dict):
                            min_v = rule.get("min")
                            max_v = rule.get("max")
                            if min_v is not None and float(metrics[key]) < float(min_v):
                                failure_modes.append(f"{key} below expected minimum")
                            if max_v is not None and float(metrics[key]) > float(max_v):
                                failure_modes.append(f"{key} above expected maximum")
                verdict = "physically_consistent_given_inputs" if not failure_modes else "physical_consistency_flags_present"
                return ok(tool_name, {"verdict": verdict, "axes_checked": axes or ["mechanism", "scale", "timing"], "checks": checks, "failure_modes": failure_modes})
            if tool_name == "synthesize_compound_hazard_chain":
                return ok(tool_name, {
                    "drivers": kwargs.get("drivers", []),
                    "hazard_components": kwargs.get("hazard_components", []),
                    "exposure_metrics": kwargs.get("exposure_metrics", {}),
                    "impact_claims": kwargs.get("impact_claims", []),
                    "chain": ["driver", "hazard", "exposure", "impact"],
                })
            if tool_name == "compare_visual_numeric_evidence":
                image_summaries = kwargs.get("image_summaries") or []
                numeric_metrics = kwargs.get("numeric_metrics") or kwargs.get("metrics") or {}
                visual_text = json.dumps(image_summaries, ensure_ascii=False).lower()
                metric_text = json.dumps(numeric_metrics, ensure_ascii=False).lower()
                hazard_signatures = {
                    "flood_or_inundation": (["water", "flood", "inundat", "ndwi"], ["flood", "water", "ndwi", "inundat"]),
                    "burn_or_wildfire": (["burn", "scar", "smoke", "fire"], ["nbr", "burn", "frp", "hotspot", "pm25", "smoke"]),
                    "dust_smoke_or_ash": (["smoke", "dust", "ash", "haze"], ["pm", "aod", "so2", "ash", "dust"]),
                    "snow_ice_or_cold": (["snow", "ice", "white"], ["snow", "ice", "cold", "tmin"]),
                    "urban_heat": (["urban", "built", "dry"], ["heat", "tmax", "lst", "temperature", "wet_bulb"]),
                }
                linked = []
                for label, (visual_terms, metric_terms) in hazard_signatures.items():
                    visual_hit = [term for term in visual_terms if term in visual_text]
                    metric_hit = [term for term in metric_terms if term in metric_text]
                    if visual_hit or metric_hit:
                        linked.append({
                            "hazard_signature": label,
                            "visual_terms": visual_hit,
                            "metric_terms": metric_hit,
                            "joint_support": bool(visual_hit and metric_hit),
                        })
                if image_summaries and numeric_metrics:
                    consistency = "paired_visual_numeric_inputs_available"
                elif image_summaries:
                    consistency = "visual_only_input"
                elif numeric_metrics:
                    consistency = "numeric_only_input"
                else:
                    consistency = "missing_visual_and_numeric_inputs"
                return ok(tool_name, {
                    "visual_classes": image_summaries,
                    "numeric_anchors": numeric_metrics,
                    "linked_interpretations": linked,
                    "consistency": consistency,
                })
            if tool_name == "calibrate_event_severity_profile":
                metrics = kwargs.get("hazard_metrics") or kwargs.get("metrics") or {}
                thresholds = kwargs.get("thresholds") or {}
                score = 0
                components = []
                if isinstance(metrics, dict):
                    for key, value in metrics.items():
                        if not isinstance(value, (int, float)):
                            continue
                        rule = thresholds.get(key) if isinstance(thresholds, dict) else None
                        if isinstance(rule, dict):
                            moderate = float(rule.get("moderate", math.inf))
                            severe = float(rule.get("severe", math.inf))
                            extreme = float(rule.get("extreme", math.inf))
                        else:
                            # Generic fallback thresholds are intentionally conservative and only
                            # turn positive numeric indicators into a coarse severity score.
                            moderate, severe, extreme = 1.0, 3.0, 5.0
                        level = 0
                        if float(value) >= extreme:
                            level = 3
                        elif float(value) >= severe:
                            level = 2
                        elif float(value) >= moderate:
                            level = 1
                        score += level
                        components.append({"metric": key, "value": value, "level": level})
                if score >= 6:
                    label = "extreme_or_high_impact_candidate"
                elif score >= 3:
                    label = "severe_candidate"
                elif score >= 1:
                    label = "moderate_candidate"
                else:
                    label = "low_or_unclassified"
                return ok(tool_name, {"severity_label": kwargs.get("severity_label", label), "score": score, "components": components, "metrics": metrics, "thresholds": thresholds})
            if tool_name == "derive_response_priority_rationale":
                candidates = kwargs.get("candidate_actions") or kwargs.get("items") or []
                metrics = kwargs.get("metrics") or {}
                ranked = sorted(candidates, key=lambda x: metrics.get(x, 0) if isinstance(metrics, dict) else 0, reverse=True)
                return ok(tool_name, {"ranked_actions": ranked, "rationale_axes": axes or ["hazard_timing", "exposed_systems", "accessibility"]})
            if tool_name == "synthesize_multisource_evidence":
                evidence_objects = kwargs.get("evidence_objects") or kwargs.get("evidence") or []
                groups: dict[str, list[Any]] = {}
                for item in evidence_objects if isinstance(evidence_objects, list) else [evidence_objects]:
                    key = "unknown"
                    blob = json.dumps(item, ensure_ascii=False).lower()
                    if any(tok in blob for tok in ["precip", "rain", "temp", "wind", "sst", "pm25"]):
                        key = "physical_hazard"
                    elif any(tok in blob for tok in ["image", "raster", "ndvi", "ndwi", "nbr", "satellite"]):
                        key = "remote_sensing"
                    elif any(tok in blob for tok in ["population", "road", "facility", "hospital", "school"]):
                        key = "exposure"
                    elif any(tok in blob for tok in ["death", "damage", "evac", "affected", "report"]):
                        key = "report_impact"
                    groups.setdefault(key, []).append(item)
                return ok(tool_name, {"groups": {k: len(v) for k, v in groups.items()}, "synthesis_rows": [{"source_group": k, "item_count": len(v)} for k, v in groups.items()]})
            if tool_name == "rank_response_priorities":
                items = kwargs.get("items") or []
                metrics = kwargs.get("metrics") or {}
                weights = kwargs.get("weights") or {}
                rows = []
                for item in items:
                    if isinstance(metrics, dict) and isinstance(metrics.get(item), (int, float)):
                        score = float(metrics[item])
                    elif isinstance(item, dict):
                        score = 0.0
                        for key, value in item.items():
                            if isinstance(value, (int, float)):
                                score += float(value) * float(weights.get(key, 1.0)) if isinstance(weights, dict) else float(value)
                    else:
                        score = 0.0
                    rows.append({"item": item, "priority_score": score})
                return ok(tool_name, {"ranked": sorted(rows, key=lambda r: r["priority_score"], reverse=True)})
            if tool_name == "test_option_hypothesis_consistency":
                options = kwargs.get("options") or {}
                metrics = kwargs.get("metrics") or {}
                option_iter = options.items() if isinstance(options, dict) else enumerate(options)
                rows = []
                for k, v in option_iter:
                    text_v = str(v)
                    nums = [float(x.replace(",", "")) for x in re.findall(r"[-+]?\d+(?:,\d{3})*(?:\.\d+)?", text_v)]
                    flags = []
                    if isinstance(metrics, dict):
                        for metric_name, metric_value in metrics.items():
                            if isinstance(metric_value, (int, float)) and nums:
                                nearest = min(nums, key=lambda x: abs(x - float(metric_value)))
                                rel_err = abs(nearest - float(metric_value)) / (abs(float(metric_value)) + 1e-9)
                                if rel_err <= 0.05:
                                    flags.append({"metric": metric_name, "matched_number": nearest, "relative_error": rel_err})
                    rows.append({"option": k, "text": text_v, "numbers_in_option": nums, "metric_matches": flags, "match_count": len(flags)})
                return ok(tool_name, {"options": rows, "metrics_checked": list(metrics) if isinstance(metrics, dict) else []})
            if tool_name == "extract_required_computation_targets":
                return ok(tool_name, required_computation_targets_metric(question, kwargs.get("metadata")))
            if tool_name == "map_task_to_required_tools":
                targets = kwargs.get("computation_targets") or kwargs.get("targets") or []
                tool_map = {
                    "precipitation": ["compute_precip_accumulation", "compute_rolling_sum", "compare_event_to_baseline_percentile"],
                    "temperature": ["compute_heatwave_duration_intensity", "compute_heat_index", "compute_wet_bulb_temperature"],
                    "flood_area": ["compare_pre_post_rasters", "compute_raster_threshold_area", "estimate_population_exposure"],
                    "fire_burn": ["compute_fire_hotspot_metrics", "compute_nbr", "compute_burned_area_metrics"],
                    "exposure": ["estimate_population_exposure", "calculate_line_length_in_polygon", "count_facilities_exposed"],
                    "ocean": ["compute_marine_heatwave_metrics", "compute_coral_bleaching_alert"],
                }
                return ok(tool_name, {"tool_map": {t: tool_map.get(t, []) for t in targets}})
            if tool_name == "build_metric_dependency_graph":
                files = kwargs.get("input_files") or []
                computations = kwargs.get("computations") or []
                final_fields = kwargs.get("final_fields") or []
                nodes = [{"id": f"file:{f}", "type": "file"} for f in files]
                nodes += [{"id": f"metric:{c}", "type": "metric"} for c in computations]
                nodes += [{"id": f"answer:{f}", "type": "answer_field"} for f in final_fields]
                edges = []
                for f in files:
                    for c in computations:
                        edges.append({"source": f"file:{f}", "target": f"metric:{c}"})
                for c in computations:
                    for f in final_fields:
                        edges.append({"source": f"metric:{c}", "target": f"answer:{f}"})
                return ok(tool_name, {"nodes": nodes, "edges": edges})
            if tool_name == "assemble_structured_answer_fields":
                fields = kwargs.get("fields") or {}
                metrics = kwargs.get("metrics") or {}
                labels = kwargs.get("labels") or {}
                selected = kwargs.get("selected_option")
                return ok(tool_name, {"fields": fields, "metrics": metrics, "labels": labels, "selected_option": selected})
            if tool_name == "summarize_key_findings_table":
                findings = kwargs.get("findings") or kwargs.get("metrics") or {}
                rows = []
                if isinstance(findings, dict):
                    rows = [{"metric": k, "value": v, "unit": None, "interpretation": None} for k, v in findings.items()]
                elif isinstance(findings, list):
                    rows = findings
                return ok(tool_name, {"findings": rows})
            if tool_name == "build_decision_brief_sections":
                return ok(tool_name, {
                    "hazard_diagnosis": kwargs.get("hazard_findings", {}),
                    "mechanism": kwargs.get("mechanism_findings", {}),
                    "impact_chain": kwargs.get("impact_findings", {}),
                    "action_priority": kwargs.get("action_findings", {}),
                })
            if tool_name == "compute_weighted_hazard_score":
                metrics = kwargs.get("metrics") or {}
                weights = kwargs.get("weights") or {}
                score = 0.0
                parts = []
                if isinstance(metrics, dict):
                    for key, value in metrics.items():
                        if isinstance(value, (int, float)):
                            w = float(weights.get(key, 1.0)) if isinstance(weights, dict) else 1.0
                            score += float(value) * w
                            parts.append({"metric": key, "value": value, "weight": w, "contribution": float(value) * w})
                return ok(tool_name, {"score": score, "parts": parts})
            if tool_name == "merge_tool_outputs_by_time":
                outputs = kwargs.get("tool_outputs") or []
                time_key = kwargs.get("time_key", "time")
                rows = []
                for out_item in outputs:
                    data = out_item.get("data", out_item) if isinstance(out_item, dict) else out_item
                    if isinstance(data, list):
                        rows.extend(data)
                    elif isinstance(data, dict):
                        rows.append(data)
                rows = sorted(rows, key=lambda r: str(r.get(time_key, "")) if isinstance(r, dict) else "")
                return ok(tool_name, {"rows": rows, "time_key": time_key})
            if tool_name == "normalize_answer_units_and_fields":
                fields = kwargs.get("answer_fields") or kwargs.get("fields") or {}
                aliases = kwargs.get("field_aliases") or {}
                unit_map = kwargs.get("unit_map") or {}
                normalized = {}
                if isinstance(fields, dict):
                    for key, value in fields.items():
                        out_key = aliases.get(key, key) if isinstance(aliases, dict) else key
                        normalized[out_key] = {"value": value, "unit": unit_map.get(out_key) if isinstance(unit_map, dict) else None}
                return ok(tool_name, {"fields": normalized})
            if tool_name == "reconcile_point_grid_regional_scale":
                source_metrics = kwargs.get("source_metrics") or kwargs.get("metrics") or {}
                rows = []
                if isinstance(source_metrics, dict):
                    for name, value in source_metrics.items():
                        lname = str(name).lower()
                        if any(tok in lname for tok in ["station", "point", "openmeteo", "power"]):
                            scale = "point"
                        elif any(tok in lname for tok in ["grid", "gpm", "chirps", "era5", "raster", "aoi"]):
                            scale = "gridded_or_aoi"
                        elif any(tok in lname for tok in ["report", "national", "regional", "basin"]):
                            scale = "report_or_regional"
                        else:
                            scale = "unknown"
                        rows.append({"source": name, "scale": scale, "value": value})
                cautions = [
                    "Do not treat point metrics as regional maxima without scale justification.",
                    "Do not treat compact AOI or gridded summaries as complete realized-loss evidence.",
                    "Use report-level claims for event identity and impact context, then calibrate with numeric layers.",
                ]
                return ok(tool_name, {"event_scale": kwargs.get("event_scale"), "sources": rows, "scale_cautions": cautions})
            if tool_name == "parse_mcq_options_and_select":
                options = kwargs.get("options")
                question_text = str(kwargs.get("question_text") or kwargs.get("question") or "")
                parsed: dict[str, str] = {}
                if isinstance(options, dict):
                    parsed = {str(k).upper().strip(".: )"): str(v).strip() for k, v in options.items()}
                else:
                    pattern = re.compile(r"(?:^|\n)\s*([A-H])[\.\)]\s+(.+?)(?=(?:\n\s*[A-H][\.\)]\s+)|\Z)", re.S)
                    parsed = {m.group(1).upper(): re.sub(r"\s+", " ", m.group(2)).strip() for m in pattern.finditer(question_text)}
                selected = kwargs.get("selected")
                selected_letter = None
                if selected is not None:
                    m = re.search(r"\b([A-H])\b", str(selected).upper())
                    selected_letter = m.group(1) if m else None
                return ok(tool_name, {"options": parsed, "selected_letter": selected_letter, "valid_selection": selected_letter in parsed if selected_letter else False})
            return ok(tool_name, {"message": "reasoning/output utility executed", "input_keys": sorted(kwargs.keys()), "content": kwargs.get("content") or kwargs.get("answer") or kwargs.get("evidence")})
        return fail(tool_name, f"tool is registered but has no dispatch implementation: {tool_name}")
    except Exception as e:
        return fail(tool_name, f"{type(e).__name__}: {e}")


@dataclass
class ToolSpec:
    name: str
    kit: str
    purpose: str
    inputs: str
    output: str
    used_by: str


class ToolRegistry:
    def __init__(self, specs: list[dict[str, Any]] | None = None):
        self.specs = [ToolSpec(**x) for x in (specs or load_registry())]
        self.by_name = {s.name: s for s in self.specs}
        self.aliases = dict(TOOL_ALIASES)

    def _resolve_name(self, name: str) -> str:
        return self.aliases.get(name, name)

    def list_tools(self, kit: str | None = None) -> list[dict[str, Any]]:
        specs = self.specs if kit is None else [s for s in self.specs if s.kit == kit]
        return [asdict(s) for s in specs]

    def describe(self, name: str) -> dict[str, Any]:
        name = self._resolve_name(name)
        if name not in self.by_name:
            raise KeyError(name)
        return asdict(self.by_name[name])

    def call(self, name: str, **kwargs: Any) -> dict[str, Any]:
        name = self._resolve_name(name)
        if name not in self.by_name:
            return fail(name, "unknown tool")
        return dispatch(name, **kwargs)

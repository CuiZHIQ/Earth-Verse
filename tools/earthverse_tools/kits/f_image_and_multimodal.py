from __future__ import annotations
from typing import Any
from ..core import dispatch

KIT = "F Image and Multimodal"

__all__ = [
    "read_image_rgb_summary",
    "summarize_image_rgb_statistics",
    "compare_image_rgb_summaries",
    "estimate_image_flood_proxy",
    "estimate_image_burn_proxy",
    "estimate_image_obscuration_proxy",
    "read_image_georeference",
    "read_alphaearth_embedding_stats",
    "compare_alphaearth_embedding_stats",
    "read_image_file_metadata",
    "compare_image_proxy_to_hazard_signature",
    "build_image_change_summary",
]


def read_image_rgb_summary(**kwargs: Any) -> dict[str, Any]:
    """read_image_rgb_summary

Kit: F Image and Multimodal
Purpose: Read image dimensions and simple RGB statistics without semantic detection.
Inputs: image_path
Output: image RGB summary
Used by: image statistics tasks
"""
    return dispatch("read_image_rgb_summary", **kwargs)


def summarize_image_rgb_statistics(**kwargs: Any) -> dict[str, Any]:
    """summarize_image_rgb_statistics

Kit: F Image and Multimodal
Purpose: Summarize per-channel RGB statistics, brightness, and contrast proxies.
Inputs: image_path
Output: image RGB statistics
Used by: image diagnostics
"""
    return dispatch("summarize_image_rgb_statistics", **kwargs)


def compare_image_rgb_summaries(**kwargs: Any) -> dict[str, Any]:
    """compare_image_rgb_summaries

Kit: F Image and Multimodal
Purpose: Compare two image RGB summaries and compute simple channel deltas.
Inputs: pre_image, post_image
Output: RGB change summary
Used by: change detection proxies
"""
    return dispatch("compare_image_rgb_summaries", **kwargs)


def estimate_image_flood_proxy(**kwargs: Any) -> dict[str, Any]:
    """estimate_image_flood_proxy

Kit: F Image and Multimodal
Purpose: Estimate a simple flood-like proxy from RGB dominance; not semantic segmentation.
Inputs: image_path, aoi?
Output: flood proxy
Used by: flood imagery proxies
"""
    return dispatch("estimate_image_flood_proxy", **kwargs)


def estimate_image_burn_proxy(**kwargs: Any) -> dict[str, Any]:
    """estimate_image_burn_proxy

Kit: F Image and Multimodal
Purpose: Estimate a simple burn-scar proxy from RGB dominance; not semantic detection.
Inputs: image_path, aoi?
Output: burn proxy
Used by: wildfire imagery proxies
"""
    return dispatch("estimate_image_burn_proxy", **kwargs)


def estimate_image_obscuration_proxy(**kwargs: Any) -> dict[str, Any]:
    """estimate_image_obscuration_proxy

Kit: F Image and Multimodal
Purpose: Estimate cloud, smoke, haze, or ash obscuration proxy from brightness and channel balance.
Inputs: image_path
Output: obscuration proxy
Used by: image reliability proxies
"""
    return dispatch("estimate_image_obscuration_proxy", **kwargs)


def read_image_georeference(**kwargs: Any) -> dict[str, Any]:
    """read_image_georeference

Kit: F Image and Multimodal
Purpose: Read georeferencing metadata from GeoTIFF or related raster metadata.
Inputs: image_path
Output: georeference summary
Used by: image-GIS alignment
"""
    return dispatch("read_image_georeference", **kwargs)


def read_alphaearth_embedding_stats(**kwargs: Any) -> dict[str, Any]:
    """read_alphaearth_embedding_stats

Kit: F Image and Multimodal
Purpose: Read AlphaEarth embedding or change-stat JSON from package files.
Inputs: stats_path
Output: AlphaEarth stats summary
Used by: semantic EO change statistics
"""
    return dispatch("read_alphaearth_embedding_stats", **kwargs)


def compare_alphaearth_embedding_stats(**kwargs: Any) -> dict[str, Any]:
    """compare_alphaearth_embedding_stats

Kit: F Image and Multimodal
Purpose: Compare two AlphaEarth statistics files and report numeric deltas on shared keys.
Inputs: pre_stats_path, post_stats_path
Output: AlphaEarth comparison summary
Used by: longer-term context
"""
    return dispatch("compare_alphaearth_embedding_stats", **kwargs)


def read_image_file_metadata(**kwargs: Any) -> dict[str, Any]:
    """read_image_file_metadata

Kit: F Image and Multimodal
Purpose: Read image file format, size, mode, and info keys.
Inputs: image_path
Output: image file metadata
Used by: file inspection
"""
    return dispatch("read_image_file_metadata", **kwargs)


def compare_image_proxy_to_hazard_signature(**kwargs: Any) -> dict[str, Any]:
    """compare_image_proxy_to_hazard_signature

Kit: F Image and Multimodal
Purpose: Compare heuristic image proxy scores with a named hazard template; not object detection.
Inputs: image_path, hazard_type
Output: proxy comparison JSON
Used by: image-hazard interpretation proxies
"""
    return dispatch("compare_image_proxy_to_hazard_signature", **kwargs)


def build_image_change_summary(**kwargs: Any) -> dict[str, Any]:
    """build_image_change_summary

Kit: F Image and Multimodal
Purpose: Combine before/after image summaries and optional EO metrics into a compact change summary.
Inputs: pre_image, post_image, eo_metrics?
Output: image change summary JSON
Used by: visual-numeric reasoning proxies
"""
    return dispatch("build_image_change_summary", **kwargs)


# Backward-compatible aliases for older traces and notebooks.
inspect_true_color_image = read_image_rgb_summary
compare_before_after_images = compare_image_rgb_summaries
detect_visible_water_extent = estimate_image_flood_proxy
detect_visible_burn_scar = estimate_image_burn_proxy
detect_visible_cloud_or_smoke = estimate_image_obscuration_proxy
query_google_earth_embedding_patch = read_alphaearth_embedding_stats
compare_earth_embedding_years = compare_alphaearth_embedding_stats
summarize_satellite_scene_content = summarize_image_rgb_statistics
locate_objects_in_image = read_image_file_metadata
compare_image_scene_to_hazard_signature = compare_image_proxy_to_hazard_signature
build_visual_change_summary = build_image_change_summary

from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'E Raster and EO'
__all__ = [
    'load_raster_summary',
    'reproject_raster',
    'clip_raster_to_aoi',
    'compute_zonal_raster_stats',
    'compute_raster_threshold_area',
    'compare_pre_post_rasters',
    'compute_ndvi',
    'compute_ndwi',
    'compute_nbr',
    'compute_lst_summary',
    'mask_clouds_from_quality_band',
    'mosaic_rasters',
    'sample_raster_at_points',
    'compute_raster_histogram',
    'align_raster_grids',
    'compute_valid_pixel_fraction',
    'extract_raster_timeseries',
    'export_raster_thumbnail',
]

def load_raster_summary(**kwargs: Any) -> dict[str, Any]:
    """load_raster_summary

Kit: E Raster and EO
Purpose: Inspect raster CRS, resolution, bbox, bands, nodata and value range.
Inputs: path
Output: raster summary
Used by: raster tasks
"""
    return dispatch('load_raster_summary', **kwargs)

def reproject_raster(**kwargs: Any) -> dict[str, Any]:
    """reproject_raster

Kit: E Raster and EO
Purpose: Reproject raster to target CRS or grid.
Inputs: path, target_crs, resolution?
Output: reprojected raster
Used by: alignment
"""
    return dispatch('reproject_raster', **kwargs)

def clip_raster_to_aoi(**kwargs: Any) -> dict[str, Any]:
    """clip_raster_to_aoi

Kit: E Raster and EO
Purpose: Clip raster to AOI and report valid-pixel count.
Inputs: raster_path, aoi
Output: clipped raster summary
Used by: AOI stats
"""
    return dispatch('clip_raster_to_aoi', **kwargs)

def compute_zonal_raster_stats(**kwargs: Any) -> dict[str, Any]:
    """compute_zonal_raster_stats

Kit: E Raster and EO
Purpose: Compute zonal raster mean, max, sum, p95, p99 or count.
Inputs: raster_path, aoi, stats
Output: zonal stats
Used by: physical fields
"""
    return dispatch('compute_zonal_raster_stats', **kwargs)

def compute_raster_threshold_area(**kwargs: Any) -> dict[str, Any]:
    """compute_raster_threshold_area

Kit: E Raster and EO
Purpose: Calculate area exceeding a raster threshold.
Inputs: raster_path, threshold, op, aoi?
Output: area metrics
Used by: flood/burn/heat
"""
    return dispatch('compute_raster_threshold_area', **kwargs)

def compare_pre_post_rasters(**kwargs: Any) -> dict[str, Any]:
    """compare_pre_post_rasters

Kit: E Raster and EO
Purpose: Compute pre/post raster differences and changed area.
Inputs: pre_path, post_path, method, threshold?
Output: change metrics
Used by: RS change
"""
    return dispatch('compare_pre_post_rasters', **kwargs)

def compute_ndvi(**kwargs: Any) -> dict[str, Any]:
    """compute_ndvi

Kit: E Raster and EO
Purpose: Compute NDVI from NIR and red bands.
Inputs: nir_band, red_band
Output: NDVI raster/stats
Used by: vegetation
"""
    return dispatch('compute_ndvi', **kwargs)

def compute_ndwi(**kwargs: Any) -> dict[str, Any]:
    """compute_ndwi

Kit: E Raster and EO
Purpose: Compute water index from green and NIR/SWIR bands.
Inputs: green_band, nir_or_swir_band
Output: NDWI raster/stats
Used by: flood/water
"""
    return dispatch('compute_ndwi', **kwargs)

def compute_nbr(**kwargs: Any) -> dict[str, Any]:
    """compute_nbr

Kit: E Raster and EO
Purpose: Compute burn ratio from NIR and SWIR bands.
Inputs: nir_band, swir_band
Output: NBR raster/stats
Used by: wildfire
"""
    return dispatch('compute_nbr', **kwargs)

def compute_lst_summary(**kwargs: Any) -> dict[str, Any]:
    """compute_lst_summary

Kit: E Raster and EO
Purpose: Summarize land surface temperature raster over AOI.
Inputs: lst_raster, aoi
Output: LST stats
Used by: heat/urban heat island
"""
    return dispatch('compute_lst_summary', **kwargs)

def mask_clouds_from_quality_band(**kwargs: Any) -> dict[str, Any]:
    """mask_clouds_from_quality_band

Kit: E Raster and EO
Purpose: Mask clouds using QA band or scene classification.
Inputs: raster_path, qa_band
Output: cloud-masked raster
Used by: optical images
"""
    return dispatch('mask_clouds_from_quality_band', **kwargs)

def mosaic_rasters(**kwargs: Any) -> dict[str, Any]:
    """mosaic_rasters

Kit: E Raster and EO
Purpose: Mosaic raster tiles and report seam/coverage warnings.
Inputs: raster_paths
Output: mosaic path
Used by: large AOIs
"""
    return dispatch('mosaic_rasters', **kwargs)

def sample_raster_at_points(**kwargs: Any) -> dict[str, Any]:
    """sample_raster_at_points

Kit: E Raster and EO
Purpose: Sample raster values at point locations.
Inputs: raster_path, points_path
Output: sample table
Used by: station comparison
"""
    return dispatch('sample_raster_at_points', **kwargs)

def compute_raster_histogram(**kwargs: Any) -> dict[str, Any]:
    """compute_raster_histogram

Kit: E Raster and EO
Purpose: Compute histogram and quantiles for raster values.
Inputs: raster_path, aoi?, bins
Output: histogram JSON
Used by: distribution reasoning
"""
    return dispatch('compute_raster_histogram', **kwargs)

def align_raster_grids(**kwargs: Any) -> dict[str, Any]:
    """align_raster_grids

Kit: E Raster and EO
Purpose: Align multiple rasters to a common grid.
Inputs: raster_paths, reference_path
Output: aligned paths
Used by: multi-raster metrics
"""
    return dispatch('align_raster_grids', **kwargs)

def compute_valid_pixel_fraction(**kwargs: Any) -> dict[str, Any]:
    """compute_valid_pixel_fraction

Kit: E Raster and EO
Purpose: Compute valid, nodata and masked pixel fractions for a raster layer or AOI clip.
Inputs: path, nodata_value?, band?
Output: valid pixel fraction JSON
Used by: raster diagnostics tasks
"""
    return dispatch('compute_valid_pixel_fraction', **kwargs)

def extract_raster_timeseries(**kwargs: Any) -> dict[str, Any]:
    """extract_raster_timeseries

Kit: E Raster and EO
Purpose: Extract per-date AOI statistics from raster stacks.
Inputs: raster_stack, aoi, stats
Output: raster time series
Used by: GPM/ERA/OISST
"""
    return dispatch('extract_raster_timeseries', **kwargs)

def export_raster_thumbnail(**kwargs: Any) -> dict[str, Any]:
    """export_raster_thumbnail

Kit: E Raster and EO
Purpose: Export a normalized image thumbnail from a raster layer.
Inputs: raster_path, bands, stretch
Output: thumbnail path
Used by: human inspection
"""
    return dispatch('export_raster_thumbnail', **kwargs)

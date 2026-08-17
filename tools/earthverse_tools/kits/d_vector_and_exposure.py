from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'D Vector and Exposure'
__all__ = [
    'load_vector_summary',
    'reproject_vector',
    'clip_vector_to_aoi',
    'buffer_geometries',
    'intersect_vectors',
    'union_hazard_footprints',
    'count_points_in_polygon',
    'calculate_line_length_in_polygon',
    'calculate_polygon_area',
    'estimate_population_exposure',
    'count_facilities_exposed',
    'compute_distance_to_track_or_epicenter',
    'spatial_join_exposure_attributes',
    'estimate_admin_unit_exposure',
    'compute_network_service_area',
    'compute_hazard_aoi_overlap',
    'make_overview_map',
]

def load_vector_summary(**kwargs: Any) -> dict[str, Any]:
    """load_vector_summary

Kit: D Vector and Exposure
Purpose: Inspect vector CRS, bbox, geometry types and feature count.
Inputs: path
Output: vector summary
Used by: GIS tasks
"""
    return dispatch('load_vector_summary', **kwargs)

def reproject_vector(**kwargs: Any) -> dict[str, Any]:
    """reproject_vector

Kit: D Vector and Exposure
Purpose: Reproject vector data to a target CRS.
Inputs: path, target_crs
Output: reprojected path
Used by: spatial alignment
"""
    return dispatch('reproject_vector', **kwargs)

def clip_vector_to_aoi(**kwargs: Any) -> dict[str, Any]:
    """clip_vector_to_aoi

Kit: D Vector and Exposure
Purpose: Clip vector features to an AOI polygon.
Inputs: vector_path, aoi
Output: clipped summary
Used by: AOI tasks
"""
    return dispatch('clip_vector_to_aoi', **kwargs)

def buffer_geometries(**kwargs: Any) -> dict[str, Any]:
    """buffer_geometries

Kit: D Vector and Exposure
Purpose: Create distance buffers around points, lines or polygons.
Inputs: vector_path, distance_km
Output: buffer polygon
Used by: track/epicenter tasks
"""
    return dispatch('buffer_geometries', **kwargs)

def intersect_vectors(**kwargs: Any) -> dict[str, Any]:
    """intersect_vectors

Kit: D Vector and Exposure
Purpose: Intersect two vector layers and summarize overlap.
Inputs: path_a, path_b
Output: intersection metrics
Used by: hazard-exposure
"""
    return dispatch('intersect_vectors', **kwargs)

def union_hazard_footprints(**kwargs: Any) -> dict[str, Any]:
    """union_hazard_footprints

Kit: D Vector and Exposure
Purpose: Union multiple hazard polygons into one footprint.
Inputs: polygon_paths
Output: union footprint
Used by: multi-sensor hazards
"""
    return dispatch('union_hazard_footprints', **kwargs)

def count_points_in_polygon(**kwargs: Any) -> dict[str, Any]:
    """count_points_in_polygon

Kit: D Vector and Exposure
Purpose: Count point features inside an AOI or hazard polygon.
Inputs: points_path, polygon_path
Output: point count
Used by: hotspots/complaints
"""
    return dispatch('count_points_in_polygon', **kwargs)

def calculate_line_length_in_polygon(**kwargs: Any) -> dict[str, Any]:
    """calculate_line_length_in_polygon

Kit: D Vector and Exposure
Purpose: Calculate line length inside polygon by class.
Inputs: line_path, polygon_path, class_filter?
Output: length by class
Used by: roads/rivers
"""
    return dispatch('calculate_line_length_in_polygon', **kwargs)

def calculate_polygon_area(**kwargs: Any) -> dict[str, Any]:
    """calculate_polygon_area

Kit: D Vector and Exposure
Purpose: Calculate polygon area by class in square kilometers.
Inputs: polygon_path, class_filter?
Output: area table
Used by: flood/burn/slip
"""
    return dispatch('calculate_polygon_area', **kwargs)

def estimate_population_exposure(**kwargs: Any) -> dict[str, Any]:
    """estimate_population_exposure

Kit: D Vector and Exposure
Purpose: Estimate population exposed inside a hazard footprint.
Inputs: hazard_polygon, population_grid
Output: exposed population
Used by: impact tasks
"""
    return dispatch('estimate_population_exposure', **kwargs)

def count_facilities_exposed(**kwargs: Any) -> dict[str, Any]:
    """count_facilities_exposed

Kit: D Vector and Exposure
Purpose: Count facilities exposed by type.
Inputs: hazard_polygon, facilities_vector, facility_types
Output: facility counts
Used by: schools/hospitals
"""
    return dispatch('count_facilities_exposed', **kwargs)

def compute_distance_to_track_or_epicenter(**kwargs: Any) -> dict[str, Any]:
    """compute_distance_to_track_or_epicenter

Kit: D Vector and Exposure
Purpose: Compute minimum distance from locations to a cyclone track, river or epicenter.
Inputs: locations, track_or_point
Output: distance metrics
Used by: cyclone/earthquake
"""
    return dispatch('compute_distance_to_track_or_epicenter', **kwargs)

def spatial_join_exposure_attributes(**kwargs: Any) -> dict[str, Any]:
    """spatial_join_exposure_attributes

Kit: D Vector and Exposure
Purpose: Join hazard and exposure attributes by spatial relation.
Inputs: hazard_path, exposure_path, predicate
Output: joined exposure table
Used by: impact chain
"""
    return dispatch('spatial_join_exposure_attributes', **kwargs)

def estimate_admin_unit_exposure(**kwargs: Any) -> dict[str, Any]:
    """estimate_admin_unit_exposure

Kit: D Vector and Exposure
Purpose: Aggregate exposed population or infrastructure by admin unit.
Inputs: hazard_path, admin_path, exposure_data
Output: admin exposure table
Used by: briefings
"""
    return dispatch('estimate_admin_unit_exposure', **kwargs)

def compute_network_service_area(**kwargs: Any) -> dict[str, Any]:
    """compute_network_service_area

Kit: D Vector and Exposure
Purpose: Estimate service area or reachable network segments around facilities.
Inputs: network_path, facility_points, distance
Output: service area summary
Used by: response access
"""
    return dispatch('compute_network_service_area', **kwargs)

def compute_hazard_aoi_overlap(**kwargs: Any) -> dict[str, Any]:
    """compute_hazard_aoi_overlap

Kit: D Vector and Exposure
Purpose: Compute overlap between a hazard footprint or track buffer and the event AOI/admin geometry.
Inputs: hazard_vector, aoi_vector, metric?
Output: overlap area/ratio JSON
Used by: spatial hazard tasks
"""
    return dispatch('compute_hazard_aoi_overlap', **kwargs)

def make_overview_map(**kwargs: Any) -> dict[str, Any]:
    """make_overview_map

Kit: D Vector and Exposure
Purpose: Create a static overview map with AOI, hazard and key exposure layers.
Inputs: layers, output_path
Output: map artifact
Used by: visual reporting
"""
    return dispatch('make_overview_map', **kwargs)

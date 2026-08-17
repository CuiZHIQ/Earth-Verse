from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'H Fire Air Geophysics Ocean'
__all__ = [
    'compute_fire_hotspot_metrics',
    'compute_burned_area_metrics',
    'compute_fire_weather_index_proxy',
    'compute_smoke_pm_lag_metrics',
    'compute_air_quality_exceedance',
    'interpolate_station_pollution',
    'compute_earthquake_sequence_metrics',
    'compute_shakemap_exposure',
    'estimate_ground_failure_susceptibility',
    'compute_landslide_trigger_index',
    'compute_volcano_ash_extent',
    'compute_so2_anomaly',
    'compute_tsunami_coastal_exposure',
    'compute_dust_storm_metrics',
    'compute_ocean_heat_content_proxy',
    'compute_coral_bleaching_alert',
    'compute_tide_surge_compound_index',
    'compute_multihazard_overlap_score',
]

def compute_fire_hotspot_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_fire_hotspot_metrics

Kit: H Fire Air Geophysics Ocean
Purpose: Summarize FIRMS hotspots, FRP and density inside AOI/time window.
Inputs: hotspot_points, aoi, time_window
Output: hotspot metrics
Used by: wildfire
"""
    return dispatch('compute_fire_hotspot_metrics', **kwargs)

def compute_burned_area_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_burned_area_metrics

Kit: H Fire Air Geophysics Ocean
Purpose: Compute burned area and severity from masks or NBR change.
Inputs: burn_mask_or_dnbr, aoi
Output: burn metrics
Used by: wildfire
"""
    return dispatch('compute_burned_area_metrics', **kwargs)

def compute_fire_weather_index_proxy(**kwargs: Any) -> dict[str, Any]:
    """compute_fire_weather_index_proxy

Kit: H Fire Air Geophysics Ocean
Purpose: Compute fire-weather risk proxy from temperature, humidity, wind and rain.
Inputs: weather_series
Output: FWI proxy
Used by: fire risk
"""
    return dispatch('compute_fire_weather_index_proxy', **kwargs)

def compute_smoke_pm_lag_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_smoke_pm_lag_metrics

Kit: H Fire Air Geophysics Ocean
Purpose: Link smoke/hotspot timing to PM2.5 or AQI response.
Inputs: smoke_or_fire, pm_series, lags
Output: lag metrics
Used by: smoke health
"""
    return dispatch('compute_smoke_pm_lag_metrics', **kwargs)

def compute_air_quality_exceedance(**kwargs: Any) -> dict[str, Any]:
    """compute_air_quality_exceedance

Kit: H Fire Air Geophysics Ocean
Purpose: Count exceedance days and peaks for PM2.5, O3, NO2 or AQI.
Inputs: pollution_series, standards
Output: AQ metrics
Used by: air quality
"""
    return dispatch('compute_air_quality_exceedance', **kwargs)

def interpolate_station_pollution(**kwargs: Any) -> dict[str, Any]:
    """interpolate_station_pollution

Kit: H Fire Air Geophysics Ocean
Purpose: Interpolate station pollution to a coarse AOI surface.
Inputs: station_points, values, method
Output: interpolated surface/stats
Used by: AQ spatial gaps
"""
    return dispatch('interpolate_station_pollution', **kwargs)

def compute_earthquake_sequence_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_earthquake_sequence_metrics

Kit: H Fire Air Geophysics Ocean
Purpose: Compute mainshock/aftershock counts, magnitude decay and spatial spread.
Inputs: quake_catalog, event_window
Output: sequence metrics
Used by: earthquake
"""
    return dispatch('compute_earthquake_sequence_metrics', **kwargs)

def compute_shakemap_exposure(**kwargs: Any) -> dict[str, Any]:
    """compute_shakemap_exposure

Kit: H Fire Air Geophysics Ocean
Purpose: Overlay shaking intensity zones with population/facilities.
Inputs: shakemap, exposure_layers
Output: shake exposure
Used by: earthquake impact
"""
    return dispatch('compute_shakemap_exposure', **kwargs)

def estimate_ground_failure_susceptibility(**kwargs: Any) -> dict[str, Any]:
    """estimate_ground_failure_susceptibility

Kit: H Fire Air Geophysics Ocean
Purpose: Estimate landslide/liquefaction susceptibility from shaking, slope and soil proxies.
Inputs: shaking, slope, soil?
Output: susceptibility score
Used by: earthquake/landslide
"""
    return dispatch('estimate_ground_failure_susceptibility', **kwargs)

def compute_landslide_trigger_index(**kwargs: Any) -> dict[str, Any]:
    """compute_landslide_trigger_index

Kit: H Fire Air Geophysics Ocean
Purpose: Combine rainfall, slope and antecedent wetness into landslide trigger index.
Inputs: rain, slope, soil_moisture?
Output: trigger index
Used by: landslide
"""
    return dispatch('compute_landslide_trigger_index', **kwargs)

def compute_volcano_ash_extent(**kwargs: Any) -> dict[str, Any]:
    """compute_volcano_ash_extent

Kit: H Fire Air Geophysics Ocean
Purpose: Estimate ash/cloud extent from polygons, images or VAAC reports.
Inputs: ash_data, aoi
Output: ash extent
Used by: volcano
"""
    return dispatch('compute_volcano_ash_extent', **kwargs)

def compute_so2_anomaly(**kwargs: Any) -> dict[str, Any]:
    """compute_so2_anomaly

Kit: H Fire Air Geophysics Ocean
Purpose: Compute SO2 anomaly or plume intensity over AOI.
Inputs: so2_raster_or_series, baseline
Output: SO2 anomaly
Used by: volcano
"""
    return dispatch('compute_so2_anomaly', **kwargs)

def compute_tsunami_coastal_exposure(**kwargs: Any) -> dict[str, Any]:
    """compute_tsunami_coastal_exposure

Kit: H Fire Air Geophysics Ocean
Purpose: Estimate coastal exposure to tsunami warning or inundation proxy.
Inputs: coast, elevation, population, warning_zone
Output: coastal exposure
Used by: tsunami
"""
    return dispatch('compute_tsunami_coastal_exposure', **kwargs)

def compute_dust_storm_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_dust_storm_metrics

Kit: H Fire Air Geophysics Ocean
Purpose: Compute dust-storm intensity from visibility, AOD, wind or PM indicators.
Inputs: dust_series_or_raster
Output: dust metrics
Used by: dust
"""
    return dispatch('compute_dust_storm_metrics', **kwargs)

def compute_ocean_heat_content_proxy(**kwargs: Any) -> dict[str, Any]:
    """compute_ocean_heat_content_proxy

Kit: H Fire Air Geophysics Ocean
Purpose: Estimate ocean heat-content proxy from SST anomaly and depth/region data if available.
Inputs: sst_anomaly, region, depth?
Output: OHC proxy
Used by: ocean events
"""
    return dispatch('compute_ocean_heat_content_proxy', **kwargs)

def compute_coral_bleaching_alert(**kwargs: Any) -> dict[str, Any]:
    """compute_coral_bleaching_alert

Kit: H Fire Air Geophysics Ocean
Purpose: Compute bleaching alert from hotspot and degree-heating-weeks style inputs.
Inputs: sst, climatology
Output: bleaching alert
Used by: marine heatwave
"""
    return dispatch('compute_coral_bleaching_alert', **kwargs)

def compute_tide_surge_compound_index(**kwargs: Any) -> dict[str, Any]:
    """compute_tide_surge_compound_index

Kit: H Fire Air Geophysics Ocean
Purpose: Combine tide, surge and rainfall timing into compound coastal flood risk.
Inputs: tide, surge_proxy, rainfall
Output: compound index
Used by: coastal flood
"""
    return dispatch('compute_tide_surge_compound_index', **kwargs)

def compute_multihazard_overlap_score(**kwargs: Any) -> dict[str, Any]:
    """compute_multihazard_overlap_score

Kit: H Fire Air Geophysics Ocean
Purpose: Score overlap among multiple hazards in space and time.
Inputs: hazard_layers, weights
Output: overlap score
Used by: compound events
"""
    return dispatch('compute_multihazard_overlap_score', **kwargs)

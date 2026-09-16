from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'G Weather Hydro Climate'
__all__ = [
    'compute_precip_accumulation',
    'compute_precip_intensity_duration',
    'compute_flood_impact_metrics',
    'compute_streamflow_anomaly',
    'estimate_runoff_proxy',
    'compute_spei_spi',
    'compute_soil_moisture_percentile',
    'compute_heat_index',
    'compute_wet_bulb_temperature',
    'compute_apparent_temperature_stats',
    'compute_warm_night_count',
    'compute_heatwave_duration_intensity',
    'compute_cyclone_track_metrics',
    'compute_storm_surge_proxy',
    'compute_wind_exposure_metrics',
    'compute_enso_phase_metrics',
    'compute_teleconnection_lag_correlation',
    'compute_marine_heatwave_metrics',
    'compute_cold_spell_metrics',
    'compute_snow_ice_anomaly',
    'compute_hot_dry_vpd_metrics',
    'compute_urban_pluvial_diagnostics',
]

def compute_precip_accumulation(**kwargs: Any) -> dict[str, Any]:
    """compute_precip_accumulation

Kit: G Weather Hydro Climate
Purpose: Compute event-window precipitation accumulation.
Inputs: precip_series_or_raster, start, end, aoi?
Output: accumulation stats
Used by: rain/flood
"""
    return dispatch('compute_precip_accumulation', **kwargs)

def compute_precip_intensity_duration(**kwargs: Any) -> dict[str, Any]:
    """compute_precip_intensity_duration

Kit: G Weather Hydro Climate
Purpose: Compute max intensity over multiple durations.
Inputs: precip_series, durations
Output: ID stats
Used by: flash flood
"""
    return dispatch('compute_precip_intensity_duration', **kwargs)

def compute_flood_impact_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_flood_impact_metrics

Kit: G Weather Hydro Climate
Purpose: Combine flood area, exposed population and road length metrics.
Inputs: flood_mask, population, roads
Output: flood impact JSON
Used by: flood GT
"""
    return dispatch('compute_flood_impact_metrics', **kwargs)

def compute_streamflow_anomaly(**kwargs: Any) -> dict[str, Any]:
    """compute_streamflow_anomaly

Kit: G Weather Hydro Climate
Purpose: Compute streamflow anomaly or return-period proxy.
Inputs: streamflow_series, climatology
Output: flow anomaly
Used by: river flood
"""
    return dispatch('compute_streamflow_anomaly', **kwargs)

def estimate_runoff_proxy(**kwargs: Any) -> dict[str, Any]:
    """estimate_runoff_proxy

Kit: G Weather Hydro Climate
Purpose: Estimate runoff proxy from rainfall, slope and soil/land-cover context.
Inputs: rain, slope, soil?, landcover?
Output: runoff risk score
Used by: flash flood/landslide
"""
    return dispatch('estimate_runoff_proxy', **kwargs)

def compute_spei_spi(**kwargs: Any) -> dict[str, Any]:
    """compute_spei_spi

Kit: G Weather Hydro Climate
Purpose: Compute SPI/SPEI drought index from precipitation and PET data.
Inputs: precip_series, pet_series?, scale
Output: drought index
Used by: drought
"""
    return dispatch('compute_spei_spi', **kwargs)

def compute_soil_moisture_percentile(**kwargs: Any) -> dict[str, Any]:
    """compute_soil_moisture_percentile

Kit: G Weather Hydro Climate
Purpose: Compute soil moisture percentile against baseline.
Inputs: soil_moisture, baseline
Output: percentile
Used by: drought/flood precondition
"""
    return dispatch('compute_soil_moisture_percentile', **kwargs)

def compute_heat_index(**kwargs: Any) -> dict[str, Any]:
    """compute_heat_index

Kit: G Weather Hydro Climate
Purpose: Compute heat index from temperature and relative humidity.
Inputs: temp, rh
Output: heat index series
Used by: heat
"""
    return dispatch('compute_heat_index', **kwargs)

def compute_wet_bulb_temperature(**kwargs: Any) -> dict[str, Any]:
    """compute_wet_bulb_temperature

Kit: G Weather Hydro Climate
Purpose: Compute wet-bulb temperature from temperature, humidity and pressure.
Inputs: temp, rh, pressure?
Output: wet-bulb series
Used by: humid heat
"""
    return dispatch('compute_wet_bulb_temperature', **kwargs)

def compute_apparent_temperature_stats(**kwargs: Any) -> dict[str, Any]:
    """compute_apparent_temperature_stats

Kit: G Weather Hydro Climate
Purpose: Compute apparent temperature peak and persistence.
Inputs: temp, humidity, wind?, radiation?
Output: apparent temp stats
Used by: heat health
"""
    return dispatch('compute_apparent_temperature_stats', **kwargs)

def compute_warm_night_count(**kwargs: Any) -> dict[str, Any]:
    """compute_warm_night_count

Kit: G Weather Hydro Climate
Purpose: Count warm nights or high minimum-temperature runs.
Inputs: daily_min_temp, threshold
Output: warm-night metrics
Used by: heat stress
"""
    return dispatch('compute_warm_night_count', **kwargs)

def compute_heatwave_duration_intensity(**kwargs: Any) -> dict[str, Any]:
    """compute_heatwave_duration_intensity

Kit: G Weather Hydro Climate
Purpose: Compute heatwave duration, peak Tmax and cumulative intensity.
Inputs: daily_temp, thresholds
Output: heatwave metrics
Used by: heat
"""
    return dispatch('compute_heatwave_duration_intensity', **kwargs)

def compute_cyclone_track_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_cyclone_track_metrics

Kit: G Weather Hydro Climate
Purpose: Compute track proximity, max wind and landfall timing.
Inputs: track_file, aoi
Output: cyclone metrics
Used by: cyclone
"""
    return dispatch('compute_cyclone_track_metrics', **kwargs)

def compute_storm_surge_proxy(**kwargs: Any) -> dict[str, Any]:
    """compute_storm_surge_proxy

Kit: G Weather Hydro Climate
Purpose: Estimate surge-risk proxy from wind, pressure, coast distance and tide context.
Inputs: track, wind, pressure, coast
Output: surge proxy
Used by: coastal flood
"""
    return dispatch('compute_storm_surge_proxy', **kwargs)

def compute_wind_exposure_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_wind_exposure_metrics

Kit: G Weather Hydro Climate
Purpose: Compute population or infrastructure exposed to wind threshold zones.
Inputs: wind_field, exposure_layers
Output: wind exposure
Used by: cyclone/storm
"""
    return dispatch('compute_wind_exposure_metrics', **kwargs)

def compute_enso_phase_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_enso_phase_metrics

Kit: G Weather Hydro Climate
Purpose: Compute ENSO phase and strength from Niño indices or SST anomalies.
Inputs: nino_series, dates
Output: ENSO metrics
Used by: ENSO
"""
    return dispatch('compute_enso_phase_metrics', **kwargs)

def compute_teleconnection_lag_correlation(**kwargs: Any) -> dict[str, Any]:
    """compute_teleconnection_lag_correlation

Kit: G Weather Hydro Climate
Purpose: Estimate lagged relationship between climate index and regional hazard.
Inputs: index_series, hazard_series, lags
Output: lag correlation
Used by: ENSO impact
"""
    return dispatch('compute_teleconnection_lag_correlation', **kwargs)

def compute_marine_heatwave_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_marine_heatwave_metrics

Kit: G Weather Hydro Climate
Purpose: Compute MHW duration, intensity and cumulative intensity.
Inputs: sst_series, climatology
Output: MHW metrics
Used by: ocean heat
"""
    return dispatch('compute_marine_heatwave_metrics', **kwargs)

def compute_cold_spell_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_cold_spell_metrics

Kit: G Weather Hydro Climate
Purpose: Compute cold-spell duration and anomaly intensity.
Inputs: temperature_series, thresholds
Output: cold metrics
Used by: cold wave
"""
    return dispatch('compute_cold_spell_metrics', **kwargs)

def compute_snow_ice_anomaly(**kwargs: Any) -> dict[str, Any]:
    """compute_snow_ice_anomaly

Kit: G Weather Hydro Climate
Purpose: Compute snow or ice anomaly from raster/time series products.
Inputs: snow_or_ice_data, baseline
Output: snow/ice anomaly
Used by: cryosphere
"""
    return dispatch('compute_snow_ice_anomaly', **kwargs)

def compute_hot_dry_vpd_metrics(**kwargs: Any) -> dict[str, Any]:
    """compute_hot_dry_vpd_metrics

Kit: G Weather Hydro Climate
Purpose: Compute hot-dry burden, VPD proxy, hot-dry hours or days, and peak dry-heat stress from temperature and humidity series.
Inputs: path or arrays, temp_col?, rh_col?, temp_threshold?, rh_max?
Output: hot-dry/VPD metrics
Used by: heat, drought, and fire-weather tasks
"""
    return dispatch('compute_hot_dry_vpd_metrics', **kwargs)

def compute_urban_pluvial_diagnostics(**kwargs: Any) -> dict[str, Any]:
    """compute_urban_pluvial_diagnostics

Kit: G Weather Hydro Climate
Purpose: Compute short-duration rainfall concentration, burst ratio, event total, and urban drainage-overload diagnostic labels.
Inputs: path or values, precip_col?, durations?, burst_threshold?
Output: urban pluvial diagnostics
Used by: city flash-flood and drainage-overload tasks
"""
    return dispatch('compute_urban_pluvial_diagnostics', **kwargs)

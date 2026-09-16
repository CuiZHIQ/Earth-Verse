# Final Answer

```json
{
  "answer": "storm_tide_surge_dominant_with_pressure_wind_forcing_support",
  "target_family": "sandy_coastal_mechanism_dominance_ranking",
  "computed_values": {
    "coastal_major_gages": 10,
    "max_storm_tide_ft": 11.75,
    "fema_100yr_or_higher_gages": 8,
    "fema_recurrence_scope": "quantified USGS New York coastal-gage list; broader NY-NJ-CT support is narrative/report context",
    "storm_surge_sensors": 38,
    "pressure_sensors": 10,
    "high_water_marks_min": 300,
    "gdacs_max_wind_kmh": 167.4,
    "power_peak_wind_kmh": 69.3,
    "openmeteo_peak_wind_kmh": 60.6,
    "event_rain_mm": 45.4,
    "wettest_24h_rain_mm": 37.4
  },
  "mechanism_scores": {
    "storm_tide_surge_dominance": 96,
    "pressure_wind_forcing": 80,
    "rainfall_flooding_only": 36,
    "generic_track_label": 24,
    "coastal_exposure_or_loss_only": 6
  },
  "ranked_mechanisms": [
    "storm_tide_surge_dominance",
    "pressure_wind_forcing",
    "rainfall_flooding_only",
    "generic_track_label",
    "coastal_exposure_or_loss_only"
  ],
  "dominant_mechanism": "storm_tide_surge_dominance",
  "rejected_mechanism": "coastal_exposure_or_loss_only",
  "reasoning_path": "Storm tide dominates: 10 coastal gages exceeded major level, 8 reached or approached FEMA 100-year elevations, and max tide was 11.75 ft. Wind/track forcing supports surge timing, but 45.4 mm rain and generic/loss labels do not explain measured coastal water levels alone."
}
```

# Key Computations

- Coastal water levels: 10 listed USGS coastal gages exceeded the National Weather Service major coastal flood elevation. The maximum listed storm tide is 11.75 ft at Rockaway Inlet near Floyd Bennett Field, NY.
- FEMA comparison: 7 gages were above FEMA 100-year levels and 1 approached a FEMA 100-year level, so the combined count is 8. This quantified recurrence comparison comes from the USGS New York coastal-gage list; broader New York-New Jersey-Connecticut support is narrative/report context, not a separate New Jersey gage count.
- Surge observation support: the report text gives 38 storm-surge sensors, 10 barometric-pressure sensors, and over 300 high-water marks.
- Wind and track support: the Sandy GDACS feature gives a maximum wind near 167.4 km/h. The local Open-Meteo point peaks at 60.6 km/h, and NASA POWER daily wind peaks at 69.3 km/h on the main impact date.
- Rainfall context: the local hourly event rain total is 45.4 mm, with a wettest 24-hour sum of 37.4 mm. NASA POWER gives 43.8 mm over the same event window, while gridded rainfall summaries remain context rather than the dominant coastal mechanism.

# Ranking Logic

The score for `storm_tide_surge_dominance` uses the visible weighted formula over major-gage count, FEMA 100-year support, peak storm tide, record coastal-flood language, surge sensors, and high-water marks. This gives 96, the highest score.

The score for `pressure_wind_forcing` uses the visible weighted formula over catalog wind, local wind peaks, storm-force duration, right-of-center landfall timing, and pressure-sensor support. This gives 80: strong as a surge-generating mechanism, but secondary to the measured coastal water levels.

The rainfall-only score is 36 because the rain totals are real but do not explain the measured tide-gage exceedances by themselves. `generic_track_label` scores 24 because a tropical-cyclone label and duration are identifying context, not a mechanism diagnosis. `coastal_exposure_or_loss_only` scores 6 and is rejected because location, exposure, and consequences are not physical flood-generation mechanisms.

# Reasoning Path

First, extract the coastal gage list and recurrence-level notes, then count the major-flood and FEMA 100-year-or-higher evidence. Second, cross-check that the event reports describe catastrophic storm surge, record coastal flooding, surge instrumentation, high-water marks, wind duration, and landfall geometry. Third, compute local wind and rainfall metrics from weather time series and daily summaries. Finally, rank mechanisms by how directly they explain Sandy's measured coastal water levels.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "A rainfall-only or generic track-label answer fails because rainfall totals and track labels do not explain measured storm-tide exceedances.",
    "evidence_weighting": "Coastal gage exceedances, FEMA recurrence comparisons, peak storm tide, surge sensors, and high-water marks dominate the ranking; wind and track explain forcing support.",
    "uncertainty_or_scale_caveat": "The recurrence comparison is quantified from the USGS New York coastal-gage list, while broader NY-NJ-CT statements remain report-context evidence."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

20 points total:

- Final ranking and compact answer, 4 points: ranks `storm_tide_surge_dominance` first, `pressure_wind_forcing` second, `rainfall_flooding_only` third, `generic_track_label` fourth, and `coastal_exposure_or_loss_only` last with the deterministic answer label. Partial credit: 2-3 points if storm tide/surge is first but middle ranks are partly reversed; 1 point for a coastal-flood dominant label without the specified ranking.
- Coastal water-level calculations, 4 points: computes 10 major coastal gages, 11.75 ft maximum storm tide, and 8 gages reaching or approaching FEMA 100-year levels. Partial credit: 2-3 points for two correct coastal values; 1 point for only one correct coastal value.
- Surge record and instrumentation support, 3 points: uses the record coastal-flood wording plus 38 storm-surge sensors, 10 barometric-pressure sensors, and over 300 high-water marks as mechanism evidence. Partial credit: 1-2 points for recognizing record coastal flooding or instrumentation but missing one or more counts.
- Wind and timing support, 3 points: uses GDACS maximum wind near 167.4 km/h, local peak wind near 60.6 km/h, NASA POWER peak wind near 69.3 km/h, and landfall/right-of-center timing to support the forcing rank. Partial credit: 1-2 points for wind support without the catalog or timing evidence.
- Rainfall-only demotion, 3 points: computes local event rain near 45.4 mm and wettest 24-hour rain near 37.4 mm, uses rainfall summaries as context, and explains why rainfall-only cannot dominate over the measured coastal water levels. Partial credit: 1-2 points for correct rainfall values without explicitly demoting rainfall-only.
- Rejected non-mechanisms and output discipline, 3 points: rejects `coastal_exposure_or_loss_only` and generic track labeling as non-dominant explanatory mechanisms, avoids AOI/population/exposure dependencies, and returns compact JSON with minimal prose. Partial credit: 1-2 points for the right physical stance with extra response-priority or exposure-only language; no credit here if the answer is mainly advice or impact triage.

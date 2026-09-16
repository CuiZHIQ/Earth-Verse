# Hurricane Sandy Coastal Mechanism Dominance Ranking

A coastal hazards analyst is revisiting Hurricane Sandy's New York and New Jersey metropolitan coastal impacts. The task is to rank physical mechanisms by explanatory dominance for the coastal impact diagnosis.

Use only local evidence in the CSX-089 event package. Read across available storm-tide/coastal-water-level evidence, event reports, catalog or hazard summaries, local weather time series, and rainfall summaries when present.

Rank these candidate mechanisms:

- `storm_tide_surge_dominance`
- `pressure_wind_forcing`
- `rainfall_flooding_only`
- `coastal_exposure_or_loss_only`
- `generic_track_label`

Compute the evidence needed to support the ranking, including coastal gage exceedances, peak storm tide, recurrence-level comparisons, surge-observation instrumentation, wind/track timing support, and rainfall totals. Return compact JSON in this shape:

Use transparent mechanism scores. Apply `cap(x)=min(max(x,0),1)`. Score `storm_tide_surge_dominance` as `round(34*cap(major_gages/10)+26*cap(fema_100yr_or_higher_gages/8)+18*cap(max_storm_tide_ft/11.75)+8*record_coastal_flood_flag+6*cap(storm_surge_sensors/38)+4*cap(high_water_marks_min/300))`. Score `pressure_wind_forcing` as `round(30*cap(gdacs_max_wind_kmh/167)+16*cap(power_peak_wind_kmh/69)+14*cap(openmeteo_peak_wind_kmh/60)+8*gale_to_storm_force_duration_flag+7*right_of_center_landfall_flag+5*cap(pressure_sensors/10))`. Score `rainfall_flooding_only` as `round(max(0, 24*cap(event_rain_mm/75)+18*cap(wettest_24h_rain_mm/50)+12*cap(power_event_rain_mm/75)+8*cap(gpm_mean_mm/100)+8*cap(era5_mean_mm/75)-7*coastal_surge_dominance_flag))`. Score `generic_track_label` from catalog-track identity, event-name hurricane label, and duration context only; score `coastal_exposure_or_loss_only` only from consequence/location language, not from physical forcing.

When reporting recurrence-level comparisons, distinguish the quantified USGS New York coastal-gage list from broader New York-New Jersey-Connecticut narrative support; do not imply a separate New Jersey gage recurrence count unless the local evidence gives one.

```json
{
  "answer": "<compact_label>",
  "target_family": "sandy_coastal_mechanism_dominance_ranking",
  "computed_values": {
    "<metric_name_with_unit_if_needed>": 0
  },
  "mechanism_scores": {
    "<mechanism_name>": 0
  },
  "ranked_mechanisms": ["<highest_dominance>", "...", "<lowest_dominance>"],
  "dominant_mechanism": "<mechanism_name>",
  "rejected_mechanism": "<mechanism_name>",
  "reasoning_path": "<compact calculation-based rationale>"
}
```

Add no more than one sentence after the JSON.

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to strengthen mechanism ranking by explaining why measured coastal water levels dominate while wind forcing remains secondary support.


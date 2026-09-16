# El Nino Drought Stress and Livelihood-Response Priority Model

Use only the local CSX-280 event package. Select package-relative evidence for every evidence family you use.

Reconstruct a coupled drought-stress model for the 2015-2016 El Nino and Ethiopia food-security crisis. The model should connect the Pacific teleconnection signal to Ethiopian rainfall and crop failure, package-derived landscape browning/darkening indicators, humanitarian load, short-window precipitation-estimate uncertainty, and package-derived response-access indicators.

Compute these normalized components:

- `teleconnection_norm = 0.50 * clip(peak_CPC_ONI_anomaly_C / 2.5, 0, 1) + 0.30 * clip(count_CPC_ONI_anomaly_ge_2C / 6, 0, 1) + 0.20 * clip(abs(min_monthly_SOI) / 3.5, 0, 1)`, using only 2015-2016 records.
- `rainfall_crop_failure_norm = 0.30 * broad_highland_rainfall_deficit_midpoint + 0.25 * severe_highland_rainfall_deficit + 0.30 * crop_production_loss_midpoint + 0.15 * east_crop_failure_flag`, where rainfall received as a fraction of normal is converted to deficit, crop-production loss is a fraction, and the east crop-failure flag is 1 when complete failure is reported.
- `landscape_degradation_norm = 0.40 * clip(green_drop_pp / 10, 0, 1) + 0.35 * clip(dark_gain_pp / 10, 0, 1) + 0.25 * clip(excess_green_drop / 2, 0, 1)`, comparing the pre-event and event images.
- `livelihood_response_pressure_norm = 0.45 * clip(food_insecure_people / 10200000, 0, 1) + 0.25 * (food_aid_people / food_insecure_people) + 0.20 * (1 - response_target_people / food_insecure_people) + 0.10 * (1 - clip(response_plan_usd_per_food_insecure_person / 10, 0, 1))`.
- `precipitation_uncertainty_norm = clip(precip_spread_ratio / 0.30, 0, 1)`, where `precip_spread_ratio` is the max-minus-min spread across the three event-precipitation mean estimates divided by their mean.
- `facility_access_norm = 0.55 * clip(critical_facilities_per_100k / 20, 0, 1) + 0.30 * clip(road_features_per_100k / 75, 0, 1) + 0.15 * clip(building_features_per_100k / 50, 0, 1)`.

Then compute:

- `drought_stress_index = 100 * (0.28 * teleconnection_norm + 0.24 * rainfall_crop_failure_norm + 0.18 * landscape_degradation_norm + 0.18 * livelihood_response_pressure_norm + 0.12 * precipitation_uncertainty_norm)`.
- `response_priority_score = 100 * (0.30 * rainfall_crop_failure_norm + 0.25 * livelihood_response_pressure_norm + 0.20 * landscape_degradation_norm + 0.15 * facility_access_norm + 0.10 * precipitation_uncertainty_norm)`.

Run a continued-stress scenario in which broad and severe rainfall deficits each worsen by 0.10, crop-production loss worsens by 0.05, the three image-change terms worsen by 10%, the reached response population falls by 20%, and precipitation-estimate uncertainty worsens by 15%; apply clipping after each perturbation. Keep the teleconnection and facility-access terms unchanged.

Round all normalized components and intermediate rates to 3 decimals. Round both index scores and deltas to 2 decimals.

Return one JSON object with this shape:

```json
{
  "process_model": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "drought_stress_index": 0.0,
    "response_priority_score": 0.0,
    "severity_class": "<class>"
  },
  "computed_metrics": {
    "teleconnection_norm": 0.0,
    "rainfall_crop_failure_norm": 0.0,
    "landscape_degradation_norm": 0.0,
    "livelihood_response_pressure_norm": 0.0,
    "precipitation_uncertainty_norm": 0.0,
    "facility_access_norm": 0.0
  },
  "scenario_analysis": {
    "continued_stress_drought_index": 0.0,
    "continued_stress_response_priority": 0.0,
    "drought_index_delta": 0.0,
    "response_priority_delta": 0.0
  },
  "mechanism_chain": ["<concise causal step>", "<concise causal step>", "<concise causal step>"],
  "source_paths": ["<package-relative path>", "..."],
  "final_interpretation": "<one concise sentence>"
}
```

Use `severe_teleconnected_livelihood_crisis` when `drought_stress_index >= 80`, `high_teleconnected_livelihood_crisis` when it is at least 65 but below 80, and `moderate_teleconnected_livelihood_crisis` otherwise.

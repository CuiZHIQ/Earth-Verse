# Christchurch Liquefaction-Weighted Seismic Score

Compute a numeric score from the local CSX-238 package for the 22 February 2011 Christchurch earthquake. Use structured package records for the earthquake catalog, ground-failure product, event impact text, and precipitation samples.

Let `clamp(x)=max(0,min(x,1))`.

Compute these terms:

- `S = mean(clamp(M/6.5), clamp(MMI/8.8), clamp(CDI/8.5), clamp(10/depth_km), clamp(felt/200))`
- `G = sqrt((liquefaction_pop/landslide_pop) * (liquefaction_hazard/landslide_hazard))`
- `G_norm = clamp(ln(G)/ln(40))`
- `I = mean(clamp(deaths/100), clamp(injuries/1000), clamp(buildings_damaged_or_destroyed/50000), landslide_flag, liquefaction_flag)`
- `R = 1 + mean(open_meteo_precip_mm, power_precip_mm, era5_mean_mm, gpm_mean_mm, chirps_mean_mm) / 10`
- `score = 100 * (0.35*S + 0.35*G_norm + 0.25*I + 0.05/R)`

Threshold rules:

- `S >= 0.90`
- `G >= 25.0`
- `G_norm >= 0.90`
- `I >= 0.80`
- `R <= 1.50`

Use `final_label = "shallow_liquefaction_weighted_urban_seismic_record"` when the score is at least 90.0 and all threshold rules pass; otherwise use `final_label = "lower_liquefaction_weighted_score"`.

Round `S`, `G_norm`, `I`, and `R` to three decimals; round `G` to three decimals and `score` to one decimal.

Return only compact JSON:

```json
{
  "target_family": "christchurch_liquefaction_weighted_seismic_score",
  "terms": [
    {"term": "S", "value": 0, "threshold_result": ""},
    {"term": "G", "value": 0, "threshold_result": ""},
    {"term": "G_norm", "value": 0, "threshold_result": ""},
    {"term": "I", "value": 0, "threshold_result": ""},
    {"term": "R", "value": 0, "threshold_result": ""}
  ],
  "score": 0,
  "final_label": "",
  "numeric_note": ""
}
```

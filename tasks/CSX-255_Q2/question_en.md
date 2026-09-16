# Cyclone Freddy Threshold Ledger

Use the local CSX-255 package for Cyclone Freddy during 2023-02-21 through 2023-03-31. Build a calculation-first ledger from structured package layers: three accumulated precipitation products, two surface-change summaries, WorldPop population, and mapped OpenStreetMap features.

Compute:

- `event_window_days` as an inclusive day count.
- For ERA5-Land, GPM IMERG, and CHIRPS: event-total mean precipitation, event-total maximum precipitation, mean daily precipitation, `mean_ge_75mm`, and `max_ge_150mm`.
- `mean_score = mean(min(product_mean_total_mm / 100, 1))`.
- `max_score = mean(min(product_max_total_mm / 150, 1))`.
- `pass_share = (count(mean_total_mm >= 75) + count(max_total_mm >= 150)) / 6`.
- `rainfall_score = round(100 * (0.55 * mean_score + 0.35 * max_score + 0.10 * pass_share), 2)`.
- Surface-check ledger: `area_mean_passes = count(alpha_mean >= 0.10, dNBR_mean >= 0.10)`, `peak_passes = count(alpha_max >= 0.40, dNBR_max >= 0.50)`, and `surface_role = "peak_only_check"` when area-mean passes are zero and peak passes are positive.
- Mapped-feature ledger: count schools, hospitals, police sites, fire stations, buildings, residential roads, and compute `facility_rate_per_100k = (schools + hospitals + police + fire_stations) / (population / 100000)`.

Return compact JSON:

```json
{
  "event_window_days": 0,
  "precipitation_products": {
    "era5_land": {"mean_total_mm": 0.0, "max_total_mm": 0.0, "mean_daily_mm": 0.0, "mean_ge_75mm": false, "max_ge_150mm": false},
    "gpm_imerg": {"mean_total_mm": 0.0, "max_total_mm": 0.0, "mean_daily_mm": 0.0, "mean_ge_75mm": false, "max_ge_150mm": false},
    "chirps": {"mean_total_mm": 0.0, "max_total_mm": 0.0, "mean_daily_mm": 0.0, "mean_ge_75mm": false, "max_ge_150mm": false}
  },
  "rainfall_ledger": {
    "ensemble_mean_total_mm": 0.0,
    "ensemble_max_total_mm": 0.0,
    "mean_score": 0.0,
    "max_score": 0.0,
    "pass_share": 0.0,
    "rainfall_score": 0.0
  },
  "surface_check": {"area_mean_passes": 0, "peak_passes": 0, "surface_role": ""},
  "mapped_feature_ledger": {"facility_count": 0, "facility_rate_per_100k": 0.0},
  "final_label": ""
}
```

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

For this task, use that object to make the Cyclone Freddy ledger explain why rainfall dominates while surface change remains peak-only support.


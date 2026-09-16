# Final Answer

Canonical final label: `short_burst_multiday_urban_exposure`.

```json
{
  "event_window": {"start": "2021-07-17", "end": "2021-07-23", "days": 7},
  "reported_rainfall": {
    "three_day_mm": 617.1,
    "one_hour_mm": 201.9,
    "hour_share": 0.3272,
    "annual_ratio": 0.963
  },
  "gridded_accumulation": {
    "mean_order": ["gpm_imerg", "chirps", "era5_land"],
    "max_mean_dataset": "gpm_imerg",
    "max_mean_mm": 460.551,
    "max_grid_mm": 484.255
  },
  "exposure_context": {
    "population_million": 5.26,
    "highway_features": 252,
    "amenity_features": 48,
    "tunnel_features": 0
  },
  "threshold_flags": {
    "hour_share_ge_0_30": true,
    "annual_ratio_ge_0_90": true,
    "population_ge_5m": true,
    "highway_features_ge_200": true
  },
  "final_label": "short_burst_multiday_urban_exposure",
  "interpretation": "A 201.9 mm hour made up about one-third of the 617.1 mm multi-day total, while the event-window rain field and dense urban road context exceed the stated thresholds."
}
```

# Key Computations

The event window runs from 2021-07-17 through 2021-07-23, inclusive, so the window length is 7 days.

Reported rainfall anchors:

`hour_share = 201.9 / 617.1 = 0.3272`

`annual_ratio = 617.1 / 640.8 = 0.963`

Gridded event-window mean accumulation ranks as GPM IMERG first, CHIRPS second, and ERA5-Land third:

`460.551 mm > 245.924 mm > 217.454 mm`

The maximum gridded accumulation value is the GPM IMERG maximum:

`max_grid_mm = 484.255`

Urban context:

`population_million = 5262538.859 / 1000000 = 5.26`

The road and amenity record contains 252 highway-tagged features, 48 amenity-tagged features, and 0 tunnel-tagged features.

Threshold checks:

- `hour_share_ge_0_30`: `0.3272 >= 0.30`, true.
- `annual_ratio_ge_0_90`: `0.963 >= 0.90`, true.
- `population_ge_5m`: `5.26 >= 5.0`, true.
- `highway_features_ge_200`: `252 >= 200`, true.

# Reasoning Path

The reported 1-hour burst is not just a large standalone value: it contributes 32.72% of the 3-day Zhengzhou total. The 3-day total is also 96.3% of the city's reported annual average precipitation, so the short burst occurred inside a multi-day rainfall total that nearly matched a full year.

The gridded rainfall ledger supports the same event-window signal. Mean accumulation is ordered as GPM IMERG, CHIRPS, and ERA5-Land, with GPM IMERG highest at 460.551 mm and the largest grid value at 484.255 mm.

The urban context thresholds are also met: population is 5.26 million and the road/amenity record has 252 highway-tagged features, exceeding the 200-feature threshold. Since all four Boolean tests are true, the deterministic label is `short_burst_multiday_urban_exposure`.

# Computed Interpretation

The computed ledger supports a compact interpretation of Zhengzhou as a short-burst extreme embedded in a near-annual multi-day rainfall total over a densely populated urban road setting.

# Scoring Rubric

Total: 20 points.

- Output schema, 2 points: returns the requested compact JSON fields with units clear in field names and one concise interpretation sentence. Partial credit: 1 point if the answer has the final label and most numeric fields but omits or misnests one ledger block.
- Reported rainfall arithmetic, 4 points: gives 617.1 mm, 201.9 mm, `201.9 / 617.1 = 0.3272`, and `617.1 / 640.8 = 0.963` within tolerance. Partial credit: 2-3 points for correct rainfall anchors with one missing or rounded ratio; 1 point for only copying one or two rainfall values.
- Gridded accumulation ledger, 4 points: orders mean accumulation as GPM IMERG, CHIRPS, ERA5-Land; gives 460.551 mm for the top mean and 484.255 mm for the gridded maximum within tolerance. Partial credit: 2-3 points for the right top dataset with one numeric error; 1 point for recognizing GPM IMERG is largest without the ledger values.
- Urban context ledger, 3 points: gives 5.26 million people, 252 highway features, 48 amenity features, and 0 tunnel features within tolerance. Partial credit: 2 points for correct population and highway count with minor omissions; 1 point for only the population value.
- Threshold logic and final label, 5 points: correctly evaluates all four Boolean checks and assigns `short_burst_multiday_urban_exposure` only because all four are true. Partial credit: 3-4 points for the correct label with one threshold mistake; 1-2 points for correct individual checks but an incorrect or missing final label.
- Computed interpretation, 2 points: ties the one-hour share, near-annual multi-day total, gridded rainfall, and urban context into a concise computed interpretation. Partial credit: 1 point if the interpretation mentions only the rainfall thresholds or only the urban context.

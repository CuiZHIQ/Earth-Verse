# Final Answer

Canonical answer:

```json
{
  "classification": "persistent_high_elevation_snowpack",
  "point_grid_contrast_ratio": 97.9,
  "snowfall_run_hours": 49,
  "retained_depth_fraction": 0.44,
  "cold_wind_check": "30 h below 0 C; max gust 80.3 km/h; min wind chill -9.1 C",
  "image_check": "bright-white fraction 0.863 with low annual embedding-change mean 0.0207",
  "basis": "A 721.0 mm point snowfall depth is 97.9x the largest coarse-grid mean precipitation, and the 49 h run plus 0.32 m retained depth and cold-wind values favor a persistent high-elevation snowpack over a bright-scene-only reading."
}
```

# Key Computations

The calculation uses the event anchor, the Open-Meteo high-elevation weather point, ERA5-Land/GPM/CHIRPS event precipitation summaries, the NASA Worldview storm-window image, and the annual embedding-change summary.

Total point snowfall is `72.10 cm`, or `721.0 mm` and `0.721 m`. The gridded mean event precipitation values are `0.8007 mm` from ERA5-Land, `4.8940 mm` from GPM, and `7.3611 mm` from CHIRPS. The contrast ratio is therefore `721.0 / 7.3611 = 97.9`.

The longest continuous positive-snowfall run is `49 h`, from `2021-01-29T21:00` through `2021-01-31T21:00`. Maximum hourly snow depth is `0.32 m`, so retained depth fraction is `0.32 / 0.721 = 0.44`.

The cold-wind check is built from `30 h` below `0 C`, maximum gust `80.3 km/h`, and minimum wind chill `-9.1 C`. The image check combines bright-white fraction `0.863` with annual embedding-change mean `0.0207`.

# Reasoning Path

The point weather series is the controlling evidence because it measures snow accumulation and retained depth at `2710 m`. A brief bright-scene explanation would not produce a 49-hour snowfall run and a retained `0.32 m` snowpack. The coarse-grid precipitation means are useful as a contrast test: their low event means do not erase the point snowpack signal because they summarize broader pixels and liquid-depth fields.

The image evidence is kept in a supporting role. A high bright-white fraction is consistent with snow or cloud brightness during the storm window, while the low annual embedding-change mean argues against treating the image as a persistent land-surface change measurement.

# Computed Interpretation

The best short answer is `persistent_high_elevation_snowpack`. The decisive pattern is not a single bright image or a generic storm description; it is the joint numerical structure of high point snowfall, multi-day continuity, retained depth, later freezing, strong gusts, and a bright scene with low annual embedding change. These data do not establish exact road closure duration, animal losses, or regional snow depth away from the point.

# Scoring Rubric

Total: 20 points.

- Final JSON answer (3 points): Returns the requested fields and classifies the event as a persistent high-elevation snowpack signal. Partial credit: 1-2 points for the right diagnosis with incomplete fields.
- Point-grid contrast calculation (4 points): Converts `72.10 cm` to `721.0 mm`, uses the largest gridded mean precipitation `7.3611 mm`, and reports `97.9`. Partial credit: 1-3 points for a minor unit, product, or rounding error.
- Snow persistence and retained depth (4 points): Reports the `49 h` continuous snowfall run and computes retained depth fraction `0.44` from `0.32 / 0.721`. Partial credit: 1-3 points for getting only the run or only the fraction right.
- Cold-wind confirmation (3 points): Includes `30 h` below `0 C`, `80.3 km/h` maximum gust, and `-9.1 C` minimum wind chill. Partial credit: 1-2 points for two of the three metrics.
- Image and embedding check (3 points): Uses bright-white fraction `0.863` together with low annual embedding-change mean `0.0207`, and keeps the image evidence secondary to the snow time series. Partial credit: 1-2 points for using only one image metric or over-weighting image brightness.
- Data-reconciliation reasoning (2 points): Explains why coarse-grid precipitation and bright-scene evidence are contrast checks rather than the main snowpack measurement. Partial credit: 1 point for a correct but thin explanation.
- Concision and limits (1 point): Gives a compact answer and avoids converting the metrics into established loss, closure, or away-from-point snow-depth totals. Partial credit: 0.5 points for a mostly compact answer with one minor overreach.

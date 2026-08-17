# Antecedent Runoff Score Ledger

For the January 2023 California atmospheric-river sequence, compute an antecedent-runoff persistence score from the event data. Use the local daily precipitation series, three regional precipitation mean summaries, the paired pre-event and event RGB images, and the annual surface-change mean.

Definitions:

- `local_total_mm` is the sum of the local daily precipitation series with ISO-date `time` entries and `precipitation_sum` values; use the same series for `peak_day_mm`, `pre_peak_mm`, and `heavy_days_ge_50mm`.
- `peak_day_mm` is the maximum local daily precipitation.
- `pre_peak_mm` is the local precipitation total before the peak day.
- `antecedent_share = pre_peak_mm / local_total_mm`.
- `peak_share = peak_day_mm / local_total_mm`.
- `heavy_days_ge_50mm` is the count of local days with precipitation at least 50 mm.
- `regional_mean_mm` is the mean of the three regional precipitation means.
- `bright_change_to_annual_change_ratio = (event_bright_fraction - pre_event_bright_fraction) / annual_surface_change_mean`, where a bright pixel has mean RGB at least 200. Compute the ratio from unrounded bright fractions and unrounded annual mean, then round only the final ratio.
- `arps = 100 * (0.35 * min(local_total_mm / 600, 1) + 0.25 * min(heavy_days_ge_50mm / 6, 1) + 0.25 * antecedent_share + 0.15 * min(regional_mean_mm / 250, 1))`.

Round millimeter values to 1 decimal, shares to 4 decimals, ratios to 2 decimals, and `arps` to 1 decimal.

Return one concise JSON object with exactly these fields:

```json
{
  "score_label": "<short label>",
  "local_total_mm": 0.0,
  "heavy_days_ge_50mm": 0,
  "pre_peak_mm": 0.0,
  "peak_day_mm": 0.0,
  "antecedent_share": 0.0,
  "peak_share": 0.0,
  "pre_peak_to_peak_ratio": 0.0,
  "regional_mean_mm": 0.0,
  "bright_change_to_annual_change_ratio": 0.0,
  "arps": 0.0
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

For this task, use that object to explain why antecedent accumulation and regional wetness dominate the runoff diagnosis rather than the single peak day or the RGB image contrast alone.


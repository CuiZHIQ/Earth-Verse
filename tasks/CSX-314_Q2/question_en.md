# Chamoli Source-Class Consistency Ledger

Compute a compact source-class consistency ledger for the 2021 Chamoli rock-ice avalanche and flood. Use the event-day precipitation summaries, the paired radar and optical pre/post terrain-change summaries, the annual embedding summary, and the point-weather sample with the compact event polygon.

Apply these deterministic rules:

- `max_precip_mm`: maximum event-day precipitation across all precipitation summaries, rounded to 4 decimals.
- `dry_source_count`: number of event-day precipitation summaries with precipitation `<= 0.01 mm`.
- `prepost_obs`: total pre plus post observation count across the paired radar and optical terrain-change summaries.
- `radar_abs_db`: maximum absolute radar VV post-minus-pre change in dB, rounded to 4 decimals.
- `optical_abs`: maximum absolute optical dNBR change, rounded to 4 decimals.
- `annual_span_yr`: annual embedding `post_year - pre_year`.
- `point_in_bbox`: whether the point-weather sample coordinate is inside the compact event polygon bounding box.
- `answer`: return `mass_movement_source_supported` only when `max_precip_mm < 10`, every precipitation summary is dry by the `0.01 mm` rule, `prepost_obs >= 200`, `radar_abs_db >= 10`, `optical_abs >= 0.5`, `annual_span_yr >= 1`, and `point_in_bbox` is `false`; otherwise return `rain_runoff_supported` if the rainfall threshold is met, or `indeterminate`.

Return only compact JSON with these eight fields:

```json
{
  "answer": "<label>",
  "max_precip_mm": 0.0,
  "dry_source_count": 0,
  "prepost_obs": 0,
  "radar_abs_db": 0.0,
  "optical_abs": 0.0,
  "annual_span_yr": 0,
  "point_in_bbox": false
}
```

# Barren Island Ash-Plume Gate Consistency Calculation

For the September 2010 Barren Island ash-plume event in the Andaman Sea, compute a deterministic rain/change-map gate. The gate tests whether same-window rain context and surface-change availability are strong enough to displace the report-level ash-plume anchor.

Use these formulas:

- `date_offset_days = report_image_date - locked_event_start_date`
- `point_precip_mean_mm = mean(the two locked-day point precipitation estimates)`
- `regional_peak_precip_mm = max(the three locked-day gridded regional precipitation maxima)`
- `peak_to_point_ratio = regional_peak_precip_mm / point_precip_mean_mm`
- `change_scene_total = radar_pre_count + radar_post_count + optical_pre_count + optical_post_count`
- `rain_change_gate_score = count(point_precip_mean_mm >= 25, regional_peak_precip_mm >= 100, date_offset_days <= 3, change_scene_total >= 1)`

Classify the event as `rain_or_change_context_controls` only when `rain_change_gate_score >= 3`; otherwise classify it as `source_proximal_ash_anchor_controls`.

Return compact JSON:

```json
{
  "answer": {
    "date_offset_days": 0,
    "point_precip_mean_mm": 0.0,
    "regional_peak_precip_mm": 0.0,
    "peak_to_point_ratio": 0.0,
    "change_scene_total": 0,
    "rain_change_gate_score": 0,
    "classification": ""
  },
  "interpretation": "<one short computed consequence>"
}
```

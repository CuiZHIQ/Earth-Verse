# Poyang Heat-Drought Lake Response and Low-Water Scenario Model

Use only the local event package for CSX-015. Select package-relative evidence for every value, timeline claim, and qualitative process link you use. Keep report evidence as concise paraphrased claim labels rather than long quotations.

Build a professional disaster-science JSON answer that reconstructs how prolonged heat stress and an incomplete late-summer precipitation record relate to the reported Poyang Lake drop, then evaluates a hotter continued-low-water scenario for emergency response planning.

Your answer must:

1. Establish the event window and the Poyang Lake hydrologic timeline from package reports.
2. Compute the longest local heat-stress sequence relevant to the late-August low-water stage.
3. Compare independent precipitation summaries and determine how far their shared window falls short of the lake-level dates.
4. Use remote-sensing mean-change statistics to decide whether package-level surface-change evidence is strong or weak at AOI scale.
5. Summarize AOI population and road/service exposure, while treating any large spatial mismatch as a planning uncertainty rather than as a direct lake-impact population count.
6. Run the specified future scenario: all daily maximum, minimum, and apparent temperatures in the late lake-drop window are increased by 2.0 C, and the observed mean lake-level drop rate continues for 10 additional days after the last reported lake level.
7. Prioritize response actions from the computed physical stress, exposure/service load, and uncertainty.

Use these definitions and rounding rules:

- Late lake-drop window: from the report date when the lake entered dry-season level conditions through the last reported lake-level date.
- In precipitation evidence, compute `precip_product_mean_spread_mm` as the GPM event-window mean minus the CHIRPS event-window mean, while still reporting the ERA5-Land mean as a third comparison product.
- Compute `hot_night_fraction` as `hot_night_count / late_lake_drop_window_days`, using the same late lake-drop window as the heat-stress sequence.
- Treat the lake-level span as the report-supported interval from the dry-season-level date to the last reported lake level; the image span is a separate context interval and should not replace the level-drop span.
- `heat_persistence_index = 100 * (0.40 * min(longest_Tmax35_days / 21, 1) + 0.25 * min(Tmax35_excess_C_day / 30, 1) + 0.20 * hot_night_fraction + 0.15 * min(apparent40_excess_C_day / 40, 1))`.
- `lake_drop_index = 100 * (0.45 * min(drop_rate_cm_per_day / 15, 1) + 0.35 * min(drop_percent / 30, 1) + 0.20 * min(early_dry_season_days / 120, 1))`.
- `late_precip_gap_index = 100 * (0.50 * min(gap_to_last_lake_level_days / 45, 1) + 0.30 * min(gap_to_lake_image_days / 45, 1) + 0.20 * min(precip_product_mean_spread_mm / 150, 1))`.
- `remote_mean_change_index = 100 * (0.50 * min(mean_dNBR / 0.05, 1) + 0.50 * min(mean_embedding_change / 0.05, 1))`.
- Count critical services from the bounded AOI road/service exposure file as hospitals, police stations, fire stations, and shelters. Count major road ways as primary, secondary, trunk, and motorway ways. Count bridge ways from `bridge` tags.
- `exposure_service_index = 100 * (0.45 * min(population / 2500000, 1) + 0.25 * min(critical_service_count / 75, 1) + 0.20 * min(major_road_way_count / 175, 1) + 0.10 * min(bridge_way_count / 30, 1))`.
- `response_priority_score = 0.35 * heat_persistence_index + 0.30 * lake_drop_index + 0.15 * late_precip_gap_index + 0.20 * exposure_service_index`.
- Use the same formulas for the +2.0 C and 10-day continued-drop scenario, replacing heat and lake-drop values with scenario values while keeping precipitation-gap and AOI exposure terms unchanged.
- Round temperatures and heat loads to 1 decimal, fractions and ratios to 3 decimals, water levels and drops to 2 decimals, rates to 3 decimals or 1 decimal for cm/day, distances to 1 decimal, indices and priority scores to 1 decimal, and remote-sensing means to 6 decimals.

Return exactly one JSON object with this schema:

```json
{
  "answer_type": "poyang_heat_drought_lake_response_model",
  "source_paths": {
    "event_window": "path",
    "lake_report": "path",
    "heat_series": "path",
    "precipitation_products": ["path"],
    "remote_change_products": ["path"],
    "aoi_geometry": "path",
    "population": "path",
    "road_service_exposure": "path"
  },
  "process_model": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "lake_timeline": {},
    "heat_stress": {},
    "precipitation_evidence": {},
    "remote_sensing_change": {},
    "spatial_exposure_context": {}
  },
  "computed_metrics": {
    "heat_persistence_index": 0.0,
    "lake_drop_index": 0.0,
    "late_precip_gap_index": 0.0,
    "remote_mean_change_index": 0.0,
    "exposure_service_index": 0.0,
    "response_priority_score": 0.0
  },
  "scenario_analysis": {
    "scenario_name": "plus_2C_and_10_day_continued_drop",
    "heat_stress": {},
    "lake_timeline": {},
    "computed_metrics": {},
    "deltas_from_baseline": {}
  },
  "response_priorities": [
    {
      "rank": 1,
      "priority": "short_action_label",
      "trigger_metrics": ["metric_name"],
      "rationale": "one_sentence"
    }
  ],
  "mechanism_chain": [
    "short package-grounded process step"
  ],
  "final_interpretation": "one concise package-grounded conclusion"
}
```

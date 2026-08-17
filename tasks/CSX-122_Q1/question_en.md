# Cyclone Freddy Late-Phase Rainfall Ledger

A hydrometeorology team is closing a technical note on Cyclone Freddy across Madagascar, Mozambique, and Malawi during February-March 2023. The unresolved question is whether the final southern Africa phase is best summarized by accumulated rainfall, wind intensity, track persistence with exposed settlements, or image-visible landscape change.

Give a compact, event-specific diagnostic ledger. Use quantitative anchors from the incident record, compare the closest competing reading, and explain how image or exposure context should be handled without converting broad context into direct proof of inundation or damage.

Return only this JSON object:

```json
{
  "answer": "<compact signal label>",
  "diagnostic_class": "<high|moderate|low>",
  "numeric_anchors": {
    "event_total_point_rain_mm": <number>,
    "late_phase_point_rain_mm": <number>,
    "gridded_rainfall_mean_mm": <number>,
    "exposed_population_context": <number>
  },
  "derived_tests": {
    "late_phase_share_of_event_point_rain": <number>,
    "gridded_mean_to_late_point_rain_ratio": <number>
  },
  "structured_findings": {
    "dominant_signal": "<one-sentence diagnostic finding>",
    "closest_alternative": "<closest competing reading and why the ledger gives it less weight>",
    "timing_test": "<how the late dates affect the finding>",
    "rainfall_test": "<how the rainfall numbers support the finding>",
    "imagery_or_exposure_context": "<how imagery or exposure context affects the diagnosis>"
  }
}
```

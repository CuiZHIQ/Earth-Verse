# Rainfall Concentration Ratio

A hydrology review team is checking the late July to early August 2023 flood episode linked to Typhoon Doksuri's remnants across Beijing, Hebei, Tianjin, and the Haihe basin. The question is whether the reported local storm maximum was only a wet-period accumulation or a much sharper extreme-rainfall anchor than the nearby event-window point series.

Compute the reported local storm rainfall total, the summed point rainfall total for the event window, and the ratio of the reported total to the point-window total. Classify the result using this rule: if the ratio is at least 3.0, label it as a spatially concentrated extreme local maximum; otherwise label it as comparable to the point-window total.

Return a compact JSON object with these fields:

```json
{
  "reported_storm_total_mm": "...",
  "point_event_total_mm": "...",
  "reported_to_point_ratio": "...",
  "concentration_class": "...",
  "computed_interpretation": "..."
}
```

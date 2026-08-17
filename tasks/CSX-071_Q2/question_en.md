# Ida Rainfall Partition Numeric Diagnosis

A hydrometeorology team is checking a proposed quantitative diagnosis for Post-Tropical Cyclone Ida's September 1-2, 2021 Northeast flooding. The question is whether the diagnosis preserves both the New York City record-hour burst and the broader northern Mid-Atlantic storm-total accumulation, rather than substituting one rainfall measure for the other.

Compute a compact JSON answer with these fields:

```json
{
  "target_family": "rainfall_partition_numeric_diagnosis",
  "event_window": "YYYY-MM-DD to YYYY-MM-DD",
  "city_hour_mm": 0.0,
  "regional_lower_bound_mm": 0.0,
  "city_hour_share": 0.0,
  "regional_minus_city_hour_mm": 0.0,
  "gridded_max_mm": 0.0,
  "gridded_max_to_regional_lower_bound": 0.0,
  "final_label": "<short label>"
}
```

Use inches-to-millimeters conversion, the stated record-hour rainfall, the stated regional storm-total lower bound, and the maximum event accumulation among the gridded precipitation summaries. Round rainfall depths to three decimals and ratios to three decimals. The final label should state whether the numbers support a combined hourly-burst plus larger storm-total accumulation diagnosis.

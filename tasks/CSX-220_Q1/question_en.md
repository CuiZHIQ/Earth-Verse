# Gjerdrum Quick-Clay Landslide Numeric Diagnosis

On 30 December 2020, a rapid quick-clay landslide struck Ask in Gjerdrum, Norway. A geohazard review team needs a compact numeric diagnosis that tests whether the record supports a large-footprint, wet-context, radar-dominant surface-change interpretation.

Return exactly one JSON object with these top-level keys:

```json
{
  "mechanism_label": "string",
  "footprint": {
    "runout_width_m": number,
    "runout_length_m": number,
    "rectangle_area_ha": number,
    "debris_flow_area_ha": number
  },
  "rainfall": {
    "antecedent_5_day_precip_mm": number,
    "event_day_precip_mm": number,
    "wetness_index_mm_day": number,
    "event_day_fraction": number
  },
  "change_signal": {
    "radar_abs_mean": number,
    "optical_abs_mean": number,
    "embedding_mean": number,
    "dominant_mean_signal": "string",
    "radar_to_optical_ratio": number
  },
  "exposure_context": {
    "population_sum_rounded": number,
    "population_millions": number
  },
  "diagnosis_label": "string"
}
```

Use the five-day rainfall window from 2020-12-26 through 2020-12-30. Compute `wetness_index_mm_day` as the five-day precipitation total divided by 5, and compute `event_day_fraction` as event-day precipitation divided by the five-day total. Compute `rectangle_area_ha` as width times length divided by 10,000. Round rainfall totals to 1 decimal, `wetness_index_mm_day` to 2 decimals, `event_day_fraction` to 4 decimals, mean-change values to 4 decimals, `radar_to_optical_ratio` to 3 decimals, and population in millions to 3 decimals.

For `dominant_mean_signal`, use the largest of the three mean-change magnitudes; the embedding value is already nonnegative and should be treated as coarse annual surface-change context rather than event-timed proof. Keep `diagnosis_label` as a short machine-readable label, and do not treat rainfall as a proven trigger or population exposure as confirmed losses.

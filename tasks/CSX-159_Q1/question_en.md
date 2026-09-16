# Koror Rainfall-Deficit Water Balance

A hydrology team in Koror, Palau is preparing a numeric drought balance note for the 2015-2016 El Nino dry spell. The team needs to decide whether the January 1-April 20, 2016 report-effective rainfall record supports a persistent rainfall-deficit water-supply drought, rather than a brief local shower miss.

Compute the drought water-balance ledger from the Koror rainfall record. Convert inches to millimeters with `1 inch = 25.4 mm`.

Use these definitions:

```text
window_days = inclusive days from event start through event end
normal_rain_inches = observed_rain_inches + below_average_inches
observed_fraction = observed_rain_inches / normal_rain_inches
deficit_index = below_average_inches / normal_rain_inches
stress_score = deficit_index * min(window_days / 90, 1) * min(record_low_years / 50, 1)
```

Classify the result as `extreme_persistent_rainfall_deficit_water_supply_drought` only if all four tests pass:

```text
window_days >= 90
observed_fraction <= 0.30
deficit_index >= 0.70
record_low_years >= 50
```

Return a compact JSON object with exactly these six top-level fields:

```json
{
  "answer": "<classification label>",
  "window_days": 0,
  "rainfall_ledger_mm": {
    "observed": 0.0,
    "deficit": 0.0,
    "inferred_normal": 0.0
  },
  "rates_mm_day": {
    "observed": 0.0,
    "deficit": 0.0,
    "inferred_normal": 0.0
  },
  "indices": {
    "observed_fraction": 0.0,
    "deficit_index": 0.0,
    "stress_score": 0.0
  },
  "threshold_result": {
    "duration_ge_90": true,
    "observed_fraction_le_0_30": true,
    "deficit_index_ge_0_70": true,
    "record_years_ge_50": true,
    "interpretation": "<one sentence tied to the numbers>"
  }
}
```

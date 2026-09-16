# Correct Answer

```json
{
  "event_time_utc": "2024-01-01T07:10:09.476Z",
  "source_intensity_score": 6,
  "coastal_ground_score": 5,
  "context_score": 3,
  "countercheck_penalty": 0,
  "final_score": 14,
  "consistency_class": "high_seismic_coastal"
}
```

# Computation

The recorded event time is 2024-01-01T07:10:09.476Z. The source and shaking values are Mw 7.5, depth 10.0 km, maximum MMI 8.8, and red event alert, so `source_intensity_score = 2 + 2 + 1 + 1 = 6`.

The coastal and ground-failure values are tsunami flag 1, liquefaction population exposure 710,000, and landslide population exposure 3,800. The exposure ratio is `710000 / 3800 = 186.842`, so `coastal_ground_score = 2 + 2 + 1 = 5`.

The context values are exposed-area population 10,066,670, finite-fault length 175.0 km, and maximum slip 6.03 m, so `context_score = 1 + 1 + 1 = 3`.

The counterchecks do not subtract points: the larger mean precipitation value is 0.349 mm, the absolute mean Sentinel-1 VV change is 1.772 dB, and the mean annual embedding change is 0.026. These are below the 25 mm, 5 dB, and 0.10 thresholds, so `countercheck_penalty = 0`.

The final score is `6 + 5 + 3 - 0 = 14`. Because 14 is at least 11, the class is `high_seismic_coastal`.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested JSON fields with numeric values and the UTC event time.
- 4 points: Computes `source_intensity_score` correctly from Mw 7.5, maximum MMI 8.8, depth 10.0 km, and red event alert.
- 4 points: Computes `coastal_ground_score` correctly from tsunami flag 1, liquefaction exposure 710,000, landslide exposure 3,800, and the ratio 186.842.
- 3 points: Computes `context_score` correctly from population 10,066,670, finite-fault length 175.0 km, and maximum slip 6.03 m.
- 3 points: Applies the precipitation and surface-change counterchecks correctly, yielding zero penalty.
- 2 points: Computes `final_score = 14` and assigns `high_seismic_coastal`.
- 1 point: Does not infer exact casualty totals, damage totals, measured local inundation height, or rainfall causation from these ledger values.

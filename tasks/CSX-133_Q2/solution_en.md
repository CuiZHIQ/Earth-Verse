# Final Answer

`compound_typhoon_passage_consistent`

```json
{
  "metrics": {
    "catalog_peak_wind_kmh": 240.7,
    "local_peak_gust_kmh": 116.6,
    "gust_energy_proxy_kmh2_per_1000": 13.6,
    "pressure_drop_hpa": 28.0,
    "event_precip_mm": 165.3,
    "wettest_24h_mm": 120.3,
    "rainfall_concentration_24h": 0.728,
    "peak_sync_lag_hours": 1
  },
  "threshold_tests": {
    "wind": true,
    "pressure": true,
    "rain_concentration": true,
    "timing": true
  },
  "conclusion": "compound_typhoon_passage_consistent",
  "rejected_alternative": "single_driver_wind_or_rain",
  "proof": "The point record passes all four tests: 116.6 km/h >= 90 km/h, 28.0 hPa >= 20 hPa, 120.3/165.3 = 0.728 >= 0.70, and the peak gust, minimum pressure, and wettest hour are within 1 hour. Because wind, pressure fall, and concentrated rainfall pass together, a wind-only or rain-only diagnosis is rejected."
}
```

# Key Computations

Total event precipitation is the sum of hourly precipitation, 165.3 mm. The maximum rolling 24-hour precipitation is 120.3 mm, giving `rainfall_concentration_24h = 120.3 / 165.3 = 0.728`.

The local peak gust is 116.6 km/h, so `gust_energy_proxy_kmh2_per_1000 = 116.6^2 / 1000 = 13.6`. Sea-level pressure ranges from 1010.0 hPa to 982.0 hPa, so `pressure_drop_hpa = 28.0`.

The local peak gust occurs at 2024-09-07T12:00, while both the minimum pressure and wettest hour occur at 2024-09-07T13:00. The largest separation among those extrema is therefore 1 hour, which satisfies the timing rule.

# Reasoning Path

The wind test passes because 116.6 km/h is greater than the 90 km/h threshold. The pressure test passes because the 28.0 hPa drop is greater than the 20 hPa threshold. The rainfall concentration test passes because the wettest 24 hours contain 120.3 mm of 165.3 mm total rainfall, so `0.728 >= 0.70`. The timing test passes because the peak gust, pressure minimum, and wettest hour are all within a maximum separation of 1 hour.

Since all four required tests are true, the conclusion is `compound_typhoon_passage_consistent`. A single wind or rain driver is rejected by the ledger because neither wind nor rainfall is acting alone in the threshold proof.

# Computed Interpretation

The local record shows a tightly timed burst of damaging gust, pressure fall, and concentrated rainfall, so the compact event label should be a compound typhoon passage rather than a one-driver reading.

# Scoring Rubric

Total: 20 points.

- 4 points: Returns the requested five-key JSON structure and the exact conclusion label `compound_typhoon_passage_consistent`. Partial credit: 2-3 points for a mostly complete structure with the right conclusion in the wrong place.
- 5 points: Correctly computes the numeric ledger within tolerance: 240.7 km/h catalog wind, 116.6 km/h local gust, 13.6 gust-energy proxy, 28.0 hPa pressure drop, 165.3 mm total precipitation, 120.3 mm wettest 24-hour precipitation, 0.728 concentration ratio, and 1 hour timing lag. Partial credit: award by metric family when units and formulas are recognizable.
- 4 points: Shows or applies the required formulas for rolling 24-hour precipitation, concentration ratio, gust-energy proxy, pressure drop, and peak-time lag. Partial credit: award up to 4 points for correctly applied formula families.
- 3 points: Applies all four threshold tests correctly: wind, pressure, rain concentration, and timing are all true. Partial credit: 1-2 points for mostly correct inequality logic with one missing or misclassified test.
- 2 points: Rejects the single wind or rain reading because wind, pressure fall, and concentrated rainfall pass together. Partial credit: 1 point for rejecting a one-driver reading without tying it to the full ledger.
- 1 point: Gives a concise computed interpretation consistent with the coupled passage proof. Partial credit: 0.5 point for a correct but wordy interpretation.
- 1 point: Avoids unjustified exact loss, outage, road-closure, or flood-depth claims. Partial credit: 0.5 point if such claims are clearly secondary and do not drive the answer.

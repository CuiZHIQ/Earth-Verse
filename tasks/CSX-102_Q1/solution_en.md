# Final Answer

```json
{
  "event_window_days": 36,
  "event_window_hours": 864,
  "core_metrics": {
    "monthly_anomaly": {
      "july_percent_above_normal": 70,
      "august_percent_above_normal": 102,
      "august_to_july_ratio": 1.457,
      "mean_percent_above_normal": 86.0
    },
    "precipitation_products": {
      "gpm_mean_event_precip_mm": 218.227,
      "chirps_mean_event_precip_mm": 230.084,
      "chirps_minus_gpm_mm": 11.858,
      "chirps_to_gpm_ratio": 1.054
    },
    "hourly_point_timing_evidence": {
      "hour_count": 864,
      "precipitation_sum_mm": 347.8,
      "wet_hours": 204,
      "wet_hour_share": 0.236,
      "wet_hour_mean_mm": 1.705,
      "max_hour_share_of_sum": 0.04
    },
    "impact_normalization": {
      "scope": "national lower-bound report context, not an exact point-window impact total",
      "minimum_flooded_extent_sq_km": 37280,
      "affected_people_lower_bound": 18000000,
      "affected_people_per_flooded_sq_km": 482.833,
      "deaths_per_1000_affected": 0.11,
      "houses_per_affected_person": 0.0944
    },
    "catalog": {
      "start_date": "2010-07-27",
      "alert_level": "RED",
      "severity": 7.46
    }
  },
  "final_label": "persistent_monsoon_basin_flood_signal_consistent",
  "tests": {
    "monthly_anomaly_persistence": "pass",
    "precipitation_product_agreement": "pass",
    "wet_hour_persistence": "pass",
    "basin_scale_impact_magnitude": "pass",
    "catalog_severity_alignment": "pass"
  },
  "basis": "All five checks pass: July and August rainfall were 70% and 102% above normal, CHIRPS/GPM is 1.054, 204 wet hours occurred in the 864-hour window, reported flood extent and affected population exceed the magnitude thresholds, and the catalog entry begins on 2010-07-27 with RED alert and severity 7.46."
}
```

# Key Computations

The inclusive window from 2010-07-27 through 2010-08-31 is 36 days, or 864 hours.

Monthly rainfall anomalies are 70 percent above normal in July and 102 percent above normal in August. The August/July anomaly ratio is `102 / 70 = 1.457`, and the mean anomaly is `(70 + 102) / 2 = 86.0` percent above normal.

GPM event mean precipitation is 218.227 mm and CHIRPS event mean precipitation is 230.084 mm. Their difference is `230.084 - 218.227 = 11.858` mm, and their ratio is `230.084 / 218.227 = 1.054`.

The hourly point series totals 347.8 mm over 864 hours. This equals 9.661 mm/day and 0.403 mm/hour. It has 204 wet hours, so the wet-hour share is `204 / 864 = 0.236`; the wet-hour mean is `347.8 / 204 = 1.705` mm; and the maximum-hour share is `13.9 / 347.8 = 0.040`. This is point-series timing evidence for persistence, not a basin-wide wet-area fraction.

Reported flood extent is at least 37,280 square kilometers and affected population is at least 18,000,000 people. These are national lower-bound report-context values, not exact impacts confined to the point-weather window. The impact normalizations are `18,000,000 / 37,280 = 482.833` affected people per flooded square kilometer, `1,985 / 18,000,000 * 1000 = 0.110` deaths per 1,000 affected people, and `1,700,000 / 18,000,000 = 0.0944` houses per affected person.

The catalog row is Pakistan, starts on 2010-07-27, has RED alert level, and has severity 7.46.

# Reasoning Path

The anomaly test passes because both 70 percent and 102 percent exceed the 50 percent monthly threshold, and their 86.0 percent mean exceeds the 75 percent persistence threshold. This argues against treating the event as a single brief burst.

The precipitation product test passes because the CHIRPS/GPM ratio is 1.054, inside the 0.9-1.1 agreement band. The wet-hour test also passes because 204 wet hours exceed the 150-hour threshold, and the maximum hour contributes only 4.0 percent of the event sum.

The magnitude test passes because 37,280 square kilometers exceeds 30,000 square kilometers and 18 million affected people exceeds 10 million. The catalog test passes because the start date, RED alert level, and 7.46 severity satisfy the stated rule.

Together, the checks form a consistency proof: persistent monthly anomalies, cross-product precipitation agreement, many wet hours, broad reported flood magnitude, and catalog severity all point to the same final label.

# Computed Interpretation

The computed record is best summarized as a persistent monsoon-driven Indus basin flood signal, with the point rainfall series acting as supporting timing evidence rather than the whole basin total.

# Scoring Rubric

- 3 points: Correct final answer and JSON shape. Full credit gives `persistent_monsoon_basin_flood_signal_consistent`, the window fields, five test states, core metrics, and one basis sentence. Partial credit is available for the correct label with minor missing fields, or for a complete structure with one mislabeled test.
- 4 points: Correct event-window and anomaly computations. Full credit includes 36 days, 864 hours, 70 percent, 102 percent, 1.457 ratio, and 86.0 percent mean anomaly. Partial credit is available for correct anomalies but an incorrect inclusive-window count, or for correct window values with one rounded anomaly derivative outside tolerance.
- 4 points: Correct precipitation product and hourly-series calculations. Full credit includes 218.227 mm, 230.084 mm, 11.858 mm, 1.054 ratio, 347.8 mm, 204 wet hours, 0.236 wet-hour share, 1.705 mm wet-hour mean, and 0.040 maximum-hour share. Partial credit is available when the product comparison is correct but one hourly derivative is missing or rounded poorly.
- 3 points: Correct impact normalization. Full credit includes 37,280 square kilometers, 18,000,000 affected people, 482.833 affected people per flooded square kilometer, 0.110 deaths per 1,000 affected, and 0.0944 houses per affected person. Partial credit is available for using the right formulas with one denominator or unit mistake.
- 3 points: Correct threshold logic. Full credit marks all five tests as pass and explains why each satisfies its rule. Partial credit is available when the final label is right but one threshold is omitted or one pass/fail state is wrong.
- 2 points: Correct reasoning against a short isolated burst. Full credit ties the rejection to persistent monthly anomalies, 204 wet hours, and the 4.0 percent maximum-hour share. Partial credit is available for mentioning persistence without at least two numeric anchors.
- 1 point: Concise calculation-first wording. Full credit avoids broad narrative beyond what the computed values support. Partial credit is available for a verbose answer that still keeps the numeric proof recoverable.

# Correct Answer

```json
{
  "answer": {
    "radar_margin_db": 1.89,
    "dnbr_margin": 0.057,
    "dnbr_mean_to_max": 0.052,
    "precip_3source_mean_mm": 166.4,
    "warm_wet_score": 2,
    "ledger_score": 5,
    "classification": "radar_led_surface_change_with_warm_wet_loading"
  },
  "interpretation": "5/5 ledger supports strong VV change with weak area-mean dNBR and warm-wet loading."
}
```

# Computation

The mean VV post-minus-pre change is 3.887 dB, so `radar_margin_db = abs(3.887) - 2.0 = 1.887`, rounded to 1.89.

The mean dNBR is 0.0426 and max dNBR is 0.8234, so `dnbr_margin = 0.10 - abs(0.0426) = 0.0574`, rounded to 0.057, and `dnbr_mean_to_max = abs(0.0426) / 0.8234 = 0.0517`, rounded to 0.052.

The three event-accumulated precipitation means are 120.5 mm, 141.7 mm, and 237.1 mm. Their mean is 166.4 mm. This clears the 100 mm precipitation threshold, and the mean daily maximum temperature of 34.7 C clears the 30 C threshold, so `warm_wet_score = 2`.

All three surface tests pass, and both warm-wet tests pass, giving `ledger_score = 5`. The compact classification is `radar_led_surface_change_with_warm_wet_loading`.

# Scoring Rubric

- 3 points: JSON schema is complete, with all requested numeric fields and the final classification string. Partial credit: 2 points for all numeric fields but missing the classification; 1 point for parseable but incomplete JSON.
- 4 points: Uses the correct input values for VV mean change, dNBR mean and max, three precipitation means, and mean daily maximum temperature. Partial credit: 0.5 point for each correct extracted input value, up to 4 points.
- 5 points: Computes `radar_margin_db = 1.89`, `dnbr_margin = 0.057`, and `dnbr_mean_to_max = 0.052` within tolerance. Partial credit: up to 1.5 points for each correct surface value and 0.5 point for correct formulas.
- 3 points: Computes `precip_3source_mean_mm = 166.4` and `warm_wet_score = 2`. Partial credit: 2 points for the precipitation mean only; 1 point for the temperature threshold only.
- 3 points: Combines the three surface passes and two warm-wet passes into `ledger_score = 5` and the expected classification. Partial credit: 2 points for the correct ledger score without the exact classification; 1 point for the right pass-count logic with an arithmetic error.
- 2 points: Gives a concise interpretation tied to the computed ledger without adding casualty, damage, or direct runout assertions. Partial credit: 1 point for a concise interpretation with one uncomputed extra assertion.

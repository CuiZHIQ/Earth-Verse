# Final Answer

```json
{
  "psi_ratio_min": 5.714,
  "surface_co_ratio": 13.0,
  "aerosol_factor": 6,
  "max_vertical_signal_km": 9,
  "dry_day_shares": {
    "open_meteo": 0.391,
    "nasa_power": 0.326
  },
  "dnbr_pre_post_counts": [0, 0],
  "candidate_scores": {
    "peat_smoke": 6,
    "rainfall_only": 1,
    "burn_scar": 0
  },
  "final_label": "peat_smoke_haze_pass"
}
```

# Key Computations

The local report gives PSI above 2000 and a hazardous threshold of 350, so `psi_ratio_min = 2000 / 350 = 5.714`.

The same report gives near-surface carbon monoxide up to nearly 1300 ppb against a usual value of about 100 ppb, so `surface_co_ratio = 1300 / 100 = 13.0`.

It reports a 6-fold particle increase at Palangkaraya. Vertical signals are 2 km smoke from CALIPSO, about 5 km carbon monoxide from AIRS, and above 9 km carbon monoxide from MLS, so `max_vertical_signal_km = 9`.

The daily-weather windows run from 2015-08-01 to 2015-09-15 in both local daily products. Open-Meteo has 18 days below 1 mm out of 46 days, so `18 / 46 = 0.391`. NASA POWER has 15 days below 1 mm out of 46 days, so `15 / 46 = 0.326`.

The dNBR summary has `pre_count = 0` and `post_count = 0`. The report also states peat fires release 3 times as much carbon monoxide and 10 times as much methane as savanna or grassland fires.

# Reasoning Path

The peat-smoke ledger has six tests. The dry-day test passes because both dry-day shares are at least 0.30. The peat-emission multiplier test passes because the carbon-monoxide and methane multipliers meet the 3 and 10 thresholds. The PSI test passes because 5.714 is at least 5, and the near-surface carbon-monoxide test passes because 13.0 is at least 10. The aerosol test passes because the particle factor is 6, and the vertical-signal test passes because the maximum reported height is 9 km.

The peat-smoke score is therefore 6. The rainfall-only score is 1 because it receives only the dry-day point. The burn-scar score is 0 because both dNBR scene counts are zero. Since the peat-smoke score is 6 and the other two scores are lower, the final label is `peat_smoke_haze_pass`.

# Computed Interpretation

The ledger is dominated by smoke chemistry, particle loading, and vertical transport values; the dry-window numbers are supporting context, while the dNBR scene count does not produce a burn-scar score.

# Scoring Rubric

Total: 20 points

- 3 points: Final compact ledger and label. Full credit gives the requested JSON with `final_label` equal to `peat_smoke_haze_pass` and the three candidate scores equal to 6, 1, and 0. Partial credit gives 1-2 points for a correct label with incomplete scores or correct scores with a missing label.
- 4 points: PSI and near-surface carbon-monoxide ratios. Full credit computes `2000 / 350 = 5.714` and `1300 / 100 = 13.0` with correct rounding and units understood from field names. Partial credit gives 1-3 points for one correct ratio, small rounding errors, or values listed without the division logic.
- 3 points: Aerosol and vertical-signal values. Full credit reports the 6-fold particle factor and uses the maximum of 2, 5, and 9 km as `max_vertical_signal_km = 9`. Partial credit gives 1-2 points for one correct value or for using a lower listed height while showing the right source values.
- 4 points: Dry-window and peat-emission tests. Full credit computes `18 / 46 = 0.391`, `15 / 46 = 0.326`, and applies the peat carbon-monoxide and methane multiplier thresholds of 3 and 10. Partial credit gives 1-3 points for correct dry-day counts but wrong shares, one weather product only, or multiplier values without the pass test.
- 3 points: Candidate-score arithmetic. Full credit assigns six peat-smoke points, one rainfall-only point, and zero burn-scar points according to the stated rules. Partial credit gives 1-2 points for applying most tests but miscounting one candidate score.
- 2 points: dNBR count handling. Full credit reports `[0, 0]` and uses those counts to give the burn-scar candidate zero points. Partial credit gives 1 point for listing the counts without applying the burn-scar scoring rule.
- 1 point: Answer discipline. Full credit returns only the compact JSON object and avoids adding legal culpability, exact ignition-site claims, casualty estimates, or other quantities not produced by the ledger. Partial credit gives 0.5 points for minor extra wording without changing the computed answer.

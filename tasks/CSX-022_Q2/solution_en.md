# Final Answer

The correct compact diagnosis is:

```json
{
  "target_family": "numeric_diagnosis",
  "metrics": {
    "peak_tmax_c": 45.3,
    "run_tmax_ge40_d": 9,
    "warm_nights_ge25": 25,
    "peak_wbt_c": 27.3,
    "acclim_anom_c": 4.5
  },
  "gates": {
    "persistent_heat": true,
    "warm_night_recovery_loss": true,
    "early_season_jump": true,
    "wet_bulb_ceiling": false,
    "isolated_spike": false
  },
  "answer": "persistent_early_season_dry_heat_recovery_stress",
  "rejected_alternative": "wet_bulb_ceiling_or_isolated_spike",
  "computed_consequence": "The ledger supports cumulative daytime heat with limited night recovery, not a humid-ceiling or one-day-spike diagnosis."
}
```

# Key Computations

`compute_gt.py` reads the CSX-022 event metadata and Open-Meteo daily and hourly archive for the March 1 to May 15, 2022 event window.

The numeric ledger is:

- `peak_tmax_c = max(Tmax) = 45.3 C`, on 2022-05-13.
- `run_tmax_ge40_d = longest consecutive run(Tmax >= 40 C) = 9 days`.
- `warm_nights_ge25 = count(Tmin >= 25 C) = 25 nights`.
- `peak_wbt_c = max(Stull wet-bulb approximation from hourly temperature and relative humidity) = 27.3 C`.
- `acclim_anom_c = max(mean(Tmean over 3 days) - mean(Tmean over preceding 30 days)) = 4.5 C`, ending 2022-04-12, where `Tmean = (Tmax + Tmin) / 2`.

The threshold ledger is:

- `persistent_heat = true` because `9 >= 7`.
- `warm_night_recovery_loss = true` because `25 >= 20`.
- `early_season_jump = true` because `4.5 >= 4.0 C`.
- `wet_bulb_ceiling = false` because `27.3 < 28.0 C`.
- `isolated_spike = false` because `9 > 2`.

# Reasoning Path

The controlling diagnosis follows directly from the gates. The event passes the persistence gate, the warm-night gate, and the early-season jump gate. Those three passing gates show that the event was not just one very hot afternoon; it combined repeated very hot days, many warm nights, and a sharp early-season jump relative to the preceding local baseline.

The humid-heat alternative fails the ledger because the maximum estimated wet-bulb temperature is 27.3 C, below the 28.0 C ceiling-style screen used in the prompt. Humid heat may add stress, but it is not the controlling threshold result.

The isolated-spike alternative also fails because the longest run of daily maximum temperature at or above 40 C is 9 days, not 2 days or fewer. The final answer is therefore `persistent_early_season_dry_heat_recovery_stress`.

# Computed Interpretation

The calculation supports a cumulative heat-stress interpretation: repeated extreme daytime heat and many warm nights reduced recovery during an early pre-monsoon phase. The result should not be expanded into uncomputed mortality, crop-loss, power-grid, or region-wide damage totals.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the final target family and answer label. Full credit requires `target_family = numeric_diagnosis` and `answer = persistent_early_season_dry_heat_recovery_stress` or an exact semantic equivalent. Partial credit for a persistent dry-heat label that omits either early-season timing or night recovery.
- 5 points: Reports the five required metrics with units or unit-implied keys and tolerances: 45.3 C peak Tmax, 9-day `Tmax >= 40 C` run, 25 warm nights, 27.3 C peak wet-bulb temperature, and 4.5 C acclimatization anomaly. Partial credit is proportional to the number of correct metrics.
- 4 points: Uses the required formulas and windows correctly, including longest-run logic, warm-night count, Stull-style hourly wet-bulb estimation, and the 3-day versus prior-30-day anomaly. Partial credit for correct values with one formula or window error.
- 3 points: Applies the gate thresholds and final decision rule correctly: persistence, warm-night, and early-season gates pass, while wet-bulb ceiling and isolated spike fail. Partial credit for one incorrect gate with the correct overall diagnosis.
- 2 points: Rejects the humid wet-bulb-ceiling and isolated-spike alternatives using the computed inequalities, not broad mechanism prose. Partial credit for rejecting only one alternative with a numeric basis.
- 2 points: Gives a bounded computed consequence tied to cumulative daytime heat and night-recovery loss. Partial credit for a consequence that is plausible but only weakly tied to the ledger.
- 1 point: Keeps the JSON compact and avoids uncomputed action plans, loss totals, or broad disaster explanation.

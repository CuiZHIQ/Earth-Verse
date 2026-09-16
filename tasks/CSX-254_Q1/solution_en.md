# Final Answer

```json
{
  "target_family": "threshold_ledger",
  "metrics": {
    "longest_hot_dry_run_days": 15,
    "longest_very_hot_dry_windy_run_days": 2,
    "peak_tmax_c": 46.0,
    "sentinel2_dnbr_mean": 0.156
  },
  "gates": {
    "hot_dry_run_ge_10": true,
    "vhdw_run_ge_2": true,
    "burn_change_mean_gt_0_10": true,
    "pyrocb_or_firestorm_text": true,
    "stratospheric_smoke_text": true
  },
  "answer": "compound_fire_weather_smoke_threshold_pass",
  "rejected_alternative": "heat_only_or_vegetation_only",
  "computed_consequence": "The threshold ledger supports a fire-weather-to-smoke cascade rather than a heat-only, rain/flood, or slow vegetation-change diagnosis."
}
```

# Key Computations

The reproducibility script reads the locked CSX-254 event anchor, the NASA Earth Observatory narrative, the Open-Meteo daily point weather series, and the Sentinel-2 dNBR summary.

Event window: 2019-09-01 through 2020-02-29.

Daily weather predicates:

- `hot_dry_day = Tmax >= 40.0 C and precipitation < 1.0 mm`
- `very_hot_dry_windy_day = Tmax >= 45.0 C and precipitation < 1.0 mm and wind_speed_10m_max >= 30.0 km/h`

Computed weather values:

- Peak daily maximum temperature: 46.0 C on 2019-12-24.
- Longest hot-dry run: 15 days, 2019-12-16 through 2019-12-30.
- Longest very-hot-dry-windy run: 2 days, 2019-12-19 through 2019-12-20.

Burn and narrative gates:

- Sentinel-2 mean dNBR: 0.156, so `burn_change_mean_gt_0_10 = true`.
- The narrative supports pyrocumulonimbus, fire-triggered cloud, or firestorm behavior, so `pyrocb_or_firestorm_text = true`.
- The narrative supports smoke at 15-19 km altitude or the stratosphere, so `stratospheric_smoke_text = true`.

Decision rule:

```text
compound_fire_weather_smoke_threshold_pass =
  longest_hot_dry_run_days >= 10
  and longest_very_hot_dry_windy_run_days >= 2
  and sentinel2_dnbr_mean > 0.10
  and pyrocb_or_firestorm_text
  and stratospheric_smoke_text
```

All five gates pass: `15 >= 10`, `2 >= 2`, `0.156 > 0.10`, `true`, and `true`.

# Reasoning Path

1. The hot-dry run test establishes a sustained preconditioning interval: 15 consecutive days meet the `Tmax >= 40.0 C` and `precipitation < 1.0 mm` predicate.
2. The very-hot-dry-windy test captures the acute escalation window: 2 consecutive days meet the `Tmax >= 45.0 C`, `precipitation < 1.0 mm`, and `wind >= 30.0 km/h` predicate.
3. The burn-change gate is positive because the mean dNBR is 0.156, exceeding the 0.10 threshold.
4. The narrative gates separately support pyrocumulonimbus or firestorm behavior and high-altitude or stratospheric smoke.
5. Because every required gate is true, the deterministic label is `compound_fire_weather_smoke_threshold_pass`.
6. A heat-only diagnosis fails because it omits the burn and smoke gates. A rain/flood diagnosis fails because the threshold test is built around dry heat, wind, burn change, and smoke. A slow vegetation-change diagnosis fails because the acute weather and smoke gates are required and satisfied.

# Computed Interpretation

The computed result is a compact threshold pass for a fire-weather-to-smoke cascade. The Sentinel-2 dNBR value is an early-season burn-change threshold signal from the package, not a full-season burned-area inventory. The result should not be expanded into exact national burned area, casualty, property-loss, or full fireground-representativeness claims.

# Scoring Rubric

Total: 20 points.

- 3 points: Requested JSON shape. Full credit for returning compact JSON with `target_family`, `metrics`, `gates`, `answer`, `rejected_alternative`, and one ledger-tied `computed_consequence`. Partial credit for minor key-name differences that preserve the same fields.
- 5 points: Metric extraction. Full credit for `longest_hot_dry_run_days = 15`, `longest_very_hot_dry_windy_run_days = 2`, `peak_tmax_c = 46.0`, and `sentinel2_dnbr_mean = 0.156` within tolerance and with recognizable units. Partial credit for two or three correct metrics.
- 3 points: Predicate and formula use. Full credit for applying the hot-dry, very-hot-dry-windy, and burn-change threshold definitions exactly. Partial credit for correct qualitative gates with one threshold or inequality error.
- 4 points: Gate ledger and final label. Full credit for setting all five gates to true and returning `compound_fire_weather_smoke_threshold_pass` by the all-gates decision rule. Partial credit for the correct label with one missing gate or for correct gates with a mislabeled final answer.
- 2 points: Text-gate separation. Full credit for treating pyrocumulonimbus or firestorm support and stratospheric-smoke support as narrative gates, not as quantities inferred from dNBR. Partial credit for finding the right flags but blurring their source.
- 2 points: Rejected alternative. Full credit for rejecting heat-only, rain/flood, or slow vegetation-change alternatives through the failed ledger logic. Partial credit for rejecting one weaker alternative without tying it to a gate.
- 1 point: Bounded computed consequence. Full credit for keeping the final sentence tied to the threshold result and avoiding extra loss totals, national representativeness claims, action claims, or broad disaster explanation. No credit if the answer turns into an action note or broad disaster explanation.

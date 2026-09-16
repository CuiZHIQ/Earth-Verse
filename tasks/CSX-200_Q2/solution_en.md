# Final Answer

```json
{
  "dnbr_metrics": {
    "dnbr_max": 0.859705,
    "dnbr_mean": -0.083037,
    "dnbr_std_dev": 0.212884,
    "dnbr_peak_z": 4.428428
  },
  "annual_change_metrics": {
    "annual_change_max": 0.807727,
    "annual_change_mean": 0.061316,
    "annual_peak_mean_ratio": 13.173189
  },
  "threshold_flags": {
    "local_high_dnbr": true,
    "uniform_scene_burn": false,
    "mixed_scene": true,
    "localized_annual_change": true
  },
  "consistency_class": "consistent_patchy_high_severity_fire_change",
  "interpretation": "Local high-severity dNBR is consistent with patchy fire-linked surface change, not uniform burn."
}
```

# Key Computations

The dNBR maximum is `0.859705`, which passes the high-severity threshold of `0.66`. The scene mean is `-0.083037`, so the broad uniform burn threshold of `0.27` fails, while the standard deviation of `0.212884` satisfies the mixed-scene spread threshold of `0.10`.

The derived dNBR peak z-score is:

```text
(0.859705 - -0.083037) / 0.212884 = 4.428428
```

For the annual surface-change product:

```text
0.807727 / 0.061316 = 13.173189
```

That passes the localized annual-change rule because the annual maximum is at least `0.75`, the annual mean is below `0.10`, and the peak/mean ratio is at least `10`. The final class is therefore `consistent_patchy_high_severity_fire_change`.

# Reasoning Path

The ledger first checks the local high-severity tail: the dNBR maximum clears `0.66`, so a local high-end surface-change signal is present. It then checks whether that signal is broad and uniform. The negative dNBR mean fails the broad-positive threshold, while the standard deviation clears the mixed-scene threshold, so the scene-level summary is patchy rather than uniform.

The annual surface-change test is evaluated separately. The annual maximum is high, the annual mean stays low, and the peak/mean ratio is above `10`, so the annual-change record supports localized change rather than broad scene-wide change. Combining these flags gives the consistency class and rejects broad uniform burn, smoke-only reading, and a negative-mean veto of the local high-end dNBR value.

# Computed Interpretation

The numeric result is a patchy high-severity surface-change ledger: the peak dNBR and annual-change ratio are high, but the negative dNBR mean prevents a uniform-burn summary.

# Scoring Rubric

Total: 20 points.

- 4 points: Provides the requested compact JSON with dNBR metrics, annual-change metrics, threshold flags, consistency class, and one calculation-grounded interpretation.
- 6 points: Correctly reports the key values and derived formulas within tolerance: dNBR max `0.859705`, mean `-0.083037`, std `0.212884`, dNBR peak z-score `4.428428`, annual max `0.807727`, annual mean `0.061316`, and annual peak/mean ratio `13.173189`.
- 4 points: Applies all threshold tests correctly: `local_high_dnbr=true`, `uniform_scene_burn=false`, `mixed_scene=true`, and `localized_annual_change=true`.
- 3 points: Combines the threshold states to reach `consistent_patchy_high_severity_fire_change` for the right consistency reason.
- 2 points: Rejects at least two numeric overreads, such as broad uniform burn, smoke-only interpretation, negative-mean veto of local fire effects, or annual hotspot as broad change.
- 1 point: Keeps the interpretation concise and avoids extra-data impact, loss, or response claims. Partial credit: 0.5 points for a correct but overly broad interpretation.

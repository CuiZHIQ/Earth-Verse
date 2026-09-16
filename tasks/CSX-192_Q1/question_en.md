# Western Cape Wildfire Threshold Ledger

A fire-risk review team is checking a numeric screen for the June 2017 Western Cape wildfires near Knysna and Plettenberg Bay. Use the incident technical record for 7-14 June 2017 and its paired burn-summary window to test whether the event reaches a high-threshold ledger.

Use these fixed rules:

- A report anchor passes if the record gives at least 10,000 evacuees and a house-destruction lower bound of at least 500.
- A gridded heat context passes if ERA5-Land reports event-window maximum 2 m temperature at least 34.0 C and mean maximum 2 m temperature at least 32.0 C.
- A gridded wind context passes if ERA5-Land mean 10 m wind-vector speed is at least 1.0 m/s.
- A positive burn summary passes if mean dNBR is `>= 0.000` and maximum dNBR is `>= 0.300`.
- The high-threshold ledger is met only when at least three of the four component tests pass.

Return compact JSON with exactly these fields: `score`, `high_threshold_met`, `era5_peak_tmax_c`, `era5_mean_tmax_c`, `era5_mean_wind_speed_mps`, `dnbr_state`, `passed_tests`, `failed_tests`.

Round numeric values to one decimal for temperature and three decimals for wind speed.

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to make the Western Cape fire screen explain why the high-threshold label fails despite strong report and heat signals.


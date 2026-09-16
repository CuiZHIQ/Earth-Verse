# CSX-279 Q2: ENSO Drought Threshold Ledger

Use the local CSX-279 event package to compute a deterministic numeric ledger for the 2015-2016 El Nino and Pacific Island drought event.

Select package-local precipitation evidence for the 2015-10-01 to 2015-11-15 rainfall slice, regional aggregate precipitation evidence for the same slice, and package-local ocean-atmosphere index evidence spanning SON 2015 through MAM 2016 plus October 2015 through April 2016 monthly values.

Derive these quantities from the package data:

1. `r_gpm = gpm_event_precip_mm_min / gpm_event_precip_mm_mean`.
2. `r_chirps = chirps_event_precip_mm_min / chirps_event_precip_mm_mean`.
3. `dry_ratio_mean = mean(r_gpm, r_chirps)`.
4. `dry_deficit_mean = 1 - dry_ratio_mean`.
5. `agreement_delta = abs(r_gpm - r_chirps)`.
6. `oni_peak_c = max(ONI anomaly)` across SON 2015 through MAM 2016.
7. `soi_neg_frac = count(SOI < 0) / count(SOI months)` across October 2015 through April 2016.
8. `tmax_spread_c = temperature_2m_max_c_max - temperature_2m_max_c_mean`.
9. `ledger_score = 100 * (0.35 * min(dry_deficit_mean / 0.70, 1) + 0.20 * max(0, 1 - agreement_delta / 0.01) + 0.25 * min(oni_peak_c / 2.0, 1) + 0.10 * soi_neg_frac + 0.10 * min(tmax_spread_c / 4.0, 1))`.

Set `answer` to `all_5_thresholds_met` when these five tests all pass: `dry_deficit_mean >= 0.70`, `agreement_delta <= 0.01`, `oni_peak_c >= 2.0`, `soi_neg_frac >= 0.80`, and `tmax_spread_c >= 4.0`. Otherwise set it to `thresholds_incomplete`.

Return only a compact JSON object with:

```json
{
  "answer": "",
  "dry_ratio_mean": 0.0,
  "dry_deficit_mean": 0.0,
  "agreement_delta": 0.0,
  "oni_peak_c": 0.0,
  "soi_neg_frac": 0.0,
  "tmax_spread_c": 0.0,
  "ledger_score": 0.0
}
```

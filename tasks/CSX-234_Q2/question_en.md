# Gorkha May 12 Consistency Ledger

The 2015 Gorkha earthquake sequence in Nepal had a major April 25 mainshock and a large May 12 earthquake recorded in the same technical timeline. A geoscience reviewer needs a compact numeric ledger that tests whether the May 12 entry is quantitatively consistent with a major seismic sequence signal rather than a rainfall-threshold signal.

Using the earthquake catalog entries and event-window precipitation summaries, compute:

- `elapsed_days`: decimal days from the April 25 mainshock UTC time to the largest Nepal earthquake on May 12, rounded to two decimals
- `may12_rank_by_magnitude`: rank of the largest May 12 Nepal earthquake among Nepal earthquakes in the sequence catalog, with rank 1 as largest
- `mag_deficit`: `M_mainshock - M_May12`, rounded to one decimal
- `may12_moment_share`: `10 ** (1.5 * (M_May12 - M_mainshock))`, rounded to three decimals
- `mainshock_to_may12_moment_ratio`: reciprocal of `may12_moment_share`, rounded to two decimals
- `nepal_eq_mge6_count`: count of Nepal earthquakes with magnitude at least 6.0 in the sequence catalog
- `red_alert_share`: red-alert Nepal earthquake count divided by all Nepal earthquakes in that catalog, rounded to three decimals
- `precip_mean_max_mm`: largest event-window precipitation mean, rounded to two decimals
- `precip_means_ge_20mm_count`: count of event-window precipitation means at or above 20 mm

Assign `sequence_class` as `"seismic_sequence_consistent"` only if the May 12 rank is 2, `may12_moment_share >= 0.15`, `nepal_eq_mge6_count >= 4`, `red_alert_share >= 0.5`, and `precip_means_ge_20mm_count == 0`; otherwise assign `"fails_seismic_sequence_screen"`.

Return compact JSON:

```json
{
  "answer": {
    "elapsed_days": 0.0,
    "may12_rank_by_magnitude": 0,
    "mag_deficit": 0.0,
    "may12_moment_share": 0.0,
    "mainshock_to_may12_moment_ratio": 0.0,
    "nepal_eq_mge6_count": 0,
    "red_alert_share": 0.0,
    "precip_mean_max_mm": 0.0,
    "precip_means_ge_20mm_count": 0
  },
  "sequence_class": "<class label>"
}
```

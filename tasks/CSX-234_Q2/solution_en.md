# Correct Answer

```json
{
  "answer": {
    "elapsed_days": 17.04,
    "may12_rank_by_magnitude": 2,
    "mag_deficit": 0.5,
    "may12_moment_share": 0.178,
    "mainshock_to_may12_moment_ratio": 5.62,
    "nepal_eq_mge6_count": 5,
    "red_alert_share": 0.571,
    "precip_mean_max_mm": 13.14,
    "precip_means_ge_20mm_count": 0
  },
  "sequence_class": "seismic_sequence_consistent"
}
```

Canonical class token for deterministic scoring: `seismic_sequence_consistent`.

# Key Computations

The April 25 Nepal mainshock is M7.8 at 2015-04-25T06:11:25.950Z. The largest Nepal earthquake on May 12 is M7.3 at 2015-05-12T07:05:19Z. The elapsed time is `(May12 - mainshock) / 86400 = 17.0374` days, rounded to 17.04 days.

The magnitude deficit is `7.8 - 7.3 = 0.5`. The May 12 moment share is `10 ** (1.5 * (7.3 - 7.8)) = 0.1778279`, rounded to 0.178. Its reciprocal is `5.6234`, rounded to 5.62.

Among Nepal earthquake entries, the magnitudes are 7.8, 7.3, 6.7, 6.6, 6.3, 5.6, and 5.6, so the May 12 event ranks second and 5 entries are M>=6.0. Four of the seven Nepal entries have red alerts, giving `4 / 7 = 0.571`. The three event-window precipitation means are 13.143 mm, 6.912 mm, and 3.158 mm; the maximum is 13.14 mm and none reach the 20 mm threshold.

# Numeric Check Path

All five class tests pass: rank 2, moment share above 0.15, at least four Nepal M>=6 entries, red-alert share above 0.5, and zero precipitation means at or above 20 mm. The resulting class is `seismic_sequence_consistent`.

# Scoring Rubric

- 4 points: Returns the requested compact JSON with all nine numeric fields and `sequence_class`.
- 4 points: Identifies the correct April 25 and May 12 Nepal earthquake entries, times, magnitudes, and May 12 magnitude rank.
- 4 points: Computes the magnitude deficit, moment-share formula, and reciprocal moment ratio with correct rounding.
- 3 points: Computes the Nepal M>=6 count and red-alert share from the catalog entries.
- 3 points: Computes the precipitation threshold ledger, including the 13.14 mm maximum mean and zero means at or above 20 mm.
- 2 points: Keeps units, rounding, and the class rule clear using only the requested computed fields.

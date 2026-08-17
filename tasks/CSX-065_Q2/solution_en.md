# Final Answer

```json
{
  "final_label": "prolonged_lowland_storage_supported",
  "score": 5,
  "tests": {
    "partial_window": true,
    "heavy_accumulation": true,
    "satellite_agreement": true,
    "moderate_concentration": true,
    "report_persistence": true
  },
  "key_values": {
    "coverage_pct": 33.6,
    "precip_means_mm": {
      "era5": 360.117,
      "gpm": 310.842,
      "chirps": 311.49
    },
    "satellite_gap_pct": 0.2,
    "max_mean_ratios": {
      "era5": 1.49,
      "gpm": 2.015,
      "chirps": 1.886
    },
    "report_signal_count": 12
  },
  "rejected_diagnosis": "short_burst_only",
  "interpretation": "The five-test ledger supports a prolonged lowland storage signal because substantial multi-product rainfall, low satellite disagreement, moderate max-to-mean ratios, and persistent reported flooding all pass together."
}
```

# Key Computations

- Event window: 2011-07-31 to 2011-12-14, inclusive = 137 days.
- Quantified precipitation window: 2011-07-31 to 2011-09-14, inclusive = 46 days.
- Coverage percentage: `46 / 137 * 100 = 33.6%`, below the 50% partial-window threshold.
- Event-mean precipitation: ERA5-Land = 360.117 mm, GPM IMERG = 310.842 mm, CHIRPS = 311.490 mm. All are at least 300 mm.
- Satellite agreement: satellite mean = `(310.842 + 311.490) / 2 = 311.166 mm`; absolute gap = `0.649 mm`; percent gap = `0.649 / 311.166 * 100 = 0.2%`, below the 1% threshold.
- Product max-to-mean ratios: ERA5-Land = `536.513 / 360.117 = 1.490`; GPM = `626.477 / 310.842 = 2.015`; CHIRPS = `587.479 / 311.490 = 1.886`. All are below 2.5.
- Documented persistence signals found in the event report: 12, meeting the threshold of at least 10.

# Reasoning Path

The `partial_window` test passes because the measured precipitation interval covers 33.6% of the full 137-day flood season, so the rainfall sample is part of a longer event period rather than the whole season.

The `heavy_accumulation` test passes because all three product means exceed 300 mm. The `satellite_agreement` test passes because GPM and CHIRPS differ by only 0.2% relative to their two-product mean. This makes the heavy-rainfall signal stable across the two satellite products.

The `moderate_concentration` test passes because the largest max-to-mean ratio is 2.015, below the 2.5 cutoff. The precipitation field has important maxima, but the ratios do not reduce the diagnosis to a single-cell burst. The `report_persistence` test also passes because 12 documented signals describe sustained monsoon flooding, weeks of water, agricultural inundation, and Bangkok backwater risk.

With all five tests passing, the score is 5 out of 5. The deterministic label is `prolonged_lowland_storage_supported`, and the rejected diagnosis is `short_burst_only`.

# Computed Interpretation

The event is best scored as a prolonged lowland rainfall-storage case: the quantitative precipitation metrics and documented persistence signals align, while the short-burst-only diagnosis fails the five-test ledger.

# Scoring Rubric

- 4 points: Final JSON structure and label. Full credit requires the requested top-level keys, all five test booleans, score 5, final label `prolonged_lowland_storage_supported`, and rejected diagnosis `short_burst_only`. Partial credit: 2-3 points for a mostly complete JSON ledger with one missing field or a synonymous final label; 1 point for a readable but incomplete structured answer.
- 4 points: Duration and accumulation calculations. Full credit requires 137 event days, 46 precipitation days, 33.6% coverage, and all three mean precipitation values within tolerance. Partial credit: 2-3 points for correct duration or precipitation values with one rounding or product omission; 1 point for only identifying that rainfall was substantial.
- 4 points: Satellite agreement and concentration ratios. Full credit requires satellite mean 311.166 mm, GPM-CHIRPS gap 0.649 mm, gap percentage 0.2%, and max-to-mean ratios 1.490, 2.015, and 1.886. Partial credit: 2-3 points for correct formulas with minor arithmetic errors; 1 point for using the right products but missing either the agreement or ratio test.
- 3 points: Threshold scoring. Full credit requires all five tests marked true and the score computed as 5 out of 5 using the stated thresholds. Partial credit: 2 points for one incorrect test state; 1 point for recognizing the overall label but not showing the component scoring.
- 3 points: Reasoning path and rejected diagnosis. Full credit ties the passed tests to prolonged lowland storage and rejects `short_burst_only` because the ledger has multi-product accumulation, low satellite disagreement, moderate ratios, and persistent report signals. Partial credit: 1-2 points for a plausible explanation that misses one or two required links.
- 2 points: Computed interpretation discipline. Full credit keeps the interpretation to one calculation-bound event consequence without management steps or a broad disaster essay. Partial credit: 1 point for a mostly concise interpretation with minor extra narrative.

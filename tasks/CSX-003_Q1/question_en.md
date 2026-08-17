# Evidence Sufficiency Ruling: Heat Timing Versus Drought Evidence

A benchmark reviewer proposes this evidence basis for CSX-003:

> "Use the package heat archive to place the compound heat peak in late August, and use the package gridded precipitation accumulations as the direct drought measurement for that same late-August peak."

Resolve whether that proposed basis is sufficient. Use only CSX-003 package-local evidence. Do not use web search, hidden answers, or invented values. All paths in the answer must be package-relative.

You must:

1. Use the locked event window from the package anchor.
2. Use the daily heat archive to compute the peak apparent-temperature date/value and the longest same-day run satisfying Tmax >= 35 C, apparent temperature >= 40 C, and Tmin >= 28 C inside the locked event window.
3. Use the strongest package report evidence for drought or Poyang Lake low-water context.
4. Compare ERA5, GPM, and CHIRPS precipitation-summary windows against the peak apparent-temperature date.
5. Compute the GPM and CHIRPS mean-precipitation difference and ratio over their shared summary window.
6. Reject or mark insufficient at least one tempting alternative source basis, with a package-relative path and a numeric or source-path reason.

Return only compact JSON with this schema:

```json
{
  "answer_type": "evidence_sufficiency_ruling",
  "ruling": "sufficient|partially_supported|insufficient",
  "claim_ruling": {
    "supported_part": "short statement",
    "insufficient_part": "short statement"
  },
  "selected_evidence": {
    "event_window": {
      "path": "package-relative/path",
      "start": "YYYY-MM-DD",
      "end": "YYYY-MM-DD",
      "expected_days": 0
    },
    "heat_timing": {
      "path": "package-relative/path",
      "daily_records_in_window": 0,
      "peak_apparent_temperature_c": 0,
      "peak_apparent_temperature_date": "YYYY-MM-DD",
      "compound_heat_run": {
        "start": "YYYY-MM-DD",
        "end": "YYYY-MM-DD",
        "days": 0,
        "rule": "Tmax >=35 C, apparent >=40 C, Tmin >=28 C"
      }
    },
    "drought_low_water_context": {
      "path": "package-relative/path",
      "evidence_role": "direct_report_context",
      "matched_terms": ["term"]
    }
  },
  "calculation_check": {
    "precipitation_summary_window": {
      "era5": ["YYYY-MM-DD", "YYYY-MM-DD"],
      "gpm": ["YYYY-MM-DD", "YYYY-MM-DD"],
      "chirps": ["YYYY-MM-DD", "YYYY-MM-DD"]
    },
    "precipitation_to_heat_peak_gap_days": 0,
    "precipitation_product_conflict": {
      "gpm_mean_mm": 0,
      "chirps_mean_mm": 0,
      "difference_mm": 0,
      "ratio": 0
    }
  },
  "insufficient_alternatives": [
    {
      "basis": "short rejected or insufficient basis",
      "paths": ["package-relative/path"],
      "reason_code": "wrong_window|product_conflict|wrong_measurement_type|weak_context",
      "numeric_or_path_reason": "short reason"
    }
  ],
  "minimal_required_paths": ["package-relative/path"],
  "final_assessment": "one sentence"
}
```

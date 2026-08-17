# Black Summer Burn-Change Evidence Arbitration

A benchmark audit is checking a narrow package-local claim for CSX-008: the package contains direct remote-sensing evidence of localized burn-scar change associated with the 2019-2020 Black Summer event window. Resolve which file can support that claim and which plausible files are insufficient or wrong-role substitutes.

Use only the CSX-008 package files. Do not use web search, outside burn-severity thresholds, or hidden answers. Use package-relative source paths only.

Rules:

- Establish the official event window from the strongest package-local event anchor.
- Select a direct burn-change source only if it is a burn-index or dNBR-style product and its post/fire window overlaps the official event window.
- The annual satellite-embedding cosine-change file may be reported as a rejected substitute, but do not treat its metric as dNBR or burn severity.
- The local heat/humidity time series may be used only as fire-weather context, not as direct burn-scar measurement.
- Report the dNBR source statistics, event-window overlap, a compact contrast calculation, rejected alternatives, and the final ruling.

Return compact JSON exactly in this schema:

```json
{
  "answer_type": "remote_sensing_change_attribution",
  "claim": "direct_package_evidence_of_localized_burn_scar_change",
  "ruling": "<fixed ruling label>",
  "selected_evidence": {
    "path": "<package-relative path>",
    "modality": "<product/modality>",
    "pre_window": ["YYYY-MM-DD", "YYYY-MM-DD"],
    "post_window": ["YYYY-MM-DD", "YYYY-MM-DD"],
    "post_window_overlap_with_event_days": 0,
    "post_window_extra_days_after_event": 0,
    "stats": {
      "dnbr_max": 0.0,
      "dnbr_mean": 0.0,
      "dnbr_min": 0.0,
      "dnbr_stdDev": 0.0
    }
  },
  "calculation_check": {
    "event_window_days": 0,
    "dnbr_max_minus_mean": 0.0,
    "dnbr_max_over_mean": 0.0,
    "dnbr_max_z_like_above_mean": 0.0
  },
  "rejected_or_insufficient_alternatives": {
    "<package-relative path>": {
      "role_error": "<why insufficient>",
      "numeric_consequence_if_swapped": {}
    }
  },
  "source_paths": {
    "event_window": "<package-relative path>",
    "direct_burn_change": "<package-relative path>",
    "rejected_embedding_change": "<package-relative path>",
    "fire_weather_context_only": "<package-relative path>"
  },
  "reference_trace": [
    "<short reproducible step>",
    "<short reproducible step>"
  ]
}
```

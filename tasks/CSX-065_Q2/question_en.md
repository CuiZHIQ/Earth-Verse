# Monsoon Rainfall Storage Score Ledger

A hydrometeorology review team is checking the 2011 Southeast Asia monsoon floods, with the flood season running from 2011-07-31 through 2011-12-14. The team needs a compact calculation ledger that decides whether the quantitative record supports a prolonged lowland rainfall-storage diagnosis rather than a short-burst-only diagnosis.

Compute five one-point tests:

- `partial_window`: `precip_window_days / event_window_days * 100` is below 50%.
- `heavy_accumulation`: ERA5-Land, GPM IMERG, and CHIRPS event-mean precipitation are each at least 300 mm.
- `satellite_agreement`: `abs(GPM mean - CHIRPS mean) / mean(GPM mean, CHIRPS mean) * 100` is below 1%.
- `moderate_concentration`: every product max-to-mean precipitation ratio is below 2.5.
- `report_persistence`: at least 10 documented event signals indicate sustained monsoon flooding, weeks of water, agricultural inundation, or Bangkok backwater risk.

Return only compact JSON with these keys:

```json
{
  "final_label": "<compact diagnosis label>",
  "score": "<0-5 integer>",
  "tests": {
    "partial_window": "<true/false>",
    "heavy_accumulation": "<true/false>",
    "satellite_agreement": "<true/false>",
    "moderate_concentration": "<true/false>",
    "report_persistence": "<true/false>"
  },
  "key_values": {
    "coverage_pct": "<number>",
    "precip_means_mm": {},
    "satellite_gap_pct": "<number>",
    "max_mean_ratios": {},
    "report_signal_count": "<integer>"
  },
  "rejected_diagnosis": "<compact rejected diagnosis>",
  "interpretation": "<one calculation-bound sentence>"
}
```

Use percentages to one decimal place, precipitation means to three decimals, and ratios to three decimals. Keep the interpretation to one sentence and do not add management steps or a broad disaster essay.

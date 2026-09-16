# Final Answer

Correct answer: `persistent_record_marine_heatwave`.

Canonical JSON:

```json
{
  "coverage_record_ratio": 1.39,
  "duration_ratio": 60.8,
  "evidence_paths": [
    "metadata/event.json",
    "data/event_reports/event_reports_004_01_Locked_package_evidence_report.html.html",
    "data/other/other_004_02_Copernicus_State_of_the_Planet_-_2023_North_Atlantic_tropical_marine_heatwave.html.html",
    "data/other/other_005_03_NOAA_Climate.html.html"
  ],
  "final_label": "persistent_record_marine_heatwave",
  "max_sst_anomaly_c": 3.0,
  "mhw_days_record_ratio": 1.35,
  "mhw_min_months": 10,
  "phase_code": "ne_may_peak_to_caribbean_autumn",
  "proof_sentence": "The diagnosis passes because the North Atlantic persistence is 10 months, about 60.8 times the five-day MHW definition, both record ratios exceed 1.0, the anomaly reaches about 3.0 deg C, and the basin phase evolves from a north-east May peak to Caribbean conditions by autumn."
}
```

# Key Computations

The hidden computation uses the local CSX-021 event metadata plus three report records:

- `data/other/other_005_03_NOAA_Climate.html.html`: approximately 94 percent of the ocean surface experienced at least one marine heatwave in 2023; a marine heatwave is defined by SSTs in the warmest 10 percent for at least five days; the eastern tropical and North Atlantic Ocean was in a marine-heatwave state for at least 10 months; the global ocean experienced 116 marine-heatwave days versus the previous record of 86 days in 2016.
- `data/event_reports/event_reports_004_01_Locked_package_evidence_report.html.html`: the global ocean had average daily marine-heatwave coverage of 32 percent versus a previous record of 23 percent; a severe and extreme North Atlantic band reached about 3.0 deg C above average.
- `data/other/other_004_02_Copernicus_State_of_the_Planet_-_2023_North_Atlantic_tropical_marine_heatwave.html.html`: the event peaked in the north-east in May and spread south-west to reach the Caribbean by autumn.

Formulas and values:

- Minimum duration in days: `round(10 * 365 / 12) = 304`.
- Duration ratio against the five-day definition: `304 / 5 = 60.8`.
- Average daily coverage record ratio: `32 / 23 = 1.39`.
- Global mean marine-heatwave-days record ratio: `116 / 86 = 1.35`.
- SST anomaly anchor: `3.0 deg C`.
- Basin phase code: `ne_may_peak_to_caribbean_autumn`.

# Reasoning Path

The proof has four gates. First, the North Atlantic duration is at least 10 months, which converts to about 304 days and a 60.8 ratio against the five-day definition. That fails the brief-pulse hypothesis by a large margin.

Second, the two record ratios both exceed 1.0: average daily marine-heatwave coverage is 1.39 times the previous record, and global mean marine-heatwave days are 1.35 times the previous record. These ratios place the event in record context rather than a local or one-day anomaly frame.

Third, the North Atlantic anomaly anchor reaches about 3.0 deg C and is paired with severe and extreme category wording. Fourth, the phase timing is not static: the basin signal peaks in the north-east in May and reaches the Caribbean by autumn. Since all gates pass, the compact conclusion is `persistent_record_marine_heatwave`.

# Computed Interpretation

The calculation supports a persistent marine heatwave diagnosis: duration, record ratios, anomaly magnitude, and basin timing all support the same final label. Land-exposure layers or a sole ENSO framing do not satisfy these computed gates.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested compact JSON shape and gives `persistent_record_marine_heatwave` or a very close equivalent as the final label.
- 4 points: Extracts the North Atlantic minimum duration as 10 months and correctly computes `round(10 * 365 / 12) / 5 = 60.8`.
- 4 points: Computes both record ratios with acceptable rounding: `32 / 23 = 1.39` and `116 / 86 = 1.35`.
- 3 points: Includes the North Atlantic SST anomaly anchor of about 3.0 deg C and the phase code `ne_may_peak_to_caribbean_autumn`.
- 3 points: Explains the pass result through the four gates: duration, record ratios, anomaly magnitude, and basin phase timing.
- 2 points: Rejects the brief-pulse and single-cause climate-mode hypotheses through the computed gates rather than by broad narrative.
- 1 point: Keeps the answer concise and does not add realized-loss totals or action planning beyond the computed diagnosis.

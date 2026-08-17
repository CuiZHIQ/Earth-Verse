# Tasman Seismic-Calving Consistency Index

A technical review team is checking whether the February-March 2011 Tasman Glacier event satisfies a compact seismic-calving consistency test, or whether same-window weather metrics are strong enough to counterweight that diagnosis.

Compute the Tasman seismic-calving consistency index, TSCI, using these rules:

- `chain_score_0_5`: count one point each for earthquake magnitude being present, Tasman Glacier as the source, Tasman Lake as the receiving medium, iceberg expression, and a final-pulse timing statement.
- `mass_gate`: 1 if the reported ice mass is at least 30 million tons, otherwise 0.
- `image_lag_gate`: 1 if the lake-image date is 1 to 14 days after 2011-02-22, otherwise 0.
- `weather_counterweight_gate`: 3 only if point precipitation total is below 50 mm, point precipitation peak share is below 0.5, peak daily 10 m wind is below 30 km/h, and the wind peak occurs after 2011-02-22; otherwise 0.
- `TSCI = chain_score_0_5 + mass_gate + image_lag_gate + weather_counterweight_gate`.

Return one compact JSON object with exactly these fields:

```json
{
  "chain_score_0_5": 0,
  "mass_million_tons": 0,
  "image_lag_days": 0,
  "point_precip": {"total_mm": 0, "peak_share": 0},
  "wind_peak": {"kmh": 0, "lag_days": 0},
  "tsci_0_10": 0,
  "consistency_label": "",
  "computed_consequence": ""
}
```

Use `seismic_calving_lake_iceberg_consistent` only if the chain score is 5 and TSCI is at least 9. Keep `computed_consequence` to one short computed phrase.

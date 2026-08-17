# Hurricane Ida NYC Pluvial Signal Ledger

A hydrometeorology team is checking the New York City signal from the September 1-3, 2021 Hurricane Ida flooding. The team needs a compact, data-backed ledger that tests whether the NYC record satisfies a rainfall-driven urban pluvial signal, rather than a surge-, wind-, or remote-damage-dominant interpretation.

Compute the event rainfall load, rainfall concentration, local street/sewer feedback, and exposed-population proxy. Apply these gates:

- `rainfall_burst`: peak hourly rainfall is at least 25 mm and the wettest 6-hour share of the event total is at least 0.50.
- `street_sewer_signal`: both sewer and street-flooding shares of the local service records are at least 0.80.
- `urban_exposure`: exposed-population proxy is at least 50,000.

Return compact JSON in this shape, rounding rainfall to 0.1 mm, shares to 4 decimals, and population to 0.1:

```json
{
  "target_family": "nyc_ida_pluvial_signal_score_ledger",
  "metrics": {
    "event_total_mm": 0,
    "peak_hour_mm": 0,
    "wettest_6h_mm": 0,
    "wettest_6h_share": 0,
    "service_records": 0,
    "sewer_share": 0,
    "street_flooding_share": 0,
    "exposed_population_proxy": 0
  },
  "gates": {
    "rainfall_burst": false,
    "street_sewer_signal": false,
    "urban_exposure": false
  },
  "score": 0,
  "max_score": 3,
  "answer": "",
  "computed_consequence": ""
}
```

Use `answer` to give the final one-line consistency label, and keep `computed_consequence` to one sentence tied only to the ledger values.

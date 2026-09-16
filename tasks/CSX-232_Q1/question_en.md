# Kahramanmaras Sequence Severity Ledger

A seismic analysis cell is checking an index-based severity ledger for the 6 February 2023 Turkiye-Syria (Kahramanmaras) earthquake sequence. Several large shocks occurred close together, so the team needs a reproducible way to identify the lead shock and its closest competitor without turning the result into a broad impact narrative.

For every major sequence earthquake with magnitude at least 6.0, compute this severity score:

```text
score =
  0.30 * (magnitude / 8.0 * 100)
+ 0.25 * (maximum modeled intensity / 10.0 * 100)
+ 0.20 * (significance / maximum sequence significance * 100)
+ 0.15 * alert_points
+ 0.10 * (log10(felt_reports + 1) / log10(maximum sequence felt_reports + 1) * 100)
```

Use alert points of red = 100, orange = 80, yellow = 60, green = 20, and missing = 0. Classify the winning score as critical if it is at least 85, high if it is at least 70, medium if it is at least 50, and low otherwise.

Return compact JSON with these keys:

```json
{
  "selected_event_id": "event identifier",
  "selected_event_title": "event title",
  "severity_class": "critical|high|medium|low",
  "selected_score": 0.0,
  "nearest_rival_id": "event identifier",
  "nearest_rival_score": 0.0,
  "decision_margin": 0.0,
  "winning_components": {
    "magnitude_pct": 0.0,
    "intensity_pct": 0.0,
    "significance_pct": 0.0,
    "alert_pct": 0.0,
    "felt_pct": 0.0
  },
  "interpretation": "one sentence"
}
```

Round scores and component percentages to three decimals. Keep the interpretation to one sentence that follows from the score ledger.

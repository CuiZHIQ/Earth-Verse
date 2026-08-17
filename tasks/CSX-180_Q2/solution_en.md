# Final Answer

The compact final label is `regional_smoke_aerosol_window_confirmed`.

```json
{
  "event_days": 61,
  "local_days": 46,
  "coverage_fraction": 0.754,
  "smoke_phrase_hits": 7,
  "precip_mm": {"mean": 275.0, "spread": 101.3},
  "wind_mps": {"u": 0.697, "v": 0.149, "speed": 0.713, "bearing_to_deg": 77.9},
  "dnbr_status": "no_sufficient_scenes",
  "consistency_verdict": "The ledger confirms a regional smoke-and-aerosol window; local dNBR burn mapping is not available, and rainfall remains contextual."
}
```

# Key Computations

The event anchor runs from 2000-08-01 through 2000-09-30, so inclusive days are `(2000-09-30 - 2000-08-01) + 1 = 61`. The ERA5-Land aggregate window runs from 2000-08-01 through 2000-09-15, giving 46 inclusive days and `46 / 61 = 0.754`.

Across the NASA event and air-quality reports, all 7 listed motifs are present, including the air-quality report phrase `burning of grass and shrubland`.

The three event-accumulated precipitation means are ERA5-Land 221.1 mm, GPM IMERG 322.4 mm, and CHIRPS 281.5 mm. Their mean is `(221.1 + 322.4 + 281.5) / 3 = 275.0 mm`, and their spread is `322.4 - 221.1 = 101.3 mm`.

ERA5-Land mean wind components are `u = 0.696863 m/s` and `v = 0.148988 m/s`. The vector speed is `sqrt(u^2 + v^2) = 0.713 m/s`; the bearing toward which the vector points is `atan2(u, v)` converted to degrees clockwise from north, or 77.9 degrees.

Sentinel-2 dNBR reports `no_sufficient_scenes`, with 0 pre scenes and 0 post scenes.

# Reasoning Path

The ledger passes the two numeric gates that define the smoke-window check: the local hazard-product coverage is at least 0.75 of the event window, and the report motif count is 7 of the 7 specified smoke, aerosol, burning, and satellite-tracking phrases. The precipitation ledger is contextual rather than controlling because the three precipitation products have a 101.3 mm spread and do not overturn the report motif and window tests. The wind calculation supplies a weak eastward transport anchor: positive u and v components give a 0.713 m/s vector pointing 77.9 degrees clockwise from north. The dNBR state blocks a local burn-scar reconstruction because no sufficient pre/post scenes are available.

# Computed Interpretation

The computed checks support a regional smoke-and-aerosol window with rainfall treated as contextual and local dNBR burn mapping treated as unavailable.

# Scoring Rubric

Total: 20 points.

- Window reconstruction (4 points): full credit computes the 61-day inclusive event window, the 46-day local product window, and the 0.754 coverage fraction. Partial credit: 1 point for each correct day count and 2 points for the correct fraction with an explicit inclusive-day formula.
- Report motif count (4 points): full credit finds all 7 listed smoke, aerosol, burning, and satellite-tracking motifs, including `burning of grass and shrubland`. Partial credit: proportional credit for each motif presence or absence handled correctly.
- Precipitation ledger (3 points): full credit uses the three precipitation means to compute 275.0 mm mean precipitation and 101.3 mm spread. Partial credit: 1 point for the three source means, 1 point for the mean, and 1 point for the spread.
- Wind vector calculation (3 points): full credit computes u = 0.697 m/s, v = 0.149 m/s, speed = 0.713 m/s, and bearing toward 77.9 degrees clockwise from north. Partial credit: credit for the component extraction, speed formula, and bearing formula.
- Burn-map availability check (2 points): full credit reports `no_sufficient_scenes` and does not treat a local dNBR map as available. Partial credit: 1 point for the status and 1 point for the correct implication.
- Consistency verdict (2 points): full credit states that the numeric ledger supports a regional smoke-and-aerosol window while keeping rainfall and local exposure context secondary. Partial credit: 1 point for the smoke-and-aerosol verdict and 1 point for not overextending other layers.
- Precision and limits (2 points): full credit uses requested units and rounding, and avoids quantified health-loss, crop-loss, or infrastructure-disruption statements that are not derived in the ledger. Partial credit: minor rounding or formatting issues that leave the calculations interpretable.

# Smoke-Window Consistency Ledger

A climate-smoke analyst is checking the September 2000 southern Africa fires and "river of smoke" episode. Rebuild a compact numeric ledger that tests whether the technical record coheres as a regional smoke-and-aerosol window rather than a local burn-scar reconstruction or rainfall-led episode.

Compute the following values:

1. Inclusive event-window days from the event anchor dates.
2. Local hazard-product days covered by the ERA5-Land aggregate window, plus that coverage as a fraction of the full event window.
3. The count of report motifs present across the NASA event and air-quality reports, using this motif list: `river of smoke`, `heat-absorbing aerosols`, `warming influence`, `heaviest burning`, `fire fronts 20 miles long`, `daily satellite maps`, `burning of grass and shrubland`.
4. The mean and spread of the three event-accumulated precipitation means from ERA5-Land, GPM IMERG, and CHIRPS, in millimeters.
5. The mean 10 m wind vector speed from the u and v components, and the bearing toward which the vector points in degrees clockwise from north.
6. The dNBR status and a one-sentence consistency verdict.

Return a JSON object with these keys:

```json
{
  "event_days": 0,
  "local_days": 0,
  "coverage_fraction": 0.0,
  "smoke_phrase_hits": 0,
  "precip_mm": {"mean": 0.0, "spread": 0.0},
  "wind_mps": {"u": 0.0, "v": 0.0, "speed": 0.0, "bearing_to_deg": 0.0},
  "dnbr_status": "",
  "consistency_verdict": ""
}
```

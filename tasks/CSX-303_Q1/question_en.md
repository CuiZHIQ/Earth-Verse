# Celia Saharan Dust Pathway Index

For the March 2022 Saharan dust episode over Spain, Portugal, and France, compute a deterministic pathway index that tests whether the event record supports a Storm Celia source-to-receptor dust pathway after checking common package-derived physical countermetrics. Treat the point rain, heat, wind, and annual surface-change values as countermetric diagnostics for the index, not as geolocation validation or direct impact measurements.

Use these definitions:

1. `event_days`: inclusive days from the locked start date through the locked end date.
2. `peak_fraction`: reported peak-window days inside the event window divided by `event_days`; a March 15-16 peak has two inclusive days.
3. `transport_anchor_count`: sum these six binary anchors: dust or sandstorm hazard family; Storm Celia plus North African air mass; passage through the Sahara; France, Spain, and Portugal all named as receptor countries; the reported peak window lies inside the locked event window; both air-quality and visibility impacts are present.
4. `rain_ratio = max(max point daily precipitation / 25, max regional mean event precipitation / 10)`.
5. `heat_ratio = max point or regional maximum 2 m temperature / 35`.
6. `wind_ratio = max available 10 m wind speed in m/s / 10`, converting km/h to m/s where needed.
7. `surface_ratio = max(annual embedding-change mean / 0.1, annual embedding-change max / 0.6)`.
8. `max_countermetric_ratio`: maximum of `rain_ratio`, `heat_ratio`, `wind_ratio`, and `surface_ratio`.
9. `dust_pathway_index = transport_anchor_count + peak_fraction + (1 - max_countermetric_ratio)`.

The threshold state is `celia_saharan_dust_pathway_pass` only when `transport_anchor_count == 6`, `peak_fraction >= 0.5`, `max_countermetric_ratio < 1`, and `dust_pathway_index >= 6.5`; otherwise use `countermetric_dominant`.

Return compact JSON with exactly these fields:

```json
{
  "event_days": 0,
  "peak_fraction": 0,
  "transport_anchor_count": 0,
  "max_countermetric_ratio": 0,
  "dust_pathway_index": 0,
  "conclusion": ""
}
```

Round ratios and the index to three decimals. Keep the conclusion as the short computed threshold label.

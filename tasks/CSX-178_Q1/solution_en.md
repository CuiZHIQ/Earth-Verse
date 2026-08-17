# Final Answer

```json
{
  "answer": "dry_hotspot_smoke_transport_signature",
  "metrics": {
    "reported_rain_fraction_of_normal": 0.25,
    "reported_fire_hotspots": 41000,
    "smoke_transport_anchor_count": 3
  },
  "computed_implication": "The 0.25 rainfall fraction, roughly 41000 hotspots, and three smoke-transport anchors identify a dry Nepal fire-smoke episode with broad satellite-observed smoke movement."
}
```

# Key Computations

The local report states that Nepal received just a quarter of its normal January-April rainfall. This is encoded as:

`reported_rain_fraction_of_normal = 0.25`

The report states that VIIRS detected roughly 41,000 hotspots in Nepal between January 1 and April 7, 2021:

`reported_fire_hotspots = 41000`

The report contains three smoke-transport anchors:

- smoke enveloping much of the mountainous country
- a smoke pall covering foothills and valleys near Pokhara
- the Himalayas directing smoke east toward India and Bangladesh

Therefore:

`smoke_transport_anchor_count = 3`

# Reasoning Path

The rainfall fraction supplies the dryness component, the hotspot count supplies the fire-activity burden, and the three smoke anchors connect that fire activity to observed smoke coverage and downwind movement. Together they support the compact label `dry_hotspot_smoke_transport_signature`.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns parseable JSON with top-level `answer`, `metrics`, and `computed_implication`, and includes all three requested metric keys.
- 3 points: Gives `dry_hotspot_smoke_transport_signature` or an accepted equivalent centered on dry conditions, hotspot burden, and smoke transport.
- 4 points: Extracts the reported quarter-normal rainfall and reports `0.25` within `0.001`.
- 3 points: Reports approximately `41000` VIIRS hotspots within 500 detections and treats the value as an approximate detection count.
- 3 points: Counts all three smoke-transport anchors: smoke over much of Nepal, smoke pall near Pokhara, and eastward transport toward India and Bangladesh.
- 2 points: Connects the three values to the final label without adding claims beyond the report-supported numeric signature.
- 2 points: Gives a one-sentence implication limited to dry conditions, hotspot detections, and smoke transport.

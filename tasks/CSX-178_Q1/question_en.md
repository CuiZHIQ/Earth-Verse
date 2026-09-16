# Nepal Fire-Smoke Reported Numeric Signature

A fire-weather analyst is preparing a compact numeric check for Nepal's forest-fire and smoke episode from 2021-03-26 through 2021-04-15. The note must combine three quantities from the local report record: the reported January-April rainfall fraction relative to normal, the reported VIIRS fire-hotspot count for Nepal through early April 2021, and the count of smoke-transport anchors connecting the fires to broad smoke coverage and downwind movement.

Compute those three values, assign the compact label that best fits the numeric signature, and keep the written implication to one sentence grounded in the computed values.

Return only JSON in this shape:

```json
{
  "answer": "<compact label>",
  "metrics": {
    "reported_rain_fraction_of_normal": <number from 0 to 1>,
    "reported_fire_hotspots": <integer>,
    "smoke_transport_anchor_count": <integer>
  },
  "computed_implication": "<one concise sentence>"
}
```

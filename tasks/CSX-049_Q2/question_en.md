# Hurricane Ida NYC Rainfall-Impact Score Ledger

A flood-risk analytics team is checking whether the September 1-2, 2021 Hurricane Ida record supports a compact rainfall-disruption-exposure signal for the New York City flooding episode. The task is not to recommend actions; it is to compute a score ledger from the event-window rainfall summaries, the report text, the population and infrastructure exposure slice, and the pre/post image-response summaries.

The exposure and infrastructure products in this package are spatially masked. Treat their derived population and feature-count statistics as authoritative package measurements. Do not use absolute coordinates, place names, bounding boxes, or georeferencing metadata inside masked exposure files to reject event-location validity.

Compute these diagnostics:

- `precip_peak_support_count`: count the three rainfall products whose event maximum passes its threshold: ERA5-Land >= 10 mm, GPM >= 18 mm, and CHIRPS >= 18 mm.
- `min_peak_to_mean_ratio`: the minimum of the ERA5, GPM, and CHIRPS event-maximum-to-mean precipitation ratios.
- `report_flag_count`: count six report flags: road shutdowns, public transit disruption, flight cancellations, stranded cars, high-water rescues, and flash-flood emergency statements.
- `population_sum`: the exposure population total, rounded to the nearest person.
- `infrastructure_counts`: count highway-tagged elements and amenity-tagged elements in the small roads and critical amenities slice.
- `image_response`: compute Sentinel-1 VV response range as `max - min`, and compute annual embedding max-to-mean ratio as `max / mean`.
- `score_0_to_5`: add one point each for rainfall support count equal to 3, report flag count at least 5, population at least 50,000, at least 10 highway elements and at least one amenity, and both image-response tests passing (`s1_vv_range_db >= 25` and `embedding_max_to_mean >= 20`).

Return only compact JSON:

```json
{
  "answer_label": "<label>",
  "precip_peak_support_count": 0,
  "min_peak_to_mean_ratio": 0.0,
  "report_flag_count": 0,
  "population_sum": 0,
  "infrastructure_counts": {
    "highway_elements": 0,
    "amenity_elements": 0
  },
  "image_response": {
    "s1_vv_range_db": 0.0,
    "embedding_max_to_mean": 0.0
  },
  "score_0_to_5": 0,
  "computed_interpretation": "<one sentence>"
}
```

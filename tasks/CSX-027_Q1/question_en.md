# CSX-027 Compound Heat-Water Process Diagnosis

A regional climate-risk team is reviewing the June-August 2022 China heat wave and drought. The question is not whether any single number crosses a screen. The task is to decide whether the package evidence supports a coupled heat-water stress process: persistent daytime heat load, failed nocturnal recovery, and rapid Poyang Lake drawdown occurring together, while weaker image-change signals do not explain the event by themselves.

Use only the local CSX-027 event package. Select package-relative source paths for every evidence family used in the final answer.

Compute the following evidence:

- Daytime heat load:
  - longest run of daily `Tmax >= 35 C`;
  - cumulative exceedance `sum(max(Tmax - 35, 0))`;
  - longest run of daily maximum apparent temperature `>= 40 C`.
- Nighttime recovery failure:
  - longest run of daily `Tmin >= 25 C`;
  - longest run of daily `Tmin >= 28 C`.
- Poyang Lake storage stress:
  - Xingzi Station water level on August 6;
  - Xingzi Station water level on August 30;
  - water-level drop;
  - average daily drop rate over the August 6 to August 30 interval;
  - how many days earlier than usual the dry-season level arrived.
- Proxy-evidence check:
  - mean Sentinel-2 dNBR;
  - annual embedding mean change;
  - whether those image metrics are strong enough to make a burn-change or image-only explanation primary.

Then compare three explanations:

- `compound_heat_water_stress`;
- `peak_only_heat_episode`;
- `image_or_burn_change_primary`.

Return exactly one JSON object with these top-level fields:

```json
{
  "answer": "<compact diagnosis>",
  "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD", "days": 0},
  "computed_evidence": {
    "daytime_heat_load": {},
    "nighttime_recovery": {},
    "poyang_storage_stress": {},
    "proxy_evidence_check": {}
  },
  "mechanism_chain": [
    {"stage": "<stage name>", "evidence": {}, "process_role": "<why it matters>"}
  ],
  "evidence_weighting": {
    "decisive": [],
    "contextual": [],
    "insufficient_as_primary": []
  },
  "counterfactual_tests": [
    {"hypothesis": "<alternative>", "ruling": "<accepted_or_rejected>", "reason": "<calculation-linked reason>"}
  ],
  "bounded_interpretation": "<one sentence>",
  "source_paths": ["<package-relative path>"]
}
```

Use `compound_heat_water_stress` only if the heat-persistence evidence, failed nighttime recovery evidence, and Poyang storage-stress evidence jointly support the coupled process, while the image metrics remain too weak to make an image-only or burn-change explanation primary. Round heat-load values to one decimal, water levels and drops to two decimals, water-level drop rate to three decimals, and image-change values to three decimals.

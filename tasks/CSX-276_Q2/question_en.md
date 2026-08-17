# Remote-Sensing Interpretation During the 2015-2016 Southern Africa Drought

A drought-analysis team is preparing a technical note on the 2015-2016 El Nino-linked drought across Southern Africa drylands. A two-date true-color image comparison shows a surface-appearance change, while climate indicators and briefing evidence describe a strongly coupled ENSO episode.

Decide how an expert should interpret the image-pair signal for disaster reasoning. Distinguish contextual visual support for drier or vegetation-stressed surface conditions from overclaims that a two-date true-color comparison alone proves regional drought severity, and reject unrelated interpretations such as flood damage or wildfire smoke if the physical chain does not support them.

Return compact JSON:

```json
{
  "interpretation": "<compact_label>",
  "image_change": {
    "brightness_delta": "<value>",
    "green_ratio_delta": "<value>"
  },
  "diagnostic_chain": ["<image observation>", "<climate context>", "<expert caution>"]
}
```

Base the answer on the incident record and do not add outside source claims.

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to deepen the drought interpretation by treating true-color imagery as contextual evidence constrained by ENSO and report evidence.


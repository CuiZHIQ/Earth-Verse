# Smoke-Haze Mechanism and Response Priority

A regional emergency-analysis cell is preparing a September 2019 briefing on the Indonesian smoke and haze episode affecting Sumatra, Kalimantan, Malaysia, and Singapore. The team needs a concise technical diagnosis that distinguishes a transboundary smoke-haze emergency from other plausible disaster framings before setting response priority.

Decide which mechanism should drive the emergency interpretation: dry-weather fire-smoke haze transport, rainfall flooding, volcanic ashfall, or a heat-only episode. Then assign a response priority of `high`, `moderate`, or `low` by weighing hazard persistence, transport beyond the source regions, package-derived exposed people or critical-place context, and what the imagery contributes as smoke-haze context rather than direct health-loss or damage measurement.

Return a JSON object with exactly these keys:

```json
{
  "mechanism_label": "string",
  "response_priority": "string",
  "key_findings": ["string"],
  "impact_chain": "string",
  "imagery_interpretation": "string",
  "priority_rationale": "string"
}
```

Keep `key_findings` to 3-5 short entries. Include only numeric anchors that materially change the priority diagnosis.

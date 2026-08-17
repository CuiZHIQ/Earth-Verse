# First-Response Mechanism Prioritization

On 26 December 2004, a major offshore geophysical event near Sumatra-Andaman triggered several possible response framings across nearby and distant coasts. A regional emergency coordination team needs a concise technical briefing on which physical disaster mechanism should drive the immediate first-response priority.

Decide which response framing is best supported by the local materials: basin-scale coastal life safety, local shaking response, rainfall or ordinary flood response, or image-change reconnaissance. Support the decision with quantitative anchors, a causal mechanism chain, arrival-time pressure, coastal impact logic, and the exposed-population context.

Return a compact JSON answer:

```json
{
  "answer": "<compact_priority_label>",
  "mechanism_chain": ["<trigger>", "<physical_process>", "<impact_pathway>"],
  "priority_rationale": "<two or three concise sentences>",
  "key_findings": ["<brief finding>", "<brief finding>", "<brief finding>"],
  "rejected_interpretations": ["<label>", "<label>", "<label>"]
}
```

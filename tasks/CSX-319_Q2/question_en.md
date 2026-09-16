# Surface-Change Consistency Ledger

During the July-September 2016 Aru Range glacier-collapse crisis in western Tibet, compute a compact threshold ledger for the surface-change and warm-wet loading record.

Use these formulas:

- `radar_margin_db = abs(mean VV post-minus-pre dB) - 2.0`
- `dnbr_margin = 0.10 - abs(mean dNBR)`
- `dnbr_mean_to_max = abs(mean dNBR) / max dNBR`
- `precip_3source_mean_mm = mean(the three event-accumulated precipitation means)`
- `warm_wet_score = int(precip_3source_mean_mm >= 100) + int(mean daily maximum temperature C >= 30)`
- `ledger_score = int(radar_margin_db >= 0) + int(dnbr_margin >= 0) + int(dnbr_mean_to_max <= 0.10) + warm_wet_score`

Return JSON:

```json
{
  "answer": {
    "radar_margin_db": 0.0,
    "dnbr_margin": 0.0,
    "dnbr_mean_to_max": 0.0,
    "precip_3source_mean_mm": 0.0,
    "warm_wet_score": 0,
    "ledger_score": 0,
    "classification": ""
  },
  "interpretation": "<one sentence tied to the computed ledger>"
}
```

# Final Answer

```json
{
  "formula": "early_spread_score = A * (E / N) * Hkha; late_moderation_score = M * ((N - E) / N) * 5 * C",
  "mechanism_competition": [
    {
      "mechanism": "early_dry_wind_fire_spread",
      "supporting_values": {
        "A_report_anchor_count": 3,
        "E_early_active_days": 4,
        "N_event_days": 10,
        "H_burned_area_kha": 17.0,
        "score": 20.4
      },
      "status": "dominant"
    },
    {
      "mechanism": "late_wind_slackening_fog_moderation",
      "supporting_values": {
        "M_moderation_anchor_count": 3,
        "late_days": 6,
        "continuation_discount": 0.5,
        "score": 4.5
      },
      "status": "secondary_moderation_not_dominant"
    }
  ],
  "phase_scores": {
    "early_spread_score": 20.4,
    "late_moderation_score": 4.5,
    "early_late_ratio": 4.53
  },
  "top_evidence_stage": "early_dry_wind_fire_spread",
  "first_moderation_day": "2022-03-07",
  "diagnosis": "early_dry_wind_spread_dominant",
  "computed_consequence": "The early dry-wind mechanism dominates because the report gives all early spread anchors, large burned area, and continued fire detection even on the first moderation day."
}
```

# Key Computations

The event window is March 4-13, 2022, so `N = 10` inclusive days.

Early spread anchors:

- dry weather: present
- strong winds: present
- westerly smoke transport toward southern Japan: present

Therefore `A = 3`.

The first moderation day is March 7, when the report says smoke had thinned, winds slackened, and the weather turned foggy. The same passage still says satellites continued to detect fire activity, so `C = 0.5`.

The early active interval is March 4 through March 7 inclusive: `E = 4`. The late remainder is `N - E = 6`.

The report states that nearly 17,000 hectares were charred, so `Hkha = 17.0`.

Scores:

- `early_spread_score = 3 * (4 / 10) * 17.0 = 20.40`
- `late_moderation_score = 3 * (6 / 10) * 5 * 0.5 = 4.50`
- `early_late_ratio = 20.40 / 4.50 = 4.53`

# Reasoning Path

The early mechanism is dominant because the report contains all three early spread anchors, the early active interval covers four event-window days, and the reported burned area is large. The late moderation mechanism is real but secondary: March 7 brought thinner smoke, weaker winds, and fog, but satellites still detected fire activity, so the moderation evidence is discounted.

The dominance rule passes because the early score is higher than the late moderation score, the ratio is above `1.5`, and fire activity continued on the first moderation day.

# Scoring Rubric

- 3 points: Provides the requested JSON mechanism competition and final diagnosis `early_dry_wind_spread_dominant`.
- 4 points: Finds all three early anchors: dry weather, strong winds, and westerly smoke transport toward southern Japan.
- 3 points: Finds smoke thinning, winds slackening, foggy weather, and continued fire activity on March 7.
- 4 points: Computes `N = 10`, `E = 4`, `late_days = 6`, `Hkha = 17.0`, early fraction `0.4`, and late fraction `0.6`.
- 3 points: Computes early score `20.40`, late score `4.50`, ratio `4.53`, and applies the `>= 1.5` dominance rule.
- 2 points: Keeps the consequence tied to the computed mechanism competition rather than action guidance or broad wildfire explanation.
- 1 point: Avoids claiming calibrated fire danger, exact perimeter, exact smoke dose, or measured health impact.

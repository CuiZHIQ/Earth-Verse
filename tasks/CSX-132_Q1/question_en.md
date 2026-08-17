# Northern Italy Giant-Hail Severity Ledger

In July 2023, severe storms over northern Italy produced record-size hail and reported human impacts. A climate-risk analyst is preparing a compact technical note that must decide which signal should headline the event summary: reported giant hail, rain/wind metrics, or broad image-change context.

Using the technical record and quantitative diagnostics, return a compact JSON-like answer with these fields:

- `headline_signal`: a short label.
- `hail_ledger`: maximum hail size, giant-hail threshold multiple, Italy share of giant-hail reports, and injuries per giant-hail report.
- `weather_context`: one or two rain/wind numbers and how they compare with the hail ledger.
- `image_context`: whether the imagery and change statistics provide a direct damage count or only context.
- `one_sentence_conclusion`: one sentence tying the ledger together.

Keep the answer concise. Do not add exact monetary, crop, vehicle, roof, or building-loss counts unless they are derived from the computations.

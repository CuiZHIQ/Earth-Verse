# Indus Flood Persistence Ledger

A hydrometeorology team is preparing a technical note on the July-August 2010 Pakistan Indus River floods. The team needs a calculation-first check of whether the record is consistent with a persistent monsoon-driven basin flood signal rather than a short isolated rain burst.

Use the inclusive event window 2010-07-27 through 2010-08-31. Build a compact JSON answer with:

- `event_window_days` and `event_window_hours`.
- `core_metrics`: July and August rainfall anomalies, their ratio and mean, GPM and CHIRPS event precipitation means with their difference and ratio, hourly precipitation sum, wet-hour count, wet-hour share, wet-hour mean, maximum-hour share, flooded extent, affected people, affected people per flooded square kilometer, deaths per 1,000 affected people, houses per affected person, catalog start date, alert level, and severity.
- `tests`: pass/fail states for monthly anomaly persistence, precipitation product agreement, wet-hour persistence, basin-scale impact magnitude, and catalog severity alignment.
- `final_label`: one concise consistency label.
- `basis`: one sentence tying the label to the computed values.

Treat the hourly wet-hour persistence metric as point-series timing evidence only, not as a basin-wide wet-area fraction. Treat the reported flood extent, affected population, deaths, and housing damage as national lower-bound impact context from the event report, not as exact impact totals confined only to the point-weather window.

Use these decision rules: the monthly test passes if both monthly anomalies are at least 50 percent above normal and their mean is at least 75 percent; the precipitation product test passes if CHIRPS/GPM is within 0.9-1.1; the wet-hour test passes if at least 150 event hours have nonzero precipitation; the impact test passes if flooded extent is at least 30,000 square kilometers and affected population is at least 10 million; the catalog test passes if the event begins on 2010-07-27, has RED alert level, and severity is at least 7.

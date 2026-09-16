# Final Answer

The correct canonical label is `late_august_active_fire_smoke_phase`.

A full-credit compact answer should report image date `2023-08-22`, weather/smoke context date `2023-08-23`, and the score ledger:

```json
{
  "late_august_active_fire_smoke": 5,
  "annual_burned_area_context": 1,
  "athens_only_local_fire": 1
}
```

# Key Computations

The reproducible extraction uses `metadata/event.json`, `data/event_reports/event_reports_003_Locked_event_anchor_2023_Greece_wildfires.json`, and `data/event_reports/event_reports_005_NASA_Earth_Observatory_wildfires_rage_in_Greece.html`.

The five active-fire/smoke anchors are all present:

- late-August fires: the report says dozens more fires ignited within 24 hours in late August 2023;
- plume direction: a fire near Alexandroupolis produced a plume stretching southwest toward Italy;
- image date: the satellite observation date is `2023-08-22`;
- weather context: forecasts called for hot, dry, windy fire weather to continue on `2023-08-23`;
- smoke extension: by that day, smoke was detected over Italy and across the Mediterranean Sea in northern Africa.

The annual burned-area context score is 1 because the report includes an EFFIS comparison saying the area burned in Greece so far in 2023 had surpassed the 2021 fire season. The Athens-only score is 1 because the report says fires near Athens burned homes and cars and sent smoke over the capital.

# Reasoning Path

First, extract the two dates: `2023-08-22` from the satellite image observation and `2023-08-23` from the next-day fire-weather and smoke paragraph.

Second, compute the active-fire/smoke score as a five-item count. Each of the requested late-August fire, Alexandroupolis plume, image-date, fire-weather, and broader smoke-extension anchors is present, so the score is 5.

Third, compute the comparison scores. Annual burned-area context earns 1 point, and Athens-local impact earns 1 point. Neither comparison score exceeds the five-anchor active-fire/smoke score.

Therefore the best code is `late_august_active_fire_smoke_phase`, with annual burned area and Athens impacts treated as supporting context rather than the main late-August phase code.

# Computed Interpretation

The late-August record is best summarized as an active-fire and smoke-transport phase anchored by dated satellite/report observations, with annual burned-area comparison and Athens impacts as secondary context.

# Scoring Rubric

Award 20 points:

- 3 points for the final canonical label `late_august_active_fire_smoke_phase`; partial credit for choosing an active-fire/smoke label with wording differences but losing the exact canonical label.
- 3 points for the date ledger with `image_date = 2023-08-22` and `weather_smoke_context_date = 2023-08-23`; partial credit for one correct date or correct month/day without ISO formatting.
- 4 points for computing `late_august_active_fire_smoke = 5` from all five report-backed anchors; partial credit for a score of 3 or 4 with the missing anchors identifiable.
- 3 points for computing `annual_burned_area_context = 1` and `athens_only_local_fire = 1`; partial credit for recognizing one of the two comparison anchors.
- 3 points for naming at least three event-specific anchors among late-August fires, Alexandroupolis-to-Italy plume, hot/dry/windy fire weather, Italy/northern Africa smoke, and Athens homes/cars/smoke; partial credit for generic wildfire wording with one or two specific anchors.
- 2 points for explaining why the five-anchor score selects the active-fire/smoke code over the comparison codes; partial credit for the correct label without explicit score comparison.
- 2 points for compact JSON-like structure without adding casualty, health-burden, or national damage totals; partial credit for correct content in prose rather than the requested structure.

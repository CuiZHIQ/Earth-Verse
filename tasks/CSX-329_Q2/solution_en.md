# Correct Answer

```json
{
  "answer": "recent_7day_alert_heat_stress_consistent",
  "alert_support_score": 12,
  "event_days": 92,
  "baa_window_days": 7,
  "context_scores": {
    "single_day": 0,
    "land_precip_exposure": 5,
    "surface_change": 0
  },
  "margins": {
    "alert_minus_land": 7,
    "alert_minus_surface": 12,
    "event_to_baa_ratio": 13.143
  },
  "threshold_result": "pass_alert_dominance",
  "rejected_alternative": "single_day_land_surface_proxy"
}
```

# Computation

The inclusive event window from 2020-08-01 through 2020-10-31 is 92 days. The heat-stress product uses a 7-day recent maximum Bleaching Alert Area memory window, so `event_to_baa_ratio = 92 / 7 = 13.143`.

The `alert_support_score` is 12 because all twelve binary checks are present: marine heatwave/coastal ecosystem family, Alert Level 2 wording, the Taiwan/Japan/South China Sea location triad, recent August elevation, severe bleaching and mortality wording, separable later Guam/Micronesia outlook, HotSpot, Degree Heating Week, Bleaching Alert Area, recent maximum wording, single-day inadequacy/day-to-day fluctuation wording, and accumulated heat-stress impact wording.

The single-day ledger is `HotSpot_term - single_day_inadequacy_flag = 1 - 1 = 0`. The land/precipitation/exposure ledger is 5 because GPM mean precipitation is 451.939 mm, CHIRPS mean precipitation is 369.486 mm, ERA5-Land maximum 2 m temperature is 34.557 C, WorldPop population is 11,395,560.236, and road-like OSM features total 818. The surface-change ledger is 0 because mean dNBR is -0.108468, below 0.25, and AlphaEarth mean annual change is 0.028310, below 0.10.

The resulting margins are `alert_minus_land = 12 - 5 = 7` and `alert_minus_surface = 12 - 0 = 12`. All pass thresholds are satisfied, so the compact diagnosis is `recent_7day_alert_heat_stress_consistent`; the rejected computed consequence is `single_day_land_surface_proxy`.

# Scoring Rubric (20 points)

- 4 points: Returned JSON has the requested fields, nested score objects, exact pass/fail label, and no added prose in the final object.
- 5 points: Alert ledger is computed correctly as 12, with the 12 binary checks grounded in the event family, event wording, and heat-stress product wording.
- 4 points: Numeric context ledgers are correct: single-day score 0, land/precipitation/exposure score 5, and surface-change score 0, with the precipitation, temperature, population, road, dNBR, and AlphaEarth thresholds applied correctly.
- 4 points: Formula margins and duration ratio are correct: 92 event days, 7 memory-window days, `alert_minus_land = 7`, `alert_minus_surface = 12`, and `event_to_baa_ratio = 13.143`.
- 2 points: The rejected computed consequence follows from the ledgers and does not let land/rain/population or surface-change proxies set reef heat-stress severity.
- 1 point: The mechanism label is concise and tied to the threshold result without broad narration.

# Severe-Convection Threshold Ledger

During the March 31-April 1, 2023 U.S. tornado outbreak, a severe-storm verification team is checking whether the northern Illinois and northwest Indiana corridor crossed a pre-defined convective-impact ledger. Reconstruct the event-window ledger from the local storm record and gridded precipitation diagnostics.

Return a JSON object with exactly these keys:

- `window`: the event window as `YYYY-MM-DD/YYYY-MM-DD`.
- `local_tornadoes`: confirmed tornado count in the local forecast area.
- `ef_counts`: an object with `ef1` and `ef2_plus`.
- `casualty_total`: fatalities plus injuries from the casualty-producing local site.
- `wind_damage`: an object with `max_mph` and `place_count` for named straight-line-wind damage locations.
- `max_precip_mm`: maximum event accumulated precipitation across the gridded precipitation summaries, rounded to 0.001 mm.
- `gates`: booleans for `tornado_core`, `casualty`, `wind_spread`, and `precip_complication`, using these formulas:
  - `tornado_core = local_tornadoes >= 20 and ef2_plus >= 3`
  - `casualty = casualty_total >= 40`
  - `wind_spread = max_mph >= 80 and place_count >= 10`
  - `precip_complication = max_precip_mm >= 35`
- `conclusion`: `passes_convective_impact_ledger` only if all four gates are true; otherwise `fails_convective_impact_ledger`.

After the JSON, add no more than two concise sentences explaining the arithmetic.

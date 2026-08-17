# Koror Water-Stress Index Check

A regional health-risk analysis team is auditing the 2015-2016 El Nino drought signal for Koror, Palau. Determine whether the local rainfall deficit and acute drinking-water reports meet a capped maximum-stress diagnosis under the task-specific Water-Stress Priority Index (WSPI).

Use the following calculation:

`deficit_share = rainfall_below_average_inches / (rainfall_observed_inches + rainfall_below_average_inches)`

`uncapped_WSPI = deficit_share + 0.10 * acute_water_supply_trigger_count`

`WSPI = min(1.0, uncapped_WSPI)`

Count an acute water-supply trigger only when it is supported for Koror or Palau during the event:

- the main dam supplying Koror dried up
- the other drinking-water source was very low
- water rationing had begun

Use `threshold_state = "capped_maximum"` when the uncapped WSPI is at least 1.0 and the capped WSPI is 1.000. Set `final_label = "acute_freshwater_drought_health_stress"` only when the threshold state is capped maximum and all three triggers are true.

Return compact JSON with exactly these top-level fields:

`target_family`, `rainfall`, `triggers`, `wspi`, `threshold_state`, `final_label`

Round `deficit_share`, `uncapped_WSPI`, and `WSPI` to three decimals.

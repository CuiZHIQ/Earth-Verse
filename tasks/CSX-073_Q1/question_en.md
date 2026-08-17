# Hurricane Ida Rainfall Concentration Test

During September 1-2, 2021, remnants of Hurricane Ida produced extreme rainfall over New York City. A hydrometeorology review team is testing whether the event is better described by concentrated urban pluvial drainage overload than by a daily-total-only flood account.

Compute a compact diagnostic ledger from the rainfall and city-service records. Return JSON with exactly these keys: `label`, `total_mm`, `peak_hour_mm`, `peak_hour_time`, `peak_hour_share`, `hours_ge_10mm`, `max_run_hours_ge_5mm`, `sewer_share`, and `central_park_peak_in`. Use the label `drainage_overload_pluvial` only if the peak hour supplies at least 20% of the event rainfall, at least 3 hours reach 10 mm or more, the longest run at 5 mm or more is at least 4 hours, and sewer complaints are at least 85% of the flood-related service records. After the JSON, add one sentence explaining what the ledger means for the flood mechanism.

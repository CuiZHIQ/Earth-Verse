from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'C Tables and Time Series'
__all__ = [
    'load_table_schema',
    'filter_table_rows',
    'select_table_columns',
    'normalize_time_column',
    'resample_timeseries',
    'compute_time_window_stats',
    'compute_rolling_sum',
    'compute_rolling_mean',
    'detect_consecutive_exceedance',
    'compute_lagged_peak',
    'compare_event_to_baseline_percentile',
    'detect_event_peak_window',
    'join_timeseries_on_time',
    'compute_anomaly_from_climatology',
    'compute_percentile_rank',
    'export_intermediate_table',
    'summarize_table_or_json',
    'compute_unit_conversion_or_ratio',
]

def load_table_schema(**kwargs: Any) -> dict[str, Any]:
    """load_table_schema

Kit: C Tables and Time Series
Purpose: Inspect table fields, data types, row count, samples and likely units.
Inputs: path
Output: schema JSON
Used by: tabular tasks
"""
    return dispatch('load_table_schema', **kwargs)

def filter_table_rows(**kwargs: Any) -> dict[str, Any]:
    """filter_table_rows

Kit: C Tables and Time Series
Purpose: Filter rows by explicit conditions on time, region, source or variable.
Inputs: path, conditions
Output: filtered rows summary
Used by: event-window selection
"""
    return dispatch('filter_table_rows', **kwargs)

def select_table_columns(**kwargs: Any) -> dict[str, Any]:
    """select_table_columns

Kit: C Tables and Time Series
Purpose: Select needed columns and report missing columns clearly.
Inputs: path, columns
Output: subtable summary
Used by: field selection
"""
    return dispatch('select_table_columns', **kwargs)

def normalize_time_column(**kwargs: Any) -> dict[str, Any]:
    """normalize_time_column

Kit: C Tables and Time Series
Purpose: Parse and normalize time columns to UTC or local event time.
Inputs: path, time_col, timezone?
Output: normalized table
Used by: time alignment
"""
    return dispatch('normalize_time_column', **kwargs)

def resample_timeseries(**kwargs: Any) -> dict[str, Any]:
    """resample_timeseries

Kit: C Tables and Time Series
Purpose: Resample hourly/daily/monthly series with mean, max, min or sum.
Inputs: path, time_col, freq, agg
Output: resampled series
Used by: multi-source alignment
"""
    return dispatch('resample_timeseries', **kwargs)

def compute_time_window_stats(**kwargs: Any) -> dict[str, Any]:
    """compute_time_window_stats

Kit: C Tables and Time Series
Purpose: Compute event-window min, max, mean, sum and date of peak.
Inputs: path, time_col, value_cols, start, end
Output: window stats
Used by: most tasks
"""
    return dispatch('compute_time_window_stats', **kwargs)

def compute_rolling_sum(**kwargs: Any) -> dict[str, Any]:
    """compute_rolling_sum

Kit: C Tables and Time Series
Purpose: Compute rolling accumulation and its peak window.
Inputs: path, time_col, value_col, window
Output: rolling sum stats
Used by: rain/flood
"""
    return dispatch('compute_rolling_sum', **kwargs)

def compute_rolling_mean(**kwargs: Any) -> dict[str, Any]:
    """compute_rolling_mean

Kit: C Tables and Time Series
Purpose: Compute rolling mean and its peak or trough window.
Inputs: path, time_col, value_col, window
Output: rolling mean stats
Used by: heat/smoke/drought
"""
    return dispatch('compute_rolling_mean', **kwargs)

def detect_consecutive_exceedance(**kwargs: Any) -> dict[str, Any]:
    """detect_consecutive_exceedance

Kit: C Tables and Time Series
Purpose: Find longest run above or below a threshold.
Inputs: path, time_col, value_col, threshold, op
Output: run-length stats
Used by: persistence
"""
    return dispatch('detect_consecutive_exceedance', **kwargs)

def compute_lagged_peak(**kwargs: Any) -> dict[str, Any]:
    """compute_lagged_peak

Kit: C Tables and Time Series
Purpose: Find response lag between driver and impact series.
Inputs: driver_series, response_series, lags
Output: best lag and correlation
Used by: flood/smoke/311
"""
    return dispatch('compute_lagged_peak', **kwargs)

def compare_event_to_baseline_percentile(**kwargs: Any) -> dict[str, Any]:
    """compare_event_to_baseline_percentile

Kit: C Tables and Time Series
Purpose: Compare event values with baseline percentile threshold.
Inputs: event_values, baseline_values, percentile
Output: exceedance result
Used by: extremeness
"""
    return dispatch('compare_event_to_baseline_percentile', **kwargs)

def detect_event_peak_window(**kwargs: Any) -> dict[str, Any]:
    """detect_event_peak_window

Kit: C Tables and Time Series
Purpose: Detect most dangerous window using a metric and duration.
Inputs: series, metric, window
Output: peak window
Used by: response timing
"""
    return dispatch('detect_event_peak_window', **kwargs)

def join_timeseries_on_time(**kwargs: Any) -> dict[str, Any]:
    """join_timeseries_on_time

Kit: C Tables and Time Series
Purpose: Join multiple time series on normalized time.
Inputs: paths, time_cols, join_type
Output: joined table
Used by: multi-source tasks
"""
    return dispatch('join_timeseries_on_time', **kwargs)

def compute_anomaly_from_climatology(**kwargs: Any) -> dict[str, Any]:
    """compute_anomaly_from_climatology

Kit: C Tables and Time Series
Purpose: Compute anomaly relative to monthly or daily climatology.
Inputs: event_series, climatology
Output: anomaly series
Used by: climate tasks
"""
    return dispatch('compute_anomaly_from_climatology', **kwargs)

def compute_percentile_rank(**kwargs: Any) -> dict[str, Any]:
    """compute_percentile_rank

Kit: C Tables and Time Series
Purpose: Return percentile rank of event value in a historical distribution.
Inputs: value, baseline_values
Output: percentile rank
Used by: GT metrics
"""
    return dispatch('compute_percentile_rank', **kwargs)

def export_intermediate_table(**kwargs: Any) -> dict[str, Any]:
    """export_intermediate_table

Kit: C Tables and Time Series
Purpose: Write a derived table for trace reproducibility.
Inputs: dataframe, relative_output_path
Output: artifact path
Used by: time-series inspection
"""
    return dispatch('export_intermediate_table', **kwargs)

def summarize_table_or_json(**kwargs: Any) -> dict[str, Any]:
    """summarize_table_or_json

Kit: C Tables and Time Series
Purpose: Summarize CSV, TSV, JSON, or nested JSON files with row count, columns, numeric fields, and representative records.
Inputs: path, max_rows?, numeric_summary?
Output: table/JSON summary with numeric anchors
Used by: JSON and table parsing
"""
    return dispatch('summarize_table_or_json', **kwargs)

def compute_unit_conversion_or_ratio(**kwargs: Any) -> dict[str, Any]:
    """compute_unit_conversion_or_ratio

Kit: C Tables and Time Series
Purpose: Convert common disaster-analysis units and compute ratios such as max/mean, point/grid, and event/baseline contrasts.
Inputs: value?, from_unit?, to_unit?, numerator?, denominator?
Output: converted value and/or ratio
Used by: numeric anchor normalization
"""
    return dispatch('compute_unit_conversion_or_ratio', **kwargs)

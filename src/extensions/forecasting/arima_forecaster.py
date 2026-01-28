"""
ARIMA forecasting extension.
Requires the optional dependency: statsmodels.
"""

from typing import Dict, Any, Tuple, List
import logging

import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class ForecastError(Exception):
    """Raised when a forecast cannot be produced."""


def _infer_future_dates(index: pd.DatetimeIndex, steps: int) -> List[str]:
    if index is None or len(index) == 0:
        raise ForecastError("No index to build forecast dates")
    has_weekend = any(ts.weekday() >= 5 for ts in index)
    freq = "D" if has_weekend else "B"
    start = index[-1] + pd.Timedelta(days=1)
    future_index = pd.date_range(start=start, periods=steps, freq=freq)
    return future_index.strftime("%Y-%m-%d").tolist()


def forecast_close_prices(
    historical_data: pd.DataFrame,
    steps: int = 14,
    order: Tuple[int, int, int] = (1, 1, 1),
    alpha: float = 0.4,
    trend: str = "t",
    use_log: bool = True
) -> Dict[str, Any]:
    """
    Forecast future close prices using ARIMA.
    
    Returns a dict with:
      - dates: list[str]
      - mean: list[float]
      - lower: list[float]
      - upper: list[float]
      - order: tuple[int, int, int]
      - steps: int
    """
    if historical_data is None or historical_data.empty:
        raise ForecastError("No historical data")
    if "Close" not in historical_data.columns:
        raise ForecastError("Missing Close column")
    
    series = historical_data["Close"].dropna()
    min_points = max(20, sum(order) + 5)
    if len(series) < min_points:
        raise ForecastError("Not enough data for ARIMA")
    if not (0.0 < alpha < 1.0):
        raise ForecastError("alpha must be between 0 and 1")
    
    if use_log:
        if (series <= 0).any():
            raise ForecastError("Close values must be positive for log transform")
        series = np.log(series)
    
    try:
        from statsmodels.tsa.arima.model import ARIMA
    except Exception as exc:
        raise ForecastError("statsmodels is required for ARIMA forecasting") from exc
    
    model = ARIMA(
        series,
        order=order,
        trend=trend,
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    results = model.fit()
    forecast = results.get_forecast(steps=steps)
    
    mean = forecast.predicted_mean
    conf_int = forecast.conf_int(alpha=alpha)
    lower = conf_int.iloc[:, 0]
    upper = conf_int.iloc[:, 1]
    
    if use_log:
        mean = np.exp(mean)
        lower = np.exp(lower)
        upper = np.exp(upper)
    
    if isinstance(mean.index, pd.DatetimeIndex):
        dates = mean.index.strftime("%Y-%m-%d").tolist()
    else:
        dates = _infer_future_dates(series.index, steps)
    
    return {
        "dates": dates,
        "mean": mean.tolist(),
        "lower": lower.tolist(),
        "upper": upper.tolist(),
        "order": order,
        "steps": steps
    }

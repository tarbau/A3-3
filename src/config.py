"""
Configuration management for the financial analyzer application.
Handles environment variables and application settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def _parse_arima_order(raw_value: str) -> tuple:
    """Parse ARIMA order from a comma-separated string like '1,1,1'."""
    if not raw_value:
        return (1, 1, 1)
    parts = [p.strip() for p in raw_value.split(",") if p.strip()]
    if len(parts) != 3:
        return (1, 1, 1)
    try:
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError:
        return (1, 1, 1)


def _parse_float(raw_value: str, default: float) -> float:
    try:
        return float(raw_value)
    except (TypeError, ValueError):
        return default


class Config:
    """Application configuration class."""
    
    # Alpha Vantage API (optional)
    ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "")
    
    # Flask configuration
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    
    # Data fetching settings
    DEFAULT_PERIOD = "1y"  # 1 year of historical data
    DEFAULT_INTERVAL = "1d"  # Daily interval
    
    # Forecasting settings (optional, requires statsmodels)
    ENABLE_ARIMA_FORECAST = os.getenv("ENABLE_ARIMA_FORECAST", "false").lower() == "true"
    FORECAST_STEPS = int(os.getenv("FORECAST_STEPS", "14"))
    ARIMA_ORDER = _parse_arima_order(os.getenv("ARIMA_ORDER", "1,1,1"))
    ARIMA_TREND = os.getenv("ARIMA_TREND", "t")
    FORECAST_ALPHA = _parse_float(os.getenv("FORECAST_ALPHA", "0.2"), 0.2)
    FORECAST_USE_LOG = os.getenv("FORECAST_USE_LOG", "true").lower() == "true"
    
    # Supported periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    # Supported intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo


# Create a global config instance
config = Config()

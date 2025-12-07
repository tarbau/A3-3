"""
Data fetching module for financial data.
Uses yfinance library to fetch stock and cryptocurrency data.
"""

import logging
from typing import Optional, Dict, Any
import yfinance as yf
import pandas as pd
from datetime import datetime

from src.config import config
from src.utils import validate_ticker

# Set up logger
logger = logging.getLogger(__name__)


class DataFetcher:
    """Class for fetching financial data from various sources."""
    
    def __init__(self):
        """Initialize the DataFetcher."""
        self.logger = logging.getLogger(__name__)
    
    def fetch_data(
        self,
        ticker: str,
        period: str = None,
        interval: str = None
    ) -> Optional[yf.Ticker]:
        """
        Fetch ticker data using yfinance.
        
        Args:
            ticker: Stock or cryptocurrency ticker symbol
            period: Period of historical data (default: from config)
            interval: Data interval (default: from config)
            
        Returns:
            yfinance Ticker object or None if error
        """
        if not validate_ticker(ticker):
            self.logger.error(f"Invalid ticker symbol: {ticker}")
            return None
        
        ticker_upper = ticker.strip().upper()
        period = period or config.DEFAULT_PERIOD
        interval = interval or config.DEFAULT_INTERVAL
        
        try:
            self.logger.info(f"Fetching data for {ticker_upper}...")
            ticker_obj = yf.Ticker(ticker_upper)
            
            # Test if ticker is valid by trying to get info
            info = ticker_obj.info
            if not info or len(info) < 2:  # Empty or minimal info means invalid ticker
                self.logger.error(f"Ticker {ticker_upper} not found or invalid")
                return None
            
            self.logger.info(f"Successfully fetched data for {ticker_upper}")
            return ticker_obj
            
        except Exception as e:
            self.logger.error(f"Error fetching data for {ticker_upper}: {str(e)}")
            return None
    
    def get_current_price(self, ticker_obj: yf.Ticker) -> Optional[float]:
        """
        Get current price of the ticker.
        
        Args:
            ticker_obj: yfinance Ticker object
            
        Returns:
            Current price or None if error
        """
        try:
            info = ticker_obj.info
            # Try different possible keys for current price
            price = (
                info.get("currentPrice") or
                info.get("regularMarketPrice") or
                info.get("previousClose") or
                info.get("ask") or
                info.get("bid")
            )
            return float(price) if price else None
        except Exception as e:
            self.logger.error(f"Error getting current price: {str(e)}")
            return None
    
    def get_historical_data(
        self,
        ticker_obj: yf.Ticker,
        period: str = None,
        interval: str = None
    ) -> Optional[pd.DataFrame]:
        """
        Get historical price data.
        
        Args:
            ticker_obj: yfinance Ticker object
            period: Period of historical data (default: from config)
            interval: Data interval (default: from config)
            
        Returns:
            DataFrame with historical data or None if error
        """
        period = period or config.DEFAULT_PERIOD
        interval = interval or config.DEFAULT_INTERVAL
        
        try:
            self.logger.info(f"Fetching historical data (period: {period}, interval: {interval})...")
            hist = ticker_obj.history(period=period, interval=interval)
            
            if hist.empty:
                self.logger.warning("Historical data is empty")
                return None
            
            self.logger.info(f"Fetched {len(hist)} data points")
            return hist
            
        except Exception as e:
            self.logger.error(f"Error fetching historical data: {str(e)}")
            return None
    
    def get_company_info(self, ticker_obj: yf.Ticker) -> Dict[str, Any]:
        """
        Get company/cryptocurrency information.
        
        Args:
            ticker_obj: yfinance Ticker object
            
        Returns:
            Dictionary with company information
        """
        try:
            info = ticker_obj.info
            return {
                "name": info.get("longName") or info.get("shortName", "N/A"),
                "sector": info.get("sector", "N/A"),
                "industry": info.get("industry", "N/A"),
                "currency": info.get("currency", "USD"),
                "exchange": info.get("exchange", "N/A"),
                "market_cap": info.get("marketCap"),
                "description": info.get("longBusinessSummary", "N/A")
            }
        except Exception as e:
            self.logger.error(f"Error getting company info: {str(e)}")
            return {
                "name": "N/A",
                "sector": "N/A",
                "industry": "N/A",
                "currency": "USD",
                "exchange": "N/A",
                "market_cap": None,
                "description": "N/A"
            }


# Create a global instance
data_fetcher = DataFetcher()






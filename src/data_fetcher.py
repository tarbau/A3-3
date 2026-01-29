import logging
import yfinance as yf
import pandas as pd

from src.config import config
from src.utils import validate_ticker

logger = logging.getLogger(__name__)

class DataFetcher:
    """
    Fetches financial data using yfinance.
    """
    
    def __init__(self):
        """
        Initialize a DataFetcher instance.
        """
        self.logger = logging.getLogger(__name__)
    
    def fetch_data(self, ticker, period=None, interval=None):
        """
        Fetch a yfinance Ticker object.

        Args:
            ticker: Symbol like "AAPL" or "BTC-USD".
            period: Optional history period (uses config default if None).
            interval: Optional data interval (uses config default if None).

        Returns:
            yfinance.Ticker instance or None if invalid/failed.
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
            
            info = ticker_obj.info
            
            if not info or len(info) < 2:
                self.logger.error(f"Ticker {ticker_upper} not found or invalid")
                return None
            
            self.logger.info(f"Successfully fetched data for {ticker_upper}")
            return ticker_obj
            
        except Exception as e:
            error_message = str(e).lower()
            
            if any(word in error_message for word in ["connection", "network", "timeout", "unreachable", "refused"]):
                self.logger.error(f"No internet connection: {str(e)}")
                print("❌ ERROR: No internet connection!")
                print("   Please check your internet and try again.")
            else:
                self.logger.error(f"Error fetching data for {ticker_upper}: {str(e)}")
                print(f"❌ ERROR: {str(e)}")
            
            return None
    
    def get_current_price(self, ticker_obj):
        """
        Get the current price for a ticker.

        Args:
            ticker_obj: yfinance Ticker instance.

        Returns:
            Current price as float, or None.
        """
        try:
            info = ticker_obj.info
            
            price = info.get("currentPrice")
            
            if not price:
                price = info.get("regularMarketPrice")
            
            if not price:
                price = info.get("previousClose")
            
            if not price:
                price = info.get("ask")
            
            if not price:
                price = info.get("bid")
            
            if price:
                return float(price)
            return None
                
        except Exception as e:
            self.logger.error(f"Error getting current price: {str(e)}")
            return None
    
    def get_historical_data(self, ticker_obj, period=None, interval=None):
        """
        Get historical price data.

        Args:
            ticker_obj: yfinance Ticker instance.
            period: Optional history period (uses config default if None).
            interval: Optional data interval (uses config default if None).

        Returns:
            pandas.DataFrame with historical data, or None.
        """
        period = period or config.DEFAULT_PERIOD
        interval = interval or config.DEFAULT_INTERVAL
        
        try:
            self.logger.info(f"Fetching historical data (period: {period}, interval: {interval})...")
            
            historical_data = ticker_obj.history(period=period, interval=interval)
            
            if historical_data.empty:
                self.logger.warning("Historical data is empty")
                return None
            
            self.logger.info(f"Fetched {len(historical_data)} data points")
            return historical_data
            
        except Exception as e:
            self.logger.error(f"Error fetching historical data: {str(e)}")
            return None
    
    def get_company_info(self, ticker_obj):
        """
        Get company or crypto information.

        Args:
            ticker_obj: yfinance Ticker instance.

        Returns:
            dict with company information.
        """
        try:
            info = ticker_obj.info
            
            name = info.get("longName")
            if not name:
                name = info.get("shortName", "N/A")
            
            sector = info.get("sector", "N/A")
            industry = info.get("industry", "N/A")
            currency = info.get("currency", "USD")
            exchange = info.get("exchange", "N/A")
            market_cap = info.get("marketCap")
            description = info.get("longBusinessSummary", "N/A")
            
            company_info = {
                "name": name,
                "sector": sector,
                "industry": industry,
                "currency": currency,
                "exchange": exchange,
                "market_cap": market_cap,
                "description": description
            }
            
            return company_info
            
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


data_fetcher = DataFetcher()


"""
Data analysis module for calculating financial statistics.
"""

import logging
from typing import Dict, Any, Optional
import pandas as pd

from src.utils import format_currency, format_percentage



class FinancialAnalyzer:
    """Class for analyzing financial data and calculating statistics."""
    
    def __init__(self):
        """Initialize the FinancialAnalyzer."""
        self.logger = logging.getLogger(__name__)
    
    def calculate_statistics(
        self,
        historical_data: pd.DataFrame,
        current_price: Optional[float] = None,
        currency: str = "USD"
    ) -> Dict[str, Any]:
        """
        Calculate key financial statistics from historical data.
        
        Args:
            historical_data: DataFrame with historical price data
            current_price: Current price (optional, will use latest if not provided)
            currency: Currency symbol for formatting
            
        Returns:
            Dictionary with calculated statistics
        """
        if historical_data is None or historical_data.empty:
            self.logger.warning("No historical data provided")
            return self._empty_statistics()
        
        try:
            # Use 'Close' price for calculations
            if 'Close' not in historical_data.columns:
                self.logger.error("'Close' column not found in historical data")
                return self._empty_statistics()
            
            prices = historical_data['Close']
            
            # Basic statistics
            high_52w = float(prices.max())
            low_52w = float(prices.min())
            avg_price = float(prices.mean())
            current = float(current_price) if current_price is not None else float(prices.iloc[-1])
            
            # Calculate price change
            first_price = float(prices.iloc[0])
            price_change = current - first_price
            price_change_pct = (price_change / first_price) if first_price > 0 else 0
            
            # Calculate volatility (standard deviation of daily percentage price changes)
            daily_pct_change = prices.pct_change().dropna()
            volatility = float(daily_pct_change.std()) if len(daily_pct_change) > 0 else 0.0
            
            # Calculate 30-day and 90-day averages
            avg_30d = float(prices.tail(30).mean()) if len(prices) >= 30 else None
            avg_90d = float(prices.tail(90).mean()) if len(prices) >= 90 else None
            
            statistics = {
                "current_price": current,
                "high_52w": high_52w,
                "low_52w": low_52w,
                "average_price": avg_price,
                "price_change": price_change,
                "price_change_pct": price_change_pct,
                "volatility": volatility,
                "avg_30d": avg_30d,
                "avg_90d": avg_90d,
                "data_points": len(prices),
                "currency": currency,
                # Formatted versions for display
                "formatted": {
                    "current_price": format_currency(current, currency),
                    "high_52w": format_currency(high_52w, currency),
                    "low_52w": format_currency(low_52w, currency),
                    "average_price": format_currency(avg_price, currency),
                    "price_change": format_currency(price_change, currency),
                    "price_change_pct": format_percentage(price_change_pct),
                    "volatility": format_percentage(volatility),
                    "avg_30d": format_currency(avg_30d, currency),
                    "avg_90d": format_currency(avg_90d, currency),
                }
            }
            
            self.logger.info("Statistics calculated successfully")
            return statistics
            
        except Exception as e:
            self.logger.error(f"Error calculating statistics: {str(e)}")
            return self._empty_statistics()
    
    def _empty_statistics(self) -> Dict[str, Any]:
        """Return empty statistics dictionary."""
        return {
            "current_price": None,
            "high_52w": None,
            "low_52w": None,
            "average_price": None,
            "price_change": None,
            "price_change_pct": None,
            "volatility": None,
            "avg_30d": None,
            "avg_90d": None,
            "data_points": 0,
            "currency": "USD",
            "formatted": {
                "current_price": "N/A",
                "high_52w": "N/A",
                "low_52w": "N/A",
                "average_price": "N/A",
                "price_change": "N/A",
                "price_change_pct": "N/A",
                "volatility": "N/A",
                "avg_30d": "N/A",
                "avg_90d": "N/A",
            }
        }
    
    def prepare_chart_data(self, historical_data: pd.DataFrame) -> Dict[str, Any]:
        """
        Prepare data for Plotly chart visualization.
        
        Args:
            historical_data: DataFrame with historical price data
            
        Returns:
            Dictionary with chart-ready data
        """
        if historical_data is None or historical_data.empty:
            return {"dates": [], "prices": [], "volume": []}
        
        try:
            dates = historical_data.index.strftime("%Y-%m-%d").tolist()
            prices = historical_data['Close'].tolist()
            volume = historical_data['Volume'].tolist() if 'Volume' in historical_data.columns else []
            
            return {
                "dates": dates,
                "prices": prices,
                "volume": volume
            }
        except Exception as e:
            self.logger.error(f"Error preparing chart data: {str(e)}")
            return {"dates": [], "prices": [], "volume": []}


# Create a global instance
analyzer = FinancialAnalyzer()


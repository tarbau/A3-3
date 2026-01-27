"""
Console application for financial data analysis.
Provides a simple command-line interface to analyze stocks and cryptocurrencies.
"""

import sys
import logging
from typing import Optional

from src.utils import setup_logging, validate_ticker
from src.data_fetcher import data_fetcher
from src.analyzer import analyzer
from src.config import config

# Set up logging
setup_logging()
logger = logging.getLogger(__name__)


def print_header():
    """Print application header."""
    print("\n" + "=" * 60)
    print("  FINANCIAL DATA ANALYZER - Console Application")
    print("=" * 60 + "\n")


def print_separator():
    """Print a separator line."""
    print("-" * 60)


def get_ticker_from_user() -> Optional[str]:
    """
    Get ticker symbol from user input.
    
    Returns:
        Ticker symbol or None if invalid
    """
    print("Enter a ticker symbol (e.g., AAPL, GOOGL, BTC-USD)")
    print("Or press Enter to use default (AAPL): ", end="")
    
    user_input = input().strip()
    
    if not user_input:
        return "AAPL"  # Default ticker
    
    if validate_ticker(user_input):
        return user_input.upper()
    else:
        print(f"❌ Invalid ticker symbol: {user_input}")
        return None


def display_company_info(company_info: dict):
    """
    Display company/cryptocurrency information.
    
    Args:
        company_info: Dictionary with company information
    """
    print_separator()
    print("📊 COMPANY INFORMATION")
    print_separator()
    print(f"Name:        {company_info.get('name', 'N/A')}")
    print(f"Sector:      {company_info.get('sector', 'N/A')}")
    print(f"Industry:    {company_info.get('industry', 'N/A')}")
    print(f"Exchange:    {company_info.get('exchange', 'N/A')}")
    
    market_cap = company_info.get('market_cap')
    if market_cap:
        print(f"Market Cap:  ${market_cap:,.0f}")
    print()


def display_statistics(stats: dict):
    """
    Display calculated statistics.
    
    Args:
        stats: Dictionary with statistics
    """
    print_separator()
    print("📈 STATISTICS (Last 12 Months)")
    print_separator()
    
    formatted = stats.get('formatted', {})
    
    print(f"Current Price:      {formatted.get('current_price', 'N/A')}")
    print(f"52-Week High:       {formatted.get('high_52w', 'N/A')}")
    print(f"52-Week Low:        {formatted.get('low_52w', 'N/A')}")
    print(f"Average Price:      {formatted.get('average_price', 'N/A')}")
    print(f"30-Day Average:     {formatted.get('avg_30d', 'N/A')}")
    print(f"90-Day Average:     {formatted.get('avg_90d', 'N/A')}")
    print()
    print(f"Price Change:       {formatted.get('price_change', 'N/A')}")
    print(f"Change Percentage:  {formatted.get('price_change_pct', 'N/A')}")
    print(f"Volatility:         {formatted.get('volatility', 'N/A')}")
    print(f"Data Points:        {stats.get('data_points', 0)}")
    print()


def main():
    """Main function to run the console application."""
    print_header()
    
    # Get ticker from command line argument or user input
    ticker = None
    if len(sys.argv) > 1:
        ticker = sys.argv[1].strip().upper()
        if not validate_ticker(ticker):
            print(f"❌ Invalid ticker symbol: {ticker}")
            ticker = None
    
    if not ticker:
        ticker = get_ticker_from_user()
    
    if not ticker:
        print("❌ No valid ticker provided. Exiting.")
        return
    
    print(f"\n🔍 Analyzing: {ticker}")
    print("Please wait...\n")
    
    # Fetch data
    ticker_obj = data_fetcher.fetch_data(ticker)
    if not ticker_obj:
        print(f"❌ Failed to fetch data for {ticker}")
        print("Please check:")
        print("  - Your internet connection")
        print("  - The ticker symbol is correct")
        print("  - Try a different ticker (e.g., AAPL, GOOGL, BTC-USD)")
        return
    
    # Get company info
    company_info = data_fetcher.get_company_info(ticker_obj)
    display_company_info(company_info)
    
    # Get current price
    current_price = data_fetcher.get_current_price(ticker_obj)
    
    # Get historical data
    historical_data = data_fetcher.get_historical_data(ticker_obj)
    if historical_data is None or historical_data.empty:
        print("❌ Failed to fetch historical data")
        return
    
    # Calculate statistics
    stats = analyzer.calculate_statistics(
        historical_data,
        current_price,
        company_info.get('currency', 'USD')
    )
    
    display_statistics(stats)
    
    print_separator()
    print("✅ Analysis complete!")
    print_separator()
    print("\n💡 Tips:")
    print("  - Try different tickers: TSLA, MSFT, ETH-USD, DOGE-USD")
    print("  - Run with ticker as argument: python -m app.console_app GOOGL")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        print(f"\n❌ An error occurred: {str(e)}")
        sys.exit(1)

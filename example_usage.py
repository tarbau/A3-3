"""
Example script showing how to use the financial analyzer modules programmatically.
This is useful for understanding how the components work together.
"""

from src.data_fetcher import data_fetcher
from src.analyzer import analyzer
from src.utils import setup_logging

# Set up logging to see what's happening
setup_logging()

def example_analysis(ticker: str):
    """
    Example function showing how to analyze a ticker.
    
    Args:
        ticker: Stock or cryptocurrency ticker symbol
    """
    print(f"\n{'='*60}")
    print(f"Analyzing: {ticker}")
    print(f"{'='*60}\n")
    
    # Step 1: Fetch the ticker data
    print("Step 1: Fetching data...")
    ticker_obj = data_fetcher.fetch_data(ticker)
    
    if not ticker_obj:
        print(f"❌ Failed to fetch data for {ticker}")
        return
    
    print("✅ Data fetched successfully\n")
    
    # Step 2: Get company information
    print("Step 2: Getting company information...")
    company_info = data_fetcher.get_company_info(ticker_obj)
    print(f"Company: {company_info['name']}")
    print(f"Sector: {company_info['sector']}")
    print(f"Industry: {company_info['industry']}\n")
    
    # Step 3: Get current price
    print("Step 3: Getting current price...")
    current_price = data_fetcher.get_current_price(ticker_obj)
    print(f"Current Price: ${current_price:.2f}\n")
    
    # Step 4: Get historical data
    print("Step 4: Fetching historical data...")
    historical_data = data_fetcher.get_historical_data(ticker_obj)
    
    if historical_data is None or historical_data.empty:
        print("❌ Failed to fetch historical data")
        return
    
    print(f"✅ Fetched {len(historical_data)} data points\n")
    
    # Step 5: Calculate statistics
    print("Step 5: Calculating statistics...")
    stats = analyzer.calculate_statistics(
        historical_data,
        current_price,
        company_info.get('currency', 'USD')
    )
    
    print("\n📊 Statistics:")
    print(f"  Current Price: {stats['formatted']['current_price']}")
    print(f"  52-Week High:  {stats['formatted']['high_52w']}")
    print(f"  52-Week Low:   {stats['formatted']['low_52w']}")
    print(f"  Average Price: {stats['formatted']['average_price']}")
    print(f"  Price Change:  {stats['formatted']['price_change']}")
    print(f"  Change %:      {stats['formatted']['price_change_pct']}")
    print(f"  Volatility:    {stats['formatted']['volatility']}\n")
    
    # Step 6: Prepare chart data (for visualization)
    print("Step 6: Preparing chart data...")
    chart_data = analyzer.prepare_chart_data(historical_data)
    print(f"✅ Chart data ready: {len(chart_data['dates'])} data points\n")
    
    print("✅ Analysis complete!\n")


if __name__ == "__main__":
    # Example 1: Analyze a stock
    example_analysis("AAPL")
    
    # Example 2: Analyze a cryptocurrency
    # Uncomment to try:
    # example_analysis("BTC-USD")
    
    # Example 3: Analyze another stock
    # Uncomment to try:
    # example_analysis("TSLA")


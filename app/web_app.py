"""
Flask web application for interactive financial data visualization.
Provides a web dashboard with Plotly charts.
"""

import logging
import json
from pathlib import Path
from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
import plotly.utils

from src.utils import setup_logging, validate_ticker
from src.data_fetcher import data_fetcher
from src.analyzer import analyzer
from src.config import config

# Set up logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize Flask app
# Set template and static folders to root directory
# Get the project root directory (parent of app/)
project_root = Path(__file__).parent.parent

app = Flask(
    __name__,
    template_folder=str(project_root / 'templates'),
    static_folder=str(project_root / 'static')
)
app.config.from_object(config)


def create_price_chart(chart_data: dict, ticker: str) -> str:
    """
    Create a Plotly chart for price visualization.
    
    Args:
        chart_data: Dictionary with dates, prices, and volume
        ticker: Ticker symbol for chart title
        
    Returns:
        JSON string of the Plotly chart
    """
    dates = chart_data.get('dates', [])
    prices = chart_data.get('prices', [])
    volume = chart_data.get('volume', [])
    
    # Create price trace
    price_trace = go.Scatter(
        x=dates,
        y=prices,
        mode='lines',
        name='Price',
        line=dict(color='#1f77b4', width=2),
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> $%{y:.2f}<extra></extra>'
    )
    
    # Create volume trace (if available)
    volume_trace = None
    if volume and len(volume) == len(dates):
        volume_trace = go.Bar(
            x=dates,
            y=volume,
            name='Volume',
            yaxis='y2',
            marker=dict(color='rgba(150, 150, 150, 0.5)'),
            hovertemplate='<b>Date:</b> %{x}<br><b>Volume:</b> %{y:,.0f}<extra></extra>'
        )
    
    # Create layout
    layout = go.Layout(
        title={
            'text': f'{ticker} - Price History',
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)'
        ),
        yaxis=dict(
            title='Price (USD)',
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)'
        ),
        hovermode='x unified',
        template='plotly_white',
        height=500,
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    # Add second y-axis for volume if available
    if volume_trace:
        layout.yaxis2 = dict(
            title='Volume',
            overlaying='y',
            side='right',
            showgrid=False
        )
        fig = go.Figure(data=[price_trace, volume_trace], layout=layout)
    else:
        fig = go.Figure(data=[price_trace], layout=layout)
    
    # Convert to JSON
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze a ticker and return data for visualization.
    
    Expected JSON:
    {
        "ticker": "AAPL"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        ticker = data.get('ticker', '').strip().upper()
        
        if not ticker:
            return jsonify({"error": "Ticker symbol is required"}), 400
        
        if not validate_ticker(ticker):
            return jsonify({"error": f"Invalid ticker symbol: {ticker}"}), 400
        
        logger.info(f"Analyzing ticker: {ticker}")
        
        # Fetch data
        ticker_obj = data_fetcher.fetch_data(ticker)
        if not ticker_obj:
            return jsonify({
                "error": f"Failed to fetch data for {ticker}. Please check the ticker symbol."
            }), 404
        
        # Get company info
        company_info = data_fetcher.get_company_info(ticker_obj)
        
        # Get current price
        current_price = data_fetcher.get_current_price(ticker_obj)
        
        # Get historical data
        historical_data = data_fetcher.get_historical_data(ticker_obj)
        if historical_data is None or historical_data.empty:
            return jsonify({
                "error": "Failed to fetch historical data"
            }), 500
        
        # Calculate statistics
        stats = analyzer.calculate_statistics(
            historical_data,
            current_price,
            company_info.get('currency', 'USD')
        )
        
        # Prepare chart data
        chart_data = analyzer.prepare_chart_data(historical_data)
        chart_json = create_price_chart(chart_data, ticker)
        
        # Prepare response
        response = {
            "success": True,
            "ticker": ticker,
            "company_info": company_info,
            "statistics": stats,
            "chart": chart_json
        }
        
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error in analyze endpoint: {str(e)}", exc_info=True)
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  FINANCIAL DATA ANALYZER - Web Dashboard")
    print("=" * 60)
    print(f"\n🌐 Starting Flask server...")
    print(f"📊 Dashboard available at: http://localhost:5000")
    print(f"💡 Press Ctrl+C to stop the server\n")
    
    try:
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=config.FLASK_DEBUG
        )
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
    except Exception as e:
        logger.error(f"Error starting server: {str(e)}", exc_info=True)


# Financial Data Analyzer

A beginner-friendly Python application for fetching, analyzing, and visualizing financial data from stocks and cryptocurrencies.

## Features

- 📊 Fetch real-time and historical financial data
- 📈 Calculate key statistics (high, low, average, volatility)
- 🖥️ Console application for quick analysis
- 🌐 Interactive web dashboard with Plotly charts
- 💰 Support for stocks and cryptocurrencies

## Project Structure

```
financial-analyzer/
├── src/
│   ├── __init__.py
│   ├── config.py          # Configuration management
│   ├── data_fetcher.py    # Data fetching logic
│   ├── analyzer.py        # Data analysis functions
│   └── utils.py           # Utility functions
├── app/
│   ├── __init__.py
│   ├── console_app.py     # Console application
│   └── web_app.py         # Flask web dashboard
├── templates/              # HTML templates for web app
│   └── index.html
├── static/                 # CSS and JS files
│   └── style.css
├── tests/                  # Unit tests
│   └── __init__.py
├── .env.example           # Example environment variables
├── .gitignore
├── requirements.txt       # Python dependencies
└── README.md
```

## Installation

### 1. Clone or create the project directory

```bash
cd financial-analyzer
```

### 2. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables (optional)

Copy `.env.example` to `.env` and add your Alpha Vantage API key if you want to use it:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:
```
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

**Note:** The application works with `yfinance` by default, which doesn't require an API key.

## Usage

### Console Application

Run the console application to get quick statistics:

```bash
python -m app.console_app
```

Or with a specific ticker:

```bash
python -m app.console_app AAPL
```

**Example tickers:**
- Stocks: `AAPL`, `GOOGL`, `MSFT`, `TSLA`
- Cryptocurrencies: `BTC-USD`, `ETH-USD`, `DOGE-USD`

### Web Dashboard

Start the Flask web server:

```bash
python -m app.web_app
```

Then open your browser and navigate to:
```
http://localhost:5000
```

Enter a ticker symbol and click "Analyze" to see interactive charts and statistics.

## Features Explained

### Data Fetching
- Uses `yfinance` library (free, no API key required)
- Fetches current price, historical data, and company info
- Supports both stocks and cryptocurrencies

### Statistics Calculated
- Current price
- 52-week high/low
- Average price (1 year)
- Price change percentage
- Volatility (standard deviation)

### Web Dashboard
- Interactive Plotly charts
- Historical price visualization
- Key statistics display
- Responsive design

## Requirements

- Python 3.8 or higher
- Internet connection for data fetching

## Dependencies

- `yfinance` - Financial data fetching
- `pandas` - Data manipulation
- `numpy` - Numerical calculations
- `flask` - Web framework
- `plotly` - Interactive charts
- `python-dotenv` - Environment variable management

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure you've activated your virtual environment and installed requirements
2. **Data fetch errors**: Check your internet connection and ticker symbol validity
3. **Port already in use**: Change the port in `web_app.py` if 5000 is occupied

## Learning Resources

- [yfinance Documentation](https://github.com/ranaroussi/yfinance)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Plotly Python Documentation](https://plotly.com/python/)

## License

This project is for educational purposes.




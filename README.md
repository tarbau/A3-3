# 📊 Financial Data Analyzer

A comprehensive Python application for analyzing stocks and cryptocurrencies with both console and web interfaces. Fetch real-time financial data, calculate statistics, and visualize trends with interactive charts.

## ✨ Features

- **📈 Real-time Data Fetching**: Get up-to-date financial data for stocks and cryptocurrencies using yfinance
- **🔢 Statistical Analysis**: Calculate key metrics including:
  - Current price, 52-week high/low
  - Average prices (30-day, 90-day, overall)
  - Price changes and percentages
  - Volatility calculations
- **💻 Dual Interface**:
  - **Console Application**: Command-line interface for quick analysis
  - **Web Dashboard**: Interactive browser-based interface with Plotly charts
- **📊 Interactive Visualizations**: Beautiful, interactive charts showing price history and volume
- **🌐 Multi-Asset Support**: Analyze stocks (AAPL, GOOGL, TSLA) and cryptocurrencies (BTC-USD, ETH-USD)
- **🏗️ Modular Architecture**: Clean, maintainable code structure with separation of concerns

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Internet connection (for fetching data)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tarbau/A3-3.git
   cd A3-3
   ```

2. **Create and activate virtual environment**

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Option 1: Console Application

```bash
python -m app.console_app AAPL
```

Replace `AAPL` with any ticker symbol (e.g., `GOOGL`, `TSLA`, `BTC-USD`).

#### Option 2: Web Dashboard

```bash
python -m app.web_app
```

Then open your browser and navigate to: `http://localhost:5000`

#### Option 3: Use Batch Files (Windows)

- Double-click `run_console.bat` for console app
- Double-click `run_web.bat` for web dashboard

## 📖 Usage Examples

### Console Application

```bash
# Analyze Apple stock
python -m app.console_app AAPL

# Analyze Bitcoin
python -m app.console_app BTC-USD

# Analyze Tesla
python -m app.console_app TSLA
```

### Web Dashboard

1. Start the server: `python -m app.web_app`
2. Open `http://localhost:5000` in your browser
3. Enter a ticker symbol (e.g., `AAPL`, `GOOGL`, `BTC-USD`)
4. Click "Analyze" to see interactive charts and statistics

### Programmatic Usage

```python
from src.data_fetcher import data_fetcher
from src.analyzer import analyzer

# Fetch data
ticker_obj = data_fetcher.fetch_data("AAPL")

# Get company info
company_info = data_fetcher.get_company_info(ticker_obj)

# Get current price
current_price = data_fetcher.get_current_price(ticker_obj)

# Get historical data
historical_data = data_fetcher.get_historical_data(ticker_obj)

# Calculate statistics
stats = analyzer.calculate_statistics(historical_data, current_price, "USD")
```

See `example_usage.py` for more detailed examples.

## 📁 Project Structure

```
SemProject/
├── app/
│   ├── console_app.py      # Console application entry point
│   └── web_app.py          # Flask web application
├── src/
│   ├── analyzer.py         # Financial analysis and statistics
│   ├── data_fetcher.py     # Data fetching from yfinance
│   ├── config.py           # Configuration management
│   └── utils.py            # Utility functions
├── templates/
│   └── index.html          # Web dashboard HTML template
├── static/
│   └── style.css           # Web dashboard styles
├── tests/
│   └── test_utils.py       # Unit tests
├── requirements.txt        # Python dependencies
├── example_usage.py        # Example usage script
├── QUICKSTART.md           # Quick start guide
├── SETUP_GUIDE.md          # Detailed setup instructions
└── README.md               # This file
```

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **yfinance**: Financial data fetching
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **Flask**: Web framework
- **Plotly**: Interactive data visualization
- **python-dotenv**: Environment variable management

## 📊 Supported Tickers

### Stocks
- `AAPL` - Apple Inc.
- `GOOGL` - Alphabet Inc. (Google)
- `MSFT` - Microsoft Corporation
- `TSLA` - Tesla, Inc.
- `AMZN` - Amazon.com, Inc.
- And many more...

### Cryptocurrencies
- `BTC-USD` - Bitcoin
- `ETH-USD` - Ethereum
- `DOGE-USD` - Dogecoin
- `BNB-USD` - Binance Coin
- And many more...

## ⚙️ Configuration

Configuration is managed in `src/config.py`. You can customize:

- **Data Period**: Default is `1y` (1 year)
  - Options: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`
- **Data Interval**: Default is `1d` (daily)
  - Options: `1m`, `5m`, `15m`, `30m`, `1h`, `1d`, `5d`, `1wk`, `1mo`
- **Flask Settings**: Debug mode, environment variables

## 🐛 Troubleshooting

### ModuleNotFoundError
- **Solution**: Make sure virtual environment is activated and dependencies are installed
  ```bash
  pip install -r requirements.txt
  ```

### Can't Fetch Data
- **Solution**: 
  - Check your internet connection
  - Verify the ticker symbol is correct
  - Try a different ticker (e.g., `AAPL`, `GOOGL`, `BTC-USD`)

### Port 5000 Already in Use
- **Solution**: Change the port in `app/web_app.py` (line 207) or stop the process using port 5000

### Execution Policy Error (Windows)
- **Solution**: Run this command in PowerShell:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

## 📚 Documentation

- **QUICKSTART.md**: Quick start guide (5 minutes)
- **SETUP_GUIDE.md**: Detailed setup instructions
- **START_HERE.md**: Step-by-step getting started guide

## 🧪 Testing

Run tests with:
```bash
pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- **yfinance**: For providing easy access to financial data
- **Plotly**: For beautiful interactive visualizations
- **Flask**: For the lightweight web framework

## 📧 Contact

For questions or issues, please open an issue on GitHub.

---

**Happy Analyzing! 📈**

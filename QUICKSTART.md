# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Create Virtual Environment

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

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Console Application

```bash
python -m app.console_app AAPL
```

This will analyze Apple stock and show statistics in the console.

### Step 4: Run Web Dashboard

Open a new terminal (keep virtual environment activated) and run:

```bash
python -m app.web_app
```

Then open your browser and go to: `http://localhost:5000`

## 📝 Example Tickers

### Stocks
- `AAPL` - Apple
- `GOOGL` - Google
- `MSFT` - Microsoft
- `TSLA` - Tesla
- `AMZN` - Amazon

### Cryptocurrencies
- `BTC-USD` - Bitcoin
- `ETH-USD` - Ethereum
- `DOGE-USD` - Dogecoin
- `BNB-USD` - Binance Coin

## 🎯 What You'll Learn

1. **Data Fetching**: How to get real-time financial data
2. **Data Analysis**: Calculate statistics like high, low, average, volatility
3. **Data Visualization**: Create interactive charts with Plotly
4. **Web Development**: Build a Flask web application
5. **Best Practices**: Project structure, error handling, logging

## 🐛 Troubleshooting

**Problem**: `ModuleNotFoundError`
- **Solution**: Make sure virtual environment is activated and dependencies are installed

**Problem**: Can't fetch data
- **Solution**: Check internet connection and ticker symbol validity

**Problem**: Port 5000 already in use
- **Solution**: Change port in `app/web_app.py` (line with `port=5000`)

## 📚 Next Steps

1. Try different tickers
2. Modify the analysis functions in `src/analyzer.py`
3. Customize the web dashboard in `templates/index.html`
4. Add new features like technical indicators
5. Explore the code to understand how it works!


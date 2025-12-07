# Setup Guide - Running on Your Local Computer

This guide will walk you through setting up and running the Financial Data Analyzer on your Windows computer.

## Prerequisites

Before starting, make sure you have:
- **Python 3.8 or higher** installed
- **Internet connection** (for fetching financial data)
- **A terminal/command prompt** (PowerShell or Command Prompt)

### Check Python Installation

Open PowerShell or Command Prompt and type:
```bash
python --version
```

You should see something like: `Python 3.8.x` or higher.

If Python is not installed, download it from: https://www.python.org/downloads/

**Important:** During installation, check the box "Add Python to PATH"

---

## Step-by-Step Setup

### Step 1: Navigate to Project Directory

Open PowerShell or Command Prompt and navigate to the project folder:

```bash
cd D:\Study
```

### Step 2: Create Virtual Environment

A virtual environment keeps your project dependencies separate from other Python projects.

**Windows (PowerShell):**
```bash
python -m venv venv
```

**Windows (Command Prompt):**
```bash
python -m venv venv
```

This creates a folder called `venv` in your project directory.

### Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

If you get an execution policy error, run this first:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### Step 4: Install Dependencies

With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

This will install:
- yfinance (for fetching financial data)
- pandas (for data manipulation)
- numpy (for calculations)
- flask (for web dashboard)
- plotly (for charts)
- python-dotenv (for configuration)

Wait for the installation to complete. This may take a few minutes.

### Step 5: Verify Installation

Check that everything is installed correctly:

```bash
pip list
```

You should see all the packages listed above.

---

## Running the Applications

### Option 1: Console Application (Command Line)

The console application provides quick analysis in your terminal.

**Basic usage:**
```bash
python -m app.console_app
```

This will prompt you to enter a ticker symbol.

**With ticker as argument:**
```bash
python -m app.console_app AAPL
python -m app.console_app GOOGL
python -m app.console_app BTC-USD
```

**Example output:**
```
============================================================
  FINANCIAL DATA ANALYZER - Console Application
============================================================

🔍 Analyzing: AAPL
Please wait...

📊 COMPANY INFORMATION
------------------------------------------------------------
Name:        Apple Inc.
Sector:      Technology
Industry:    Consumer Electronics
Exchange:    NMS
Market Cap:  $3,000,000,000,000

📈 STATISTICS (Last 12 Months)
------------------------------------------------------------
Current Price:      $175.50
52-Week High:       $198.23
52-Week Low:        $124.17
...
```

### Option 2: Web Dashboard (Browser Interface)

The web dashboard provides an interactive interface with charts.

**Start the server:**
```bash
python -m app.web_app
```

You should see:
```
============================================================
  FINANCIAL DATA ANALYZER - Web Dashboard
============================================================

🌐 Starting Flask server...
📊 Dashboard available at: http://localhost:5000
💡 Press Ctrl+C to stop the server
```

**Open your web browser:**
1. Open any web browser (Chrome, Firefox, Edge, etc.)
2. Go to: `http://localhost:5000`
3. Enter a ticker symbol (e.g., AAPL, GOOGL, BTC-USD)
4. Click "Analyze" to see interactive charts and statistics

**To stop the server:**
Press `Ctrl + C` in the terminal

---

## Troubleshooting

### Problem: "python is not recognized"

**Solution:**
- Python is not in your PATH
- Reinstall Python and check "Add Python to PATH"
- Or use `py` instead of `python`:
  ```bash
  py -m venv venv
  py -m app.console_app
  ```

### Problem: "ModuleNotFoundError"

**Solution:**
1. Make sure virtual environment is activated (you should see `(venv)`)
2. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Problem: "Execution Policy" error in PowerShell

**Solution:**
Run this command:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating the virtual environment again.

### Problem: Port 5000 already in use

**Solution:**
1. Close other applications using port 5000
2. Or change the port in `app/web_app.py`:
   - Find: `port=5000`
   - Change to: `port=5001`
   - Then access: `http://localhost:5001`

### Problem: Can't fetch data

**Solution:**
1. Check your internet connection
2. Verify the ticker symbol is correct
3. Try a different ticker (AAPL, GOOGL, BTC-USD)
4. Wait a moment and try again (API might be temporarily unavailable)

### Problem: "No module named 'app'"

**Solution:**
Make sure you're in the project root directory (`D:\Study`):
```bash
cd D:\Study
python -m app.console_app
```

---

## Quick Test

To verify everything works, try this:

1. **Test console app:**
   ```bash
   python -m app.console_app AAPL
   ```

2. **Test web app:**
   ```bash
   python -m app.web_app
   ```
   Then open browser to `http://localhost:5000` and analyze "AAPL"

---

## Example Tickers to Try

### Stocks:
- `AAPL` - Apple
- `GOOGL` - Google (Alphabet)
- `MSFT` - Microsoft
- `TSLA` - Tesla
- `AMZN` - Amazon
- `META` - Meta (Facebook)
- `NVDA` - NVIDIA

### Cryptocurrencies:
- `BTC-USD` - Bitcoin
- `ETH-USD` - Ethereum
- `DOGE-USD` - Dogecoin
- `BNB-USD` - Binance Coin
- `ADA-USD` - Cardano

---

## Next Steps

Once everything is working:

1. **Explore the code:**
   - Read `example_usage.py` to see how modules work
   - Check `src/data_fetcher.py` to understand data fetching
   - Look at `src/analyzer.py` to see how statistics are calculated

2. **Customize:**
   - Modify `templates/index.html` to change the web interface
   - Edit `static/style.css` to change styling
   - Add new features in `src/analyzer.py`

3. **Learn more:**
   - Read the full `README.md`
   - Check out `QUICKSTART.md` for more examples

---

## Need Help?

If you encounter any issues:
1. Check the error message carefully
2. Review the troubleshooting section above
3. Make sure all prerequisites are met
4. Verify you're in the correct directory with virtual environment activated

Happy analyzing! 📊


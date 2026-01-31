# Quick Start Guide


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

## Example Tickers

### Stocks
- `AAPL` - Apple
- `GOOGL` - Google
- `MSFT` - Microsoft
- `TSLA` - Tesla
- `AMZN` - Amazon


## 🐛 Troubleshooting

**Problem**: `ModuleNotFoundError`
- **Solution**: Make sure virtual environment is activated and dependencies are installed

**Problem**: Can't fetch data
- **Solution**: Check internet connection and ticker symbol validity

**Problem**: Port 5000 already in use
- **Solution**: Change port in `app/web_app.py` (line with `port=5000`)



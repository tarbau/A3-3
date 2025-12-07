# 🚀 START HERE - How to Run the Project

## Quick Start (3 Steps)

### Step 1: Open Terminal in Project Folder

1. Open **File Explorer**
2. Navigate to: `D:\Study`
3. Right-click in the folder → **"Open in Terminal"** or **"Open PowerShell window here"**

OR

1. Press `Windows Key + R`
2. Type: `powershell`
3. Press Enter
4. Type: `cd D:\Study`
5. Press Enter

---

### Step 2: Set Up Virtual Environment (One-Time Setup)

Copy and paste these commands **one by one**:

```powershell
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\Activate.ps1
```

**If you see an error about execution policy**, run this first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again:
```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your prompt.

**Install dependencies:**
```powershell
pip install -r requirements.txt
```

Wait for installation to finish (takes 1-2 minutes).

---

### Step 3: Run the Application

#### Option A: Console Application (Text-Based)

```powershell
python -m app.console_app AAPL
```

Replace `AAPL` with any ticker:
- `GOOGL` (Google)
- `TSLA` (Tesla)
- `BTC-USD` (Bitcoin)
- `ETH-USD` (Ethereum)

#### Option B: Web Dashboard (Browser-Based)

```powershell
python -m app.web_app
```

Then:
1. Open your web browser
2. Go to: `http://localhost:5000`
3. Enter a ticker and click "Analyze"

Press `Ctrl + C` to stop the server.

---

## 🎯 Easy Way: Use Batch Files

Instead of typing commands, you can **double-click** these files:

1. **`run_console.bat`** - Runs console app (will prompt for ticker)
2. **`run_web.bat`** - Runs web dashboard

**Note:** Make sure you've completed Step 2 (setup) first!

---

## 📋 What You'll See

### Console App Output:
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
...

📈 STATISTICS (Last 12 Months)
------------------------------------------------------------
Current Price:      $175.50
52-Week High:       $198.23
...
```

### Web Dashboard:
- Beautiful interface in your browser
- Interactive charts
- Real-time statistics
- Easy to use!

---

## ❓ Common Issues

### "python is not recognized"
→ Install Python from python.org and check "Add to PATH"

### "ModuleNotFoundError"
→ Make sure virtual environment is activated (see `(venv)` in prompt)
→ Run: `pip install -r requirements.txt`

### "Execution Policy" error
→ Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Can't fetch data
→ Check internet connection
→ Try a different ticker (AAPL, GOOGL, BTC-USD)

---

## 📚 More Help

- **Detailed Setup:** See `SETUP_GUIDE.md`
- **Quick Reference:** See `QUICKSTART.md`
- **Full Documentation:** See `README.md`

---

## ✅ Checklist

Before running, make sure:
- [ ] Python 3.8+ is installed
- [ ] You're in the `D:\Study` folder
- [ ] Virtual environment is created (`venv` folder exists)
- [ ] Virtual environment is activated (see `(venv)` in prompt)
- [ ] Dependencies are installed (`pip install -r requirements.txt`)
- [ ] Internet connection is working

---

**Ready? Start with Step 1 above!** 🎉


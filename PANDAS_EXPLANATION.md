# 🐼 What Does Pandas Do? - Beginner's Guide

## What is Pandas? (Simple Explanation)

**Pandas** is a Python library that helps you work with **tables of data** (like Excel spreadsheets, but in code).

Think of it like this:
- **Excel** = Spreadsheet program for humans
- **Pandas** = Spreadsheet tool for Python programs

### Real-World Analogy

Imagine you have a **table** with stock prices:

| Date       | Open  | High  | Low   | Close | Volume    |
|------------|-------|-------|-------|-------|-----------|
| 2024-01-01 | 150.0 | 152.0 | 149.0 | 151.0 | 10,000,000|
| 2024-01-02 | 151.0 | 153.0 | 150.0 | 152.0 | 12,000,000|
| 2024-01-03 | 152.0 | 154.0 | 151.0 | 153.0 | 11,000,000|

**Without pandas:** You'd have to write complicated code to work with this data.

**With pandas:** You can easily:
- Find the highest price
- Calculate the average
- Get the last 30 days
- Filter by date
- And much more!

---

## What is a DataFrame?

A **DataFrame** is pandas' way of storing a table of data.

```python
import pandas as pd

# This is a DataFrame (a table)
data = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Price': [150.0, 151.0, 152.0]
})
```

**Think of it like:**
- **DataFrame** = A table with rows and columns
- **Rows** = Each day's data
- **Columns** = Different types of information (Date, Price, Volume, etc.)

---

## How Pandas is Used in Your Project

### **STEP 1: Import Pandas**

```python
import pandas as pd
```

**What this does:**
- Brings in the pandas library
- Gives it a short nickname `pd` (so you don't have to type `pandas` every time)

**Location:** `src/data_fetcher.py` line 9 and `src/analyzer.py` line 7

---

### **STEP 2: Receive Data from API as DataFrame**

When the API returns historical stock data, it comes as a **pandas DataFrame**:

```python
hist = ticker_obj.history(period="1y", interval="1d")
# hist is now a pandas DataFrame!
```

**What the DataFrame looks like:**

```
            Open    High    Low     Close   Volume
Date                                              
2023-01-01  150.0   152.0   149.0   151.0   10000000
2023-01-02  151.0   153.0   150.0   152.0   12000000
2023-01-03  152.0   154.0   151.0   153.0   11000000
...         ...     ...     ...     ...     ...
```

**Location:** `src/data_fetcher.py` line 115

---

### **STEP 3: Access Columns (Get Specific Data)**

Pandas makes it easy to get a specific column:

```python
prices = historical_data['Close']
```

**What this does:**
- Gets all the "Close" prices from the table
- `prices` is now a list of all closing prices

**Think of it like:** Selecting a column in Excel by clicking on the column header.

**Location:** `src/analyzer.py` line 50

**Example:**
```python
# If your DataFrame has:
# Date       | Close
# 2024-01-01 | 150.0
# 2024-01-02 | 151.0
# 2024-01-03 | 152.0

prices = historical_data['Close']
# prices now contains: [150.0, 151.0, 152.0]
```

---

### **STEP 4: Calculate Statistics**

Pandas has built-in functions to calculate statistics:

#### **Find Maximum (Highest Price)**
```python
high_52w = float(prices.max())
```

**What this does:**
- Looks through all prices
- Finds the highest one
- Returns that value

**Location:** `src/analyzer.py` line 53

**Example:**
```python
prices = [150.0, 151.0, 152.0, 153.0, 151.0]
high_52w = prices.max()  # Returns 153.0 (the highest)
```

---

#### **Find Minimum (Lowest Price)**
```python
low_52w = float(prices.min())
```

**What this does:**
- Looks through all prices
- Finds the lowest one
- Returns that value

**Location:** `src/analyzer.py` line 54

**Example:**
```python
prices = [150.0, 151.0, 152.0, 153.0, 151.0]
low_52w = prices.min()  # Returns 150.0 (the lowest)
```

---

#### **Calculate Average**
```python
avg_price = float(prices.mean())
```

**What this does:**
- Adds up all the prices
- Divides by the number of prices
- Returns the average

**Location:** `src/analyzer.py` line 55

**Example:**
```python
prices = [150.0, 151.0, 152.0]
avg_price = prices.mean()  # Returns 151.0 (150+151+152)/3
```

---

#### **Get Last Value (Most Recent Price)**
```python
current = float(prices.iloc[-1])
```

**What this does:**
- `.iloc[-1]` = "Get the last item in the list"
- Gets the most recent price (the last one in the table)

**Location:** `src/analyzer.py` line 56

**Example:**
```python
prices = [150.0, 151.0, 152.0]
current = prices.iloc[-1]  # Returns 152.0 (the last one)
```

---

#### **Get First Value (Oldest Price)**
```python
first_price = float(prices.iloc[0])
```

**What this does:**
- `.iloc[0]` = "Get the first item in the list"
- Gets the oldest price (the first one in the table)

**Location:** `src/analyzer.py` line 59

**Example:**
```python
prices = [150.0, 151.0, 152.0]
first_price = prices.iloc[0]  # Returns 150.0 (the first one)
```

---

#### **Calculate Percentage Change**
```python
returns = prices.pct_change().dropna()
```

**What this does:**
- `.pct_change()` = Calculate how much each price changed from the previous one (as a percentage)
- `.dropna()` = Remove any "NaN" (Not a Number) values

**Location:** `src/analyzer.py` line 64

**Example:**
```python
prices = [100.0, 105.0, 110.0]
returns = prices.pct_change()
# Returns: [NaN, 0.05, 0.0476]
# (5% increase from 100 to 105, 4.76% increase from 105 to 110)
```

---

#### **Calculate Standard Deviation (Volatility)**
```python
volatility = float(returns.std())
```

**What this does:**
- Calculates how "spread out" the returns are
- Higher value = more volatile (prices change a lot)
- Lower value = less volatile (prices are stable)

**Location:** `src/analyzer.py` line 65

**Example:**
```python
returns = [0.01, 0.02, -0.01, 0.03, 0.01]
volatility = returns.std()  # Returns ~0.014 (measures how spread out)
```

---

#### **Get Last N Days**
```python
avg_30d = float(prices.tail(30).mean())
```

**What this does:**
- `.tail(30)` = Get the last 30 rows (last 30 days)
- `.mean()` = Calculate the average of those 30 days

**Location:** `src/analyzer.py` line 68

**Example:**
```python
# If you have 365 days of data
prices = [150.0, 151.0, ..., 152.0]  # 365 prices

last_30 = prices.tail(30)  # Gets last 30 prices
avg_30d = last_30.mean()   # Averages those 30 prices
```

---

### **STEP 5: Prepare Data for Charts**

Pandas helps convert the DataFrame into lists that can be used for charts:

```python
dates = historical_data.index.strftime("%Y-%m-%d").tolist()
prices = historical_data['Close'].tolist()
volume = historical_data['Volume'].tolist()
```

**What this does:**
- `.index` = Gets the dates (row labels)
- `.strftime()` = Formats dates as "YYYY-MM-DD"
- `.tolist()` = Converts pandas data to a regular Python list
- `['Close']` = Gets the Close column
- `.tolist()` = Converts to a list

**Location:** `src/analyzer.py` lines 145-147

**Example:**
```python
# DataFrame:
# Date       | Close
# 2024-01-01 | 150.0
# 2024-01-02 | 151.0

dates = historical_data.index.strftime("%Y-%m-%d").tolist()
# dates = ["2024-01-01", "2024-01-02"]

prices = historical_data['Close'].tolist()
# prices = [150.0, 151.0]
```

---

## Complete Example: How Pandas Processes Stock Data

Let's trace through what happens with real data:

### **1. API Returns DataFrame**

```python
# From yfinance API:
historical_data = ticker_obj.history(period="1y")
```

**The DataFrame looks like:**
```
            Open    High    Low     Close   Volume
Date                                              
2023-01-01  150.0   152.0   149.0   151.0   10000000
2023-01-02  151.0   153.0   150.0   152.0   12000000
2023-01-03  152.0   154.0   151.0   153.0   11000000
...         ...     ...     ...     ...     ...
2024-01-01  160.0   162.0   159.0   161.0   15000000
```

### **2. Extract Close Prices**

```python
prices = historical_data['Close']
```

**Result:**
```
Date
2023-01-01    151.0
2023-01-02    152.0
2023-01-03    153.0
...
2024-01-01    161.0
```

### **3. Calculate Statistics**

```python
high_52w = prices.max()      # 161.0 (highest)
low_52w = prices.min()       # 151.0 (lowest)
avg_price = prices.mean()    # 156.0 (average)
current = prices.iloc[-1]     # 161.0 (most recent)
first_price = prices.iloc[0] # 151.0 (oldest)
```

### **4. Calculate Price Change**

```python
price_change = current - first_price
# 161.0 - 151.0 = 10.0

price_change_pct = (price_change / first_price) * 100
# (10.0 / 151.0) * 100 = 6.62%
```

### **5. Calculate Volatility**

```python
returns = prices.pct_change().dropna()
# [0.0066, 0.0066, ...] (daily percentage changes)

volatility = returns.std()
# 0.02 (2% standard deviation)
```

### **6. Get Last 30 Days Average**

```python
last_30_days = prices.tail(30)
# Gets last 30 prices

avg_30d = last_30_days.mean()
# Averages those 30 prices
```

---

## Visual Summary

```
┌─────────────────────────────────────────────────┐
│         API Returns Data                        │
│  (From Yahoo Finance via yfinance)              │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│      Pandas DataFrame (Table)                   │
│                                                 │
│  Date       | Open  | High  | Low   | Close    │
│  ───────────┼───────┼───────┼───────┼──────────│
│  2024-01-01 | 150.0 | 152.0 | 149.0 | 151.0    │
│  2024-01-02 | 151.0 | 153.0 | 150.0 | 152.0    │
│  2024-01-03 | 152.0 | 154.0 | 151.0 | 153.0    │
│  ...        | ...   | ...   | ...   | ...      │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│      Pandas Operations                          │
│                                                 │
│  • Get column: data['Close']                   │
│  • Find max: prices.max()                      │
│  • Find min: prices.min()                      │
│  • Calculate average: prices.mean()            │
│  • Get last value: prices.iloc[-1]             │
│  • Get last 30: prices.tail(30)                │
│  • Calculate % change: prices.pct_change()     │
│  • Calculate volatility: returns.std()         │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│      Results (Statistics)                       │
│                                                 │
│  • Highest price: $161.00                      │
│  • Lowest price: $151.00                       │
│  • Average price: $156.00                      │
│  • Current price: $161.00                      │
│  • Price change: +$10.00 (+6.62%)              │
│  • Volatility: 2.0%                            │
│  • 30-day average: $159.50                     │
└─────────────────────────────────────────────────┘
```

---

## Key Pandas Functions Used in Your Project

| Function | What It Does | Example |
|----------|--------------|---------|
| `data['Column']` | Get a column | `data['Close']` gets all closing prices |
| `.max()` | Find maximum | `prices.max()` finds highest price |
| `.min()` | Find minimum | `prices.min()` finds lowest price |
| `.mean()` | Calculate average | `prices.mean()` calculates average |
| `.iloc[0]` | Get first item | `prices.iloc[0]` gets first price |
| `.iloc[-1]` | Get last item | `prices.iloc[-1]` gets most recent price |
| `.tail(30)` | Get last 30 items | `prices.tail(30)` gets last 30 days |
| `.pct_change()` | Calculate % change | `prices.pct_change()` gets daily changes |
| `.std()` | Calculate standard deviation | `returns.std()` calculates volatility |
| `.tolist()` | Convert to list | `data['Close'].tolist()` converts to list |
| `.empty` | Check if empty | `data.empty` checks if no data |
| `.dropna()` | Remove missing values | `data.dropna()` removes NaN values |

---

## Why Use Pandas Instead of Regular Python Lists?

### **Without Pandas (Hard Way):**
```python
# Get all closing prices
prices = []
for row in data:
    prices.append(row['Close'])

# Find maximum
max_price = prices[0]
for price in prices:
    if price > max_price:
        max_price = price

# Calculate average
total = 0
for price in prices:
    total += price
avg_price = total / len(prices)
```

### **With Pandas (Easy Way):**
```python
# Get all closing prices
prices = data['Close']

# Find maximum
max_price = prices.max()

# Calculate average
avg_price = prices.mean()
```

**Pandas is much simpler and faster!** 🚀

---

## Where Pandas is Used in Your Project

### **File: `src/data_fetcher.py`**
- **Line 9:** `import pandas as pd` - Import pandas
- **Line 98:** `-> Optional[pd.DataFrame]` - Function returns a DataFrame
- **Line 115:** `hist = ticker_obj.history(...)` - Gets DataFrame from API

### **File: `src/analyzer.py`**
- **Line 7:** `import pandas as pd` - Import pandas
- **Line 25:** `historical_data: pd.DataFrame` - Function receives DataFrame
- **Line 50:** `prices = historical_data['Close']` - Get Close column
- **Line 53:** `prices.max()` - Find maximum
- **Line 54:** `prices.min()` - Find minimum
- **Line 55:** `prices.mean()` - Calculate average
- **Line 56:** `prices.iloc[-1]` - Get last value
- **Line 59:** `prices.iloc[0]` - Get first value
- **Line 64:** `prices.pct_change().dropna()` - Calculate percentage changes
- **Line 65:** `returns.std()` - Calculate volatility
- **Line 68:** `prices.tail(30).mean()` - Get last 30 days average
- **Line 145:** `historical_data.index.strftime(...)` - Format dates
- **Line 146:** `historical_data['Close'].tolist()` - Convert to list

---

## Summary

**What Pandas Does:**
1. **Stores data in tables** (DataFrames) - like Excel spreadsheets
2. **Makes it easy to access data** - get columns, rows, specific values
3. **Calculates statistics** - max, min, average, standard deviation, etc.
4. **Processes large amounts of data** - handles thousands of rows easily
5. **Converts data formats** - DataFrame to lists, dates to strings, etc.

**In Your Project:**
- Receives stock data from API as a DataFrame
- Extracts specific columns (like Close prices)
- Calculates statistics (high, low, average, volatility)
- Prepares data for charts

**Think of it like:** Pandas is your data assistant - it organizes, calculates, and prepares your data so you can analyze it easily! 🐼

---

## Common Questions

### **Q: Do I need to install pandas?**
A: Yes! It should be in your `requirements.txt`. Install with: `pip install pandas`

### **Q: Is pandas the same as Excel?**
A: No, but it's similar. Pandas is for Python code, Excel is for humans. But they both work with tables of data.

### **Q: Can I use pandas without knowing all the functions?**
A: Yes! You only need to know the functions you use. Start with the basics like `.max()`, `.min()`, `.mean()`.

### **Q: Why is it called "pandas"?**
A: It's named after "Panel Data" (a type of data structure), but the name was shortened to "pandas" which is also a cute animal! 🐼

---

**Remember:** Pandas makes working with tables of data easy and powerful. Instead of writing complicated loops, you can use simple functions like `.max()`, `.mean()`, etc. It's like having a super-powered calculator for data! 🎉



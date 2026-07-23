import datetime
import numpy as np
import pandas as pd

# ==============================================================================
# Guided Lab 386.3.15 - Generating a Date Range Using date_range() Function
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1: By Specifying Start and End
# ------------------------------------------------------------------------------
print("\n--- Example 1: Basic Date Range (Start & End) ---")
date_range_1 = pd.date_range(start="07-01-2023", end="07-31-2025")
print(date_range_1)
print("\n")

# ------------------------------------------------------------------------------
# Example 2: Creating a Date Range with Periods
# ------------------------------------------------------------------------------
print("--- Example 2: Date Range with Periods (periods=10) ---")
date_range_period = pd.date_range(start="01-01-2023", end="07-31-2025", periods=10)
print(date_range_period)
print("\n")

# ------------------------------------------------------------------------------
# Exploring Different Frequencies
# ------------------------------------------------------------------------------
print("--- Example 2.1: 6-Minute Intervals (freq='6min') ---")
date_range_6min = pd.date_range(start="01-01-2023", end="07-31-2025", freq="6min")
print("First 5 entries:\n", date_range_6min[:5])
print("\n")

print("--- Example 2.2: Business Days (freq='B') ---")
date_range_biz = pd.date_range(start="01-01-2023", end="07-31-2025", freq="B")
print("First 5 entries:\n", date_range_biz[:5])
print("\n")

print("--- Example 2.3: Weekly Frequency (freq='W') ---")
date_range_weekly = pd.date_range(start="01-01-2023", end="07-31-2025", freq="W")
print("First 5 entries:\n", date_range_weekly[:5])
print("\n")

print("--- Example 2.4: Start, Periods, and Month-End Frequency (freq='2ME') ---")
date_range_2me = pd.date_range(start="01-01-2023", periods=6, freq="2ME")
print(date_range_2me)
print("\n")

# ------------------------------------------------------------------------------
# Example 3: By Specifying Start, Periods, and Timezone (tz)
# ------------------------------------------------------------------------------
print("--- Example 3: Timezone Specific Date Range (tz='Asia/Tokyo') ---")
date_range_tz = pd.date_range(start="01-01-2023", periods=6, tz="Asia/Tokyo")
print(date_range_tz)
print("\n")

# ------------------------------------------------------------------------------
# Real-World Example: Representing Stock Prices over a Specified Period
# ------------------------------------------------------------------------------
print("--- Real-World Example: Simulated Stock Prices ---")
start_date = "2023-01-01"
num_days = 30

date_range_stock = pd.date_range(start=start_date, periods=num_days, freq="D")

np.random.seed(42)
stock_prices = np.random.normal(loc=100, scale=5, size=num_days).round(2)

stock_df = pd.DataFrame({"Date": date_range_stock, "StockPrice": stock_prices})
print(stock_df.head(10))
print("\n")

# ------------------------------------------------------------------------------
# Example 4: The pandas.Timestamp() Function
# ------------------------------------------------------------------------------
print("--- Example 4.1: Creating Pandas Timestamps ---")
# 1. From string
timestamp_str = pd.Timestamp("2023-01-15 10:30:00")
print(f"Timestamp from string: {timestamp_str}")
print(f"Type: {type(timestamp_str)}\n")

# 2. From datetime.datetime object
dt_object = datetime.datetime(2024, 7, 21, 14, 45, 10)
timestamp_dt = pd.Timestamp(dt_object)
print(f"Timestamp from datetime object: {timestamp_dt}")
print(f"Type: {type(timestamp_dt)}\n")

print("--- Example 4.2: Accessing Timestamp Components and Attributes ---")
# 3. Specific components
timestamp_components = pd.Timestamp(
    year=2025, month=3, day=1, hour=9, minute=0, second=0
)
print(f"Timestamp from components: {timestamp_components}")
print(f"Type: {type(timestamp_components)}\n")

# 4. Attributes
print(f"Year: {timestamp_components.year}")
print(f"Month: {timestamp_components.month}")
print(f"Day: {timestamp_components.day}")
print(f"Hour: {timestamp_components.hour}")
print(f"Minute: {timestamp_components.minute}")
print(f"Second: {timestamp_components.second}")
print(f"Day of week (0=Monday, 6=Sunday): {timestamp_components.dayofweek}")
print(f"Name of the day: {timestamp_components.day_name()}")
print(f"Is it a leap year?: {timestamp_components.is_leap_year}\n")

# 5. Timezone information
timestamp_tz = pd.Timestamp("2023-01-15 10:30:00", tz="America/New_York")
print(f"Timestamp with timezone: {timestamp_tz}")
print(f"Timezone: {timestamp_tz.tz}\n")

# 6. Timezone conversion
timestamp_tz_utc = timestamp_tz.tz_convert("UTC")
print(f"Timestamp converted to UTC: {timestamp_tz_utc}")
print("\n")

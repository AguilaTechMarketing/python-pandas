import pandas as pd

# ==============================================================================
# Guided Lab 386.3.16 - Convert Date-Like Strings to Pandas DateTime Series 
#                       using to_datetime()
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1: Convert List of String Dates to Pandas DateTime Series
# ------------------------------------------------------------------------------
print("\n--- Example 1: Convert List of String Dates ---")
input_dates = ["2023-01-01", "2023-01-02", "2023-02-06"]
print("Original Date Strings:", input_dates)

print("\n======= Before convert ============")
print("datatype is", type(input_dates))

output_dates = pd.to_datetime(input_dates)
print("\n======= After convert ============")
print("Converted DateTime Objects:")
print("Output:", output_dates)
print("datatype is", type(output_dates))
print("\n")

# ------------------------------------------------------------------------------
# Example 2: Handling Mixed Date Formats
# ------------------------------------------------------------------------------
print("--- Example 2: Handling Mixed Date Formats ---")
input_list = ["2023-01-01", "2023-01-02", "3/10/2020 143045", "13th of October, 2023"]
print("Original Date Strings:", input_list)

print("\n======= Before convert ============")
print("datatype is", type(input_list))

output_mixed = pd.to_datetime(input_list, format="mixed")
print("\n======= After convert ============")
print("Converted DateTime Objects:\n", output_mixed)
print("datatype is", type(output_mixed))
print("\n")

# ------------------------------------------------------------------------------
# Example 3: String Column to DateTime in DataFrame
# ------------------------------------------------------------------------------
print("--- Example 3: String Column to DateTime ---")
df_patients = pd.DataFrame({
    "patientID": [101, 23, 48, 49],
    "name": ["alice", "bob", "charlie", "Eric"],
    "date_of_birth": ["2023-01-01", "2023-01-02", "3/10/2020 143045", "13th of October, 2023"],
})

print("======= Before convert ============")
print("Original DataFrame:\n", df_patients)
print("Data Type of date_of_birth:", df_patients["date_of_birth"].dtype)

df_patients["date_of_birth"] = pd.to_datetime(
    df_patients["date_of_birth"], format="mixed", dayfirst=True, errors="coerce"
)

print("\n======= After convert ============")
print("Data Type of date_of_birth:", df_patients["date_of_birth"].dtype)
print("Converted DataFrame:\n", df_patients)
print("\n")

# ------------------------------------------------------------------------------
# Example 4: Handling Parsing Errors with errors='coerce' / 'ignore'
# ------------------------------------------------------------------------------
print("--- Example 4: Handling Mismatched Format Errors ---")
df_errors = pd.DataFrame({
    "patientID": [101, 23, 48, 49],
    "name": ["alice", "bob", "charlie", "keyla"],
    "date_of_birth": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
})

print("======= Before ============")
print("Data Type of date_of_birth:", df_errors["date_of_birth"].dtype)

# Standard format conversion (Y-m-d)
df_errors["date_of_birth"] = pd.to_datetime(df_errors["date_of_birth"], format="%Y-%m-%d")

print("\n======= After ============")
print("Data Type of date_of_birth:", df_errors["date_of_birth"].dtype)
print(df_errors)
print("\n")

# ------------------------------------------------------------------------------
# Example 5: Importing CSV Data with parse_dates
# ------------------------------------------------------------------------------
print("--- Example 5: Parse Dates on CSV Import ---")
url = "https://raw.githubusercontent.com/bprasad26/lwd/master/data/tesla_stock_prices.csv"

tesla_df = pd.read_csv(url, parse_dates=["Date"], date_format="%Y-%m-%d")
tesla_df["Date"] = pd.to_datetime(tesla_df["Date"], errors="coerce")

print("Tesla Dtypes:\n", tesla_df.dtypes)
print("\nTesla Head:\n", tesla_df.head())
print("\n")

# ------------------------------------------------------------------------------
# Example 6: Extracting Day, Month, Year, and Day Name
# ------------------------------------------------------------------------------
print("--- Example 6: Extract Date Components ---")
tesla_df["Day"] = tesla_df["Date"].dt.day
tesla_df["Month"] = tesla_df["Date"].dt.month
tesla_df["Year"] = tesla_df["Date"].dt.year
tesla_df["day_name_sample"] = tesla_df["Date"].dt.day_name()

print(tesla_df[["Date", "Day", "Month", "Year", "day_name_sample"]].head(10))
print("\nMax Date:", tesla_df["Date"].max())
print("Min Date:", tesla_df["Date"].min())
print("\n")

# ------------------------------------------------------------------------------
# Example 7: Group By Month & Filtering
# ------------------------------------------------------------------------------
print("--- Example 7: Group By Month and Filtering ---")
monthly_sales = tesla_df.groupby(["Year", "Month"])["Volume"].sum().reset_index()
print("Monthly Volume Summary (First 5):\n", monthly_sales.head())

# Filter via loc
filtered_loc = tesla_df.loc[(tesla_df["Date"] >= "2010-02-01") & (tesla_df["Date"] < "2010-12-01")]
print("\nFiltered via loc (Count):", len(filtered_loc))

# Filter via query
filtered_query = tesla_df.query("Date >= '2010-02-01' and Date < '2010-12-01'")
print("Filtered via query (Count):", len(filtered_query))

# Filter Wednesday entries (weekday == 2)
wednesdays_df = tesla_df.loc[tesla_df["Date"].dt.weekday == 2]
print("Wednesday Entries (First 5):\n", wednesdays_df[["Date", "Close"]].head())
print("\n")
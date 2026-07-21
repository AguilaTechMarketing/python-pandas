import numpy as np
import pandas as pd

# ==============================================================================
# Guided Lab 386.3.13 - Select Columns and Rows of a Pandas DataFrame
#                       using Square Notation []
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Dataset Loading & Exploration
# ------------------------------------------------------------------------------
print("\n-- 1. Loading cars.json Dataset ---")
df_cars = pd.read_json("./data/cars.json")

print("------ First 5 Rows -------")
print(df_cars.head())
print("\n")

print("------ Column Names ------")
print(df_cars.columns)
print("\n")

print("------ DataFrame Info ------")
print(df_cars.info())
print("\n")

# ------------------------------------------------------------------------------
# 2. Selecting Columns
# ------------------------------------------------------------------------------
print("--- Example 1 & 2: Select Single Column ('Car') ---")
print(df_cars["Car"].head(10))
print("\n")

print("--- Example 3: Select Multiple Columns ('Car', 'Model', 'quantity') ---")
print(df_cars[["Car", "Model", "quantity"]].head())
print("\n")

# ------------------------------------------------------------------------------
# 3. Filtering Rows by Value / Condition
# ------------------------------------------------------------------------------
print("--- Example 4: Filter Rows where MPG == 17.6 ---")
print(df_cars[df_cars.MPG == 17.6])
print("\nAlternative using .eq():")
print(df_cars[df_cars["MPG"].eq(17.6)])
print("\n")

print("--- Example 5: Filter Rows where quantity > 350 ---")
get_quantity = df_cars[df_cars["quantity"] > 350]
print(get_quantity.head())
print("\n")

print("--- Example 6: Combine Conditions with AND (&) ---")
# Quantity > 350 AND Cylinders < 4
filtered_cars = df_cars[(df_cars["quantity"] > 350) & (df_cars["Cylinders"] < 4)]
print(filtered_cars)
print("\n")

print("--- Example 7: Combine Conditions with OR (|) and .isin() ---")
# City matching TEXAS or NewYork using OR (|)
print("Using OR (|):")
print(df_cars[((df_cars["city"] == "TEXAS") | (df_cars["city"] == "NewYork"))].head())

# City matching TEXAS or NewYork using .isin()
print("\nUsing .isin():")
print(df_cars[df_cars["city"].isin(["TEXAS", "NewYork"])].head())
print("\n")

# ------------------------------------------------------------------------------
# 4. String Method Filtering (.str)
# ------------------------------------------------------------------------------
print("--- Example 8: Filter Car Names Starting with 'M' ---")
print(df_cars[df_cars["Car"].str.startswith("M")].head())
print("\n")

print("--- Example 9: Filter Car Names Ending with 'm' ---")
print(df_cars[df_cars["Car"].str.endswith("m")].head())
print("\n")

print("--- Example 10: Filter Car Names Length > 20 Characters ---")
print(df_cars[df_cars["Car"].str.len() > 20].head())
print("\n")

# ------------------------------------------------------------------------------
# 5. Handling Missing Data (NaN)
# ------------------------------------------------------------------------------
print("--- Example 11: Cleaning Missing Values ---")
employee_list = [
    ["James", 36, 75, 5428000],
    ["Villers", 38, 74, 3428000],
    ["VKole", 31, 70, 8428000],
    ["Smith", 34, 80, 4428000],
    ["Gayle", 40, 100, 4528000],
    ["Adam", 40, np.nan, 4528000],
    ["Rooter", 33, 72, 7028000],
    ["Peterson", 42, 85, 2528000],
    ["lynda", 42, 85, np.nan],
    [np.nan, 42, 85, np.nan],
    ["Jenny", np.nan, 100, 25632],
    ["Kenn", np.nan, 110, 25632],
    ["Aly", np.nan, 90, 25582],
    ["John", 41, 85, 1528000],
]

df_emp = pd.DataFrame(employee_list, columns=["Name", "Age", "Weight", "Salary"])
print("------ Original Employee DataFrame with NaNs ------")
print(df_emp)
print("\n")

print("------ After Dropping Rows with NaNs (df.dropna()) ------")
df_cleaned_rows = df_emp.dropna()
print(df_cleaned_rows)
print("\n")

print("------ After Dropping Columns with NaNs (df.dropna(axis=1)) ------")
df_cleaned_cols = df_emp.dropna(axis=1)
print(df_cleaned_cols)
print("\n")
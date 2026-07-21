import pandas as pd

# ==============================================================================
# Guided Lab 386.3.6 - How to Select Columns in Pandas DataFrames
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Import Dataset
# ------------------------------------------------------------------------------
print("\n--- 1. Loading cars.json Dataset ---")
df_cars = pd.read_json("./data/cars.json")
print("Dataset Loaded Successfully!")
print("\n")

# ------------------------------------------------------------------------------
# 2. View Column Names by Index Number (.columns)
# ------------------------------------------------------------------------------
print("--- 2A. Single Column Name by Index 0 ---")
print("Column Name at Index 0:", df_cars.columns[0])
print("\n")

print("--- 2B. Multiple Column Names by Index List [0, 1, 9] ---")
print("Column Names at Index [0, 1, 9]:\n", df_cars.columns[[0, 1, 9]])
print("\n")

# ------------------------------------------------------------------------------
# 3. Select Single Column Data using Square Brackets [ ]
# ------------------------------------------------------------------------------
print("--- 3A. Direct Access: df_cars['Car'] ---")
print(df_cars["Car"].head())  # Truncated with .head() for clean terminal output
print("\n")

print("--- 3B. Dynamic Selection: df_cars[df_cars.columns[0]] ---")
print(df_cars[df_cars.columns[0]].head())
print("\n")

# ------------------------------------------------------------------------------
# 4. Select Multiple Columns Data by Index Positions
# ------------------------------------------------------------------------------
print("--- 4. Multiple Columns Data by Index Positions [0, 1, 9] ---")
print(df_cars[df_cars.columns[[0, 1, 9]]].head())
print("\n")

# ------------------------------------------------------------------------------
# 5. Select Multiple Columns Data using Square Brackets [ ]
# ------------------------------------------------------------------------------
print("--- 5. Multiple Columns Data by Name ('Car', 'Model', 'quantity') ---")
print(df_cars[["Car", "Model", "quantity"]].head())
print("\n")
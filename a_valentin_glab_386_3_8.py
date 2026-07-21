import pandas as pd

# ==============================================================================
# Guided Lab - 386.3.8 - How to Convert Pandas Column to List
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------------------------
print("\n--- 1. Loading cars.json Dataset ---")
df_cars = pd.read_json("./data/cars.json")
print("Dataset Loaded Successfully!")
print("\n")

# ------------------------------------------------------------------------------
# Example 1: Converting Pandas Column to List using .values.tolist()
# ------------------------------------------------------------------------------
print("--- Example 1A: Dot Notation (df_cars.Car.values.tolist()) ---")
col_list_dot = df_cars.Car.values.tolist()
print("First 5 elements:", col_list_dot[:5])
print("Type:", type(col_list_dot))
print("\n")

print("--- Example 1B: Bracket Notation (df_cars['Car'].values.tolist()) ---")
col_list_bracket = df_cars["Car"].values.tolist()
print("First 5 elements:", col_list_bracket[:5])
print("\n")

# ------------------------------------------------------------------------------
# Example 2: Converting Pandas Column to List using list() Function
# ------------------------------------------------------------------------------
print("--- Example 2: Using built-in list() function ---")
col_list_func = list(df_cars["Car"])
print("First 5 elements:", col_list_func[:5])
print("Type:", type(col_list_func))
print("\n")

# ------------------------------------------------------------------------------
# Example 3: Convert Pandas Column to NumPy Array (.to_numpy())
# ------------------------------------------------------------------------------
print("--- Example 3: Converting Column to NumPy Array ---")
col_array = df_cars["Car"].to_numpy()
print("First 5 elements:", col_array[:5])
print("Type:", type(col_array))
print("\n")

# ------------------------------------------------------------------------------
# Example 4: Converting Column to List by Column Index
# ------------------------------------------------------------------------------
print("--- Example 4: Convert Column by Index (df_cars.columns[0]) ---")
col_by_index = df_cars[df_cars.columns[0]].values.tolist()
print("First 5 elements:", col_by_index[:5])
print("Type:", type(col_by_index))
print("\n")

# ------------------------------------------------------------------------------
# Example 5: Convert Index Column to List
# ------------------------------------------------------------------------------
print("--- Example 5: Extract DataFrame Index as List ---")
index_list = df_cars.index.tolist()
print("First 10 index values:", index_list[:10])
print("Total index elements:", len(index_list))
print("Type:", type(index_list))
print("\n")
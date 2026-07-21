import pandas as pd

# ==============================================================================
# Guided Lab 386.3.10 - Sorting a Pandas DataFrame
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1: Sorting a Custom Student DataFrame
# ------------------------------------------------------------------------------
print("\n--- Example 1A: Creating and Enriching Student DataFrame ---")
data = {
    "Name": ["Jane", "Princi", "James", "Fadi"],
    "Height": [5.1, 6.2, 5.1, 5.2],
    "Qualification": ["Msc", "MA", "Msc", "Msc"],
    "Score 1": [56, 86, 77, 45],
    "Score 2": [50, 96, 60, 30],
}

df = pd.DataFrame(data)
print("------ Before ------")
print(df)

df = df.assign(address=["NYC", "NJ", "CA", "PA"])
print("\n------ After Adding Address Column ------")
print(df)
print("\n")

print("--- Example 1B: Sorting by Single Column (Score 1 - Descending) ---")
print(df.sort_values(by="Score 1", ascending=False))
print("\n")

print("--- Example 1C: Sorting by Multiple Columns (Score 1 Desc, Height Asc) ---")
print(df.sort_values(by=["Score 1", "Height"], ascending=[False, True]))
print("\n")

# ------------------------------------------------------------------------------
# Example 2: Sorting the Cars JSON Dataset
# ------------------------------------------------------------------------------
print("--- Example 2A: Loading Cars Dataset ---")
df_cars = pd.read_json("./data/cars.json")

print("------ Before (Top 15 Rows) ------")
print(df_cars.head(15))
print("\n")

print("--- Example 2B: Sorting by Quantity (Ascending) ---")
print(df_cars.sort_values(by=["quantity"], ascending=[True]).head())
print("\n")

print("--- Example 2C: Sorting by Quantity (Desc) and Car Name (Asc) ---")
print(df_cars.sort_values(by=["quantity", "Car"], ascending=[False, True]).head())
print("\n")
import pandas as pd

# ==============================================================================
# Guided Lab 386.4.1 - Concatenate Multiple Data Frames
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1: Basic DataFrame Concatenation (Rows & Keys)
# ------------------------------------------------------------------------------
print("\n--- Example 1A: Basic Concatenation (Preserving Original Index) ---")
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    }
)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    }
)

frames = [df1, df2, df3]
result_basic = pd.concat(frames)
print(result_basic)
print("\n")

print("--- Example 1B: Concatenation with ignore_index=True ---")
result_ignored = pd.concat(frames, ignore_index=True)
print(result_ignored)
print("\n")

print("--- Example 1C: Assigning Keys to Create MultiIndex ---")
result_keys = pd.concat(frames, keys=["x", "y", "z"])
print(result_keys)

print("\nAccessing sub-DataFrame with Key 'y':")
print(result_keys.loc["y"])
print("\n")

# ------------------------------------------------------------------------------
# Concatenating Along Different Axes & Differing Columns
# ------------------------------------------------------------------------------
print("--- Concatenating with Differing Columns & Axes ---")
df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[12, 13, 14, 15],
)

print("Concatenate along rows (axis=0, ignore_index=True):")
print(pd.concat([df1, df4], ignore_index=True, sort=False))

print("\nConcatenate along columns (axis=1):")
print(pd.concat([df1, df4], axis=1, sort=False))
print("\n")

# ------------------------------------------------------------------------------
# Example 2: Reading & Concatenating Multiple CSV Files
# ------------------------------------------------------------------------------
print("--- Example 2: Concatenating RealEstate CSV Files ---")
real_estate_df1 = pd.read_csv("./data/RealEstate1.csv")
real_estate_df2 = pd.read_csv("./data/RealEstate2.csv")
real_estate_df3 = pd.read_csv("./data/RealEstate3.csv")

# Clean column headers across all three datasets
real_estate_df1.columns = real_estate_df1.columns.str.strip()
real_estate_df2.columns = real_estate_df2.columns.str.strip()
real_estate_df3.columns = real_estate_df3.columns.str.strip()

real_estate_combined = pd.concat(
    [real_estate_df1, real_estate_df2, real_estate_df3],
    axis=0,
    ignore_index=True,
)

print("Combined Real Estate DataFrame (Top 5):")
print(real_estate_combined.head())
print("\n")

# ------------------------------------------------------------------------------
# Column Selection & Filtering on Concatenated Data
# ------------------------------------------------------------------------------
print("--- Accessing Specific Columns & Filtering ---")

print("1. Select Column by Positional Index (df.columns[1]):")
print(real_estate_combined[real_estate_combined.columns[1]].head())
print("\n")

print("2. Select 'MLS' Column as Series:")
print(real_estate_combined["MLS"].head())
print("\n")

print("3. Filter Rows where Bedrooms > 3:")
bedrooms_gt_3 = real_estate_combined[real_estate_combined["Bedrooms"] > 3]
print(bedrooms_gt_3.head())
print("\n")
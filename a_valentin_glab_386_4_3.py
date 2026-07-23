import pandas as pd

# ==============================================================================
# Guided Lab 386.4.3 - How to Join Multiple DataFrames using join() Function
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Setup DataFrames
# ------------------------------------------------------------------------------
print("\n--- 1. Initial DataFrames Setup ---")
technologies = {
    "Courses": ["Spark", "PySpark", "Python", "pandas"],
    "Fee": [20000, 25000, 22000, 30000],
    "Duration": ["30days", "40days", "35days", "50days"],
}
index_labels = ["r1", "r2", "r3", "r4"]
df1 = pd.DataFrame(technologies, index=index_labels)

technologies2 = {
    "Courses": ["Spark", "Java", "Python", "Go"],
    "Discount": [2000, 2300, 1200, 2000],
}
index_labels2 = ["r1", "r6", "r3", "r5"]
df2 = pd.DataFrame(technologies2, index=index_labels2)

print("First DataFrame (df1):\n", df1)
print("\nSecond DataFrame (df2):\n", df2)
print("\n")

# ------------------------------------------------------------------------------
# 2. Default Join Operation (Left Join on Index)
# ------------------------------------------------------------------------------
print("--- 2. Default Left Join on Index ---")
# Using lsuffix and rsuffix to resolve overlapping column 'Courses'
df3_default = df1.join(df2, lsuffix="_left", rsuffix="_right")
print("After joining two DataFrames (Left Join):\n", df3_default)
print("Result Shape:", df3_default.shape)
print("\n")

# ------------------------------------------------------------------------------
# 3. Inner Join DataFrames
# ------------------------------------------------------------------------------
print("--- 3. Inner Join on Index ---")
df3_inner = df1.join(df2, lsuffix="_left", rsuffix="_right", how="inner")
print("Inner Join Result:\n", df3_inner)
print("\n")

# ------------------------------------------------------------------------------
# 4. Right Join DataFrames
# ------------------------------------------------------------------------------
print("--- 4. Right Join on Index ---")
df3_right = df1.join(df2, lsuffix="_left", rsuffix="_right", how="right")
print("Right Join Result:\n", df3_right)
print("\n")

# ------------------------------------------------------------------------------
# 5. Pandas Join on Column (converting to index)
# ------------------------------------------------------------------------------
print("--- 5. Join on Column 'Courses' (Setting as Index) ---")
df3_col_join = df1.set_index("Courses").join(
    df2.set_index("Courses"), how="inner"
)
print("Joined on 'Courses' as Index:\n", df3_col_join)
print("\n")

# ------------------------------------------------------------------------------
# 6. Pandas Join Persisting Original Row Index
# ------------------------------------------------------------------------------
print("--- 6. Join on Column 'Courses' Persisting Original Row Index ---")
df3_persist_idx = df1.join(df2.set_index("Courses"), how="inner", on="Courses")
print("Joined on 'Courses' while keeping row labels:\n", df3_persist_idx)
print("\n")
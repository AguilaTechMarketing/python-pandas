import pandas as pd

# ==============================================================================
# Guided Lab 386.4.2 - How to Merge Pandas DataFrames by Multiple Columns
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Setup Initial DataFrames
# ------------------------------------------------------------------------------
print("\n--- 1. Initial DataFrames Setup ---")
left_df = pd.DataFrame(
    {
        "Courses": ["Spark", "PySpark", "Python", "pandas", "Java"],
        "Fee": [20000, 25000, 30000, 24000, 40000],
        "Duration": ["30day", "40days", "60days", "55days", "50days"],
    }
)

right_df = pd.DataFrame(
    {
        "Courses": ["Java", "PySpark", "Python", "pandas", "Hyperion", "html"],
        "Fee": [20000, 25000, 30000, 24000, 40000, 4000],
        "Percentage": ["10%", "20%", "25%", "20%", "10%", "50%"],
    }
)

print("Left DataFrame:\n", left_df)
print("\nRight DataFrame:\n", right_df)
print("\n")

# ------------------------------------------------------------------------------
# 2. Merge Default (Intersection of Common Columns)
# ------------------------------------------------------------------------------
print("--- 2. Default Merge (Auto-detects Common Columns) ---")
merged_default = pd.merge(left_df, right_df)
print(merged_default)
print("Result Shape:", merged_default.shape)
print("\n")

# ------------------------------------------------------------------------------
# 3. Merge on a Single Column
# ------------------------------------------------------------------------------
print("--- 3. Merge Based on Single Column ('Courses') ---")
merged_single = pd.merge(left_df, right_df, on="Courses")
print(merged_single)
print("Result Shape:", merged_single.shape)
print("\n")

# ------------------------------------------------------------------------------
# 4. Merge on Multiple Columns
# ------------------------------------------------------------------------------
print("--- 4. Merge Based on Multiple Columns ('Courses', 'Fee') ---")
merged_multi = pd.merge(left_df, right_df, on=["Courses", "Fee"])
print("After merging the DataFrames:\n", merged_multi)
print("Result Shape:", merged_multi.shape)
print("\n")

# ------------------------------------------------------------------------------
# 5. Merge with Explicit left_on and right_on
# ------------------------------------------------------------------------------
print("--- 5. Merge with left_on and right_on Parameters ---")
merged_explicit = pd.merge(
    left_df,
    right_df,
    how="left",
    left_on=["Courses", "Fee"],
    right_on=["Courses", "Fee"],
)
print("After merging the DataFrames:\n", merged_explicit)
print("Result Shape:", merged_explicit.shape)
print("\n")

# ------------------------------------------------------------------------------
# 6. Checking and Validating Duplicate Keys
# ------------------------------------------------------------------------------
print("--- 6. Handling Duplicate Keys with validate Parameter ---")
left = pd.DataFrame({"A": [1, 2], "B": [1, 2]})
right = pd.DataFrame({"A": [4, 5, 6], "B": [2, 2, 2]})

# Validating one_to_many relationship
result_validate = pd.merge(left, right, on="B", how="inner", validate="one_to_many")
print("One-to-Many Validated Merge Result:\n", result_validate)
print("\n")

# ------------------------------------------------------------------------------
# 7. Real-World Scenario: Sales Transactions and Product Details
# ------------------------------------------------------------------------------
print("--- 7. Real-World Scenario: Sales & Products Merge ---")
sales_data = {
    "TransactionID": [1, 2, 3, 4, 5],
    "ProductID": [101, 102, 103, 101, 105],
    "StoreID": [1, 2, 1, 3, 2],
    "Quantity": [5, 3, 2, 4, 1],
    "Amount": [500.00, 300.00, 200.00, 400.00, 150.00],
}
df_sales = pd.DataFrame(sales_data)

products_data = {
    "ProductID": [101, 102, 103, 104, 105],
    "ProductName": ["Laptop", "Headphones", "Smartphone", "Tablet", "Monitor"],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
    ],
}
df_products = pd.DataFrame(products_data)

df_combined = pd.merge(df_sales, df_products, on="ProductID", how="left")
print("Combined Sales & Products DataFrame:\n", df_combined)
print("\n")
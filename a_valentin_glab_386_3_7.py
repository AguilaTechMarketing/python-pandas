import pandas as pd

# ==============================================================================
# Guided Lab 386.3.7 - Count the Occurrences of Unique Values from Column
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1: Frequency Analysis (Product Categories)
# ------------------------------------------------------------------------------
print("\n--- Example 1: Category Frequency Analysis ---")
data_cat = {
    "Category": [
        "Electronics",
        "Clothing",
        "Electronics",
        "Books",
        "Books",
        "Clothing",
    ]
}
df_cat = pd.DataFrame(data_cat)

category_counts = df_cat["Category"].value_counts()
print(category_counts)
print("\n")

# ------------------------------------------------------------------------------
# Example 2: Brand Frequency Analysis & Finding Items > 1 Count
# ------------------------------------------------------------------------------
print("--- Example 2: Device Brand Frequency Analysis ---")
sales_data = {
    "Devices": [
        "Laptop",
        "iPhone",
        "LED",
        "LCD",
        "Smart-Phone",
        "Washing-Machine",
    ],
    "Brand": ["Lenovo", "Apple", "Samsung", "Samsung", "Samsung", "Whirpool"],
    "Sales": [1000, 2000, 4000, 2000, 1000, 4000],
    "Profit": [500, 1000, 1000, 1500, 1000, 1500],
    "Pices left": [5000, 4000, 4000, 5000, 5000, 1000],
}
df_sales = pd.DataFrame(sales_data)

frequency = df_sales.Brand.value_counts()
frequent_product = frequency[frequency > 1].index[0]

print(frequency)
print("This item appears more than once:", frequent_product)
print("\n")

# ------------------------------------------------------------------------------
# Example 3: Checking Missing Values (dropna=False)
# ------------------------------------------------------------------------------
print("--- Example 3: Score Frequency Including Missing Values (NaN) ---")
data_score = {"Score": [85, 92, 88, 75, None, 90, None, 85]}
df_score = pd.DataFrame(data_score)

score_counts = df_score["Score"].value_counts(dropna=False)
print(score_counts)
print("\n")

# ------------------------------------------------------------------------------
# Example 4: Checking Data Quality (Age Outliers/Distribution)
# ------------------------------------------------------------------------------
print("--- Example 4: Age Distribution Analysis ---")
data_age = {"Age": [25, 30, 25, 35, 25, 40, 25, 30, 45, 25, 30, 25]}
df_age = pd.DataFrame(data_age)

age_counts = df_age["Age"].value_counts()
print(age_counts)
print("\n")
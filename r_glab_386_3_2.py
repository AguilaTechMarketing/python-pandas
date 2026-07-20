import numpy as np
import pandas as pd


# ==============================================================================
# Guided Lab - 386.3.2 - Creating a Pandas DataFrame
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1.1: Creating a DataFrame from Dictionaries
# ------------------------------------------------------------------------------
print("\n--- Example 1.1: Basic Dictionary DataFrame ---")
d = {"x": [1, 2, 3], "y": [2, 4, 8], "z": 100}
df1_1a = pd.DataFrame(d)
print(df1_1a)
print("\n")

print("--- Example 1.1: Custom Index and Column Order ---")
df1_1b = pd.DataFrame(d, index=[100, 200, 300], columns=["z", "y", "x"])
print(df1_1b)
print("\n")

# ------------------------------------------------------------------------------
# --- Example 1.2: Setting an Existing Column as Index
# ------------------------------------------------------------------------------

print("--- Example 1.2: Student DF Before set_index ---")
student_dict = {
    "Name": ["Joe", "Nat", "Harry"],
    "Age": [20, 21, 19],
    "Marks": [85.10, 77.80, 91.54]
}
student_df = pd.DataFrame(student_dict)
print(student_df)
print("\n")

print("--- Example 1.2: Student DF After set_index('Name') ---")
student_df = student_df.set_index("Name")
print(student_df)
print("\n")

# ------------------------------------------------------------------------------
# --- Example 1.3: Creating a DataFrame with a Custom RangeIndex
# ------------------------------------------------------------------------------
print("--- Example 1.3: Product DF Default Index ---")
data = {
    "Product": ["Laptop", "Tablet", "Phone"],
    "Price": [1200, 300, 800],
    "Quantity": [50, 150, 100],
}
product_df = pd.DataFrame(data)
print(product_df)
print("\n")

print("--- Example 1.3: Product DF with Custom RangeIndex (1-3) ---")
product_df.index = pd.RangeIndex(start=1, stop=4, step=1)
print(product_df)
print("\n")

# ------------------------------------------------------------------------------
# --- Example 2.1: DataFrame from List using zip()
# ------------------------------------------------------------------------------
print("--- Example 2.1: Patient Records using zip() ---")
patientID = [101, 23, 48, 49]
name = ["alice", "bob", "charlie", "Eric"]
date_of_birth = [
    "2023-01-01",
    "2023-01-02",
    "3/10/2020 143045",
    "13th of October, 2023",
]

patient_df = pd.DataFrame(
    zip(patientID, name, date_of_birth),
    columns=["patientID", "name", "date_of_birth"],
)
print(patient_df)
print("\n")


# ------------------------------------------------------------------------------
# Example 2.2: Stock Prices using zip()
# ------------------------------------------------------------------------------
print("--- Example 2.2: Stock Prices using zip() ---")
stocks = ["IBM", "APPLE", "TWTTY", "GE", "MSFT"]
prices = [115.00, 119.14, 19.77, 25.99, 26]

stocks_df = pd.DataFrame(zip(stocks, prices), columns=["stocks", "prices"])
print(stocks_df)
print("\n")

# ------------------------------------------------------------------------------
# Example 2.3: DataFrame from List of Dictionaries & Nested Lists
# ------------------------------------------------------------------------------

print("--- Example 2.3: DataFrame from List of Dictionaries ---")
dict_list = [
    {"x": 1, "y": 2, "z": 100},
    {"x": 2, "y":  4, "z": 100},
    {"x": 3, "y": 8, "z": 100},
]
df_from_dicts = pd.DataFrame(dict_list)
print(df_from_dicts)
print("\n")

print("--- Example 2.3: Nested Lists with Column Labels ---")
nested_list = [[1, 2, 100], [2, 4, 100], [3, 8, 100]]
df_from_nested = pd.DataFrame(nested_list, columns=["x", "y", "z"])
print(df_from_nested)
print("\n")

# ------------------------------------------------------------------------------
# Example 3.0: DataFrame from NumPy Array (Reference vs. Copy Behavior)
# ------------------------------------------------------------------------------
print("--- Example 3: DataFrame from NumPy Array ---")
arr = np.array([[1, 2, 100], [2, 4, 100], [3, 8, 100]])
arr_df = pd.DataFrame(arr, columns=["x", "y", "z"], copy=False)
print("Original DataFrame:")
print(arr_df)
print("\n")

print("--- Example 3: Modifying Underlying NumPy Array (arr[0, 0] = 1000) ---")
arr[0, 0] = 1000  # Modifying array directly affects DataFrame when copy=False
print("DataFrame After Array Modification:")
print(arr_df)
print("\n")
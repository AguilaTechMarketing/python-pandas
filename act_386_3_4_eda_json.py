import pandas as pd

# ==============================================================================
# Guided Lab - 386.3.4 - Exploratory Data Analysis on JSON Data
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Loading Data & Checking Data Types (.dtypes)
# ------------------------------------------------------------------------------
print("--- 1. Data Type Inspection ---")
df_cars = pd.read_json("./data/cars.json")
print(df_cars.dtypes)
print("\n")

# ------------------------------------------------------------------------------
# 2. Descriptive Statistics (.describe())
# ------------------------------------------------------------------------------
print("--- 2. Descriptive Statistics Summary ---")
print(df_cars.describe())
print("\n")

# ------------------------------------------------------------------------------
# 3. Concise Summary & Metadata (.info() and .count())
# ------------------------------------------------------------------------------
print("--- 3A. Non-Null Counts per Column (.count()) ---")
print(df_cars.count())
print("\n")

print("--- 3B. Comprehensive Dataset Info (.info()) ---")
print(df_cars.info())
print("\n")

# ------------------------------------------------------------------------------
# 4. Data Selection (.head(), .tail(), .at, .iat)
# ------------------------------------------------------------------------------
print("--- 4A. Top 2 Rows (.head(2)) ---")
print(df_cars.head(2))
print("\n")

print("--- 4B. Bottom 2 Rows (.tail(2)) ---")
print(df_cars.tail(2))
print("\n")

print("--- 4C. Accessing Specific Element using .at[157, 'MPG'] ---")
print(df_cars.at[157, "MPG"])
print("\n")

print("--- 4D. Accessing Specific Element using .iat[157, 1] (Row 157, Col 1) ---")
print(df_cars.iat[157, 1])
print("\n")

# ------------------------------------------------------------------------------
# 5. Data Shape, Size, and Column Indices
# ------------------------------------------------------------------------------
print("--- 5A. Shape and Dimensions ---")
print("Total (Rows, Columns):", df_cars.shape)
print("Rows only:", df_cars.shape[0])
print("Columns only:", df_cars.shape[1])
print("\n")

# Student Dictionary Column Attribute Demonstration from Lab Notes
print("--- 5B. Student DataFrame Column Index Attributes ---")
student_dict = {
    "Name": ["Joe", "Nat", "Harry"],
    "Age": [20, 21, 19],
    "Marks": [85.10, 77.80, 91.54],
}
student_df = pd.DataFrame(student_dict)

list_Index = student_df.columns  # Get column index
print("Column Index:", list_Index)
print("1st Column Label:", student_df.columns[0])
Get_As_List = student_df.columns.tolist()  # Get columns as a list
print("Columns as List:", Get_As_List)
print("\n")

# ------------------------------------------------------------------------------
# 6. DataFrame Axes Length & Row Counting Alternative
# ------------------------------------------------------------------------------
print("--- 6. Axes and Row Length Extraction ---")
print("Both Axes Tuple:", df_cars.axes)
print("Row Axis Only:", df_cars.axes[0])
print("Total Row Count via len(df.axes[0]):", len(df_cars.axes[0]))
print("\n")
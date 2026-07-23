import numpy as np
import pandas as pd

# ==============================================================================
# R-Guided Lab 386.3.14 - Handling Missing Data
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1: Dropping Missing Data using df.dropna()
# ------------------------------------------------------------------------------
print("\n--- Example 1: Dropping Missing Data (.dropna()) ---")
employee_list_1 = [
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

df_emp1 = pd.DataFrame(employee_list_1, columns=["Name", "Age", "Weight", "Salary"])
print("------ Before Dropping Missing Data ------")
print(df_emp1)

print("\n------ After Dropping Missing Data (dropna()) ------")
df_emp1_cleaned = df_emp1.dropna()
print(df_emp1_cleaned)
print("\n")

# ------------------------------------------------------------------------------
# Example 2.1: fillna() on All Columns and Counting Nulls
# ------------------------------------------------------------------------------
print("--- Example 2.1: Counting and Filling NaN Values with 'None' ---")
employee_list_2 = [
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
    ["John", 41, 85, 1528000],
]

df_emp2 = pd.DataFrame(employee_list_2, columns=["Name", "Age", "Weight", "Salary"])
print("------ Before Cleaning NaN Values ------")
print(df_emp2)

print("\n------ Count of Missing Values ------")
print(df_emp2.isnull().sum())

print("\n------ After Filling NaN Values with 'None' ------")
print(df_emp2.fillna("None"))
print("\n")

# ------------------------------------------------------------------------------
# Example 2.2: Fill Same Value on Multiple Columns
# ------------------------------------------------------------------------------
print("--- Example 2.2: Filling Selected Columns with 'pending' ---")
df_emp_sub = df_emp1[["Weight", "Age"]].fillna("pending")
print(df_emp_sub)
print("\n")

# ------------------------------------------------------------------------------
# Example 2.3: Fill Different Values per Column
# ------------------------------------------------------------------------------
print("--- Example 2.3: Filling Custom Values per Column ---")
df_emp3 = pd.DataFrame(employee_list_1, columns=["Name", "Age", "Weight", "Salary"])

print("------ Before Cleaning NaN Values ------")
print(df_emp3)

print("\n------ After Cleaning NaN Values per Column ------")
df_emp3_filled = df_emp3.fillna(
    value={
        "Weight": "Pending",
        "Age": "Unknown",
        "Salary": "0.0",
        "Name": "Verification pending",
    }
)
print(df_emp3_filled)
print("\n")

# ------------------------------------------------------------------------------
# Example 3: Convert NaN to Empty String using .replace()
# ------------------------------------------------------------------------------
print("--- Example 3: Convert NaN to Empty String (.replace()) ---")
technologies = {
    "Courses": ["Spark", np.nan, "Hadoop", "Python", "pandas", np.nan, "Java"],
    "Fee": [20000, 25000, np.nan, 22000, 24000, np.nan, 22000],
    "Duration": [np.nan, "40days", "35days", np.nan, "60days", "50days", "55days"],
    "Discount": [1000, np.nan, 1500, np.nan, 2500, 2100, np.nan],
}
df_tech = pd.DataFrame(technologies)

df_tech_empty = df_tech.replace(np.nan, "", regex=True)
print(df_tech_empty)
print("\n")

# ------------------------------------------------------------------------------
# Example 4: Replace NaN on Multiple Columns with 'PENDING'
# ------------------------------------------------------------------------------
print("--- Example 4: Fill NaN on Specific Columns ('Courses', 'Fee') ---")
df_tech_multi = pd.DataFrame(technologies)
df_tech_multi[["Courses", "Fee"]] = df_tech_multi[["Courses", "Fee"]].fillna("PENDING")
print(df_tech_multi[["Courses", "Fee"]])
print("\n")

# ------------------------------------------------------------------------------
# Example 5: fillna() with inplace=True
# ------------------------------------------------------------------------------
print("--- Example 5: In-place NaN Replacement (inplace=True) ---")
df_tech_inplace = pd.DataFrame(technologies)

# Cast numeric columns so they can accept string empty values ''
df_tech_inplace = df_tech_inplace.astype(object)

df_tech_inplace.fillna("", inplace=True)
print(df_tech_inplace)
print("\n")

# ------------------------------------------------------------------------------
# Example 6: Handling Missing Data from CSV File
# ------------------------------------------------------------------------------
print("--- Example 6: Handling Missing Data from CSV ('./data/employee.csv') ---")
df_csv = pd.read_csv("./data/employee.csv", dtype={"Name": "string"})

print("------ Before Handling Missing Values ------")
print(df_csv)

print("\n------ After Handling Missing Values using fillna() ------")
df_csv_filled = df_csv.fillna(
    value={
        "Name": "Verification Pending",
        "Age": "Unknown",
        "Weight": "pending",
        "Salary": 0.0,
    }
)
print(df_csv_filled)
print("\n")

import pandas as pd

# ==============================================================================
# Guided Lab 386.3.11 - Slicing Pandas Dataframe’s Data
# ==============================================================================

# ------------------------------------------------------------------------------
# Method #1: Slicing DataFrame using DataFrame.iloc[] (Integer-based indexing)
# ------------------------------------------------------------------------------

# Initializing employee DataFrame
employee_list = [
    ["James", 36, 75, 5428000],
    ["Villers", 38, 74, 3428000],
    ["VKole", 31, 70, 8428000],
    ["Smith", 34, 80, 4428000],
    ["Gayle", 40, 100, 4528000],
    ["Rooter", 33, 72, 7028000],
    ["Peterson", 42, 85, 2528000],
    ["John", 41, 85, 1528000],
]
df_emp = pd.DataFrame(
    employee_list, columns=["Name", "Age", "Weight", "Salary"]
)

print("\n------ DataFrame Before Slicing ------")
print(df_emp)
print("\n")

# Example 1.1: Slicing by rows
print("--- Example 1.1A: Select First Row by Index (.iloc[:1]) ---")
print(df_emp.iloc[:1])
print("\n")

print("--- Example 1.1B: Slicing First 4 Rows (.iloc[0:4]) ---")
df1 = df_emp.iloc[0:4]
print(df1)
print("\n")

# Example 1.2: Slicing by columns
print("--- Example 1.2: Slicing First 2 Columns (.iloc[:, 0:2]) ---")
emp_df = df_emp.iloc[:, 0:2]
print(emp_df)
print("\n")

# Example 1.3: Slicing both rows and columns by integer range
print("--- Example 1.3: Rows 0-2 (excl) & Cols 0-2 (excl) ---")
print(df1.iloc[0:2, 0:2])
print("\n")

# ------------------------------------------------------------------------------
# Method #2: Slicing DataFrame using DataFrame.loc[] (Label-based indexing)
# ------------------------------------------------------------------------------

# Creating Demo Team Dataset
df_team = pd.DataFrame({
    "team": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "points": [18, 22, 19, 14, 14, 11, 20, 28],
    "assists": [5, 7, 7, 9, 12, 9, 9, 4],
    "rebounds": [11, 8, 10, 6, 6, 5, 9, 12],
    "steals": [4, 3, 3, 2, 5, 4, 3, 8],
    "blocks": [1, 0, 0, 3, 2, 2, 1, 5],
})

print("------ Team Demo DataFrame ------")
print(df_team)
print("\n")

# Example 2.1: Slice by Specific Column Names
print("--- Example 2.1: Specific Columns ('team', 'rebounds') ---")
df_new_cols = df_team.loc[:, ["team", "rebounds"]]
print(df_new_cols)
print("\n")

# Example 2.2: Slice by Column Names in Range
print("--- Example 2.2: Range of Columns ('team':'rebounds') ---")
df_range_cols = df_team.loc[:, "team":"rebounds"]
print(df_range_cols)
print("\n")

# Example 2.3: Select specific row label range and column label
print("--- Example 2.3: Row Labels 3:6 & 'team' Column ---")
print(df_team.loc[3:6, ["team"]])
print("\n")



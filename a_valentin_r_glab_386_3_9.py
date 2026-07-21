import pandas as pd

# ==============================================================================
# R-Guided Lab - 386.3.9 - Adding New Column to Existing DataFrame in Pandas
# ==============================================================================

# ------------------------------------------------------------------------------
# Method #1: Direct Assignment using Square Brackets [ ]
# ------------------------------------------------------------------------------

# Example 1.1: Adding a list as a new column
print("\n--- Example 1.1: Adding a List as a New Column ---")
data = {
    "Name": ["Jane", "Princi", "James", "Fadi"],
    "Height": [5.1, 6.2, 5.1, 5.2],
    "Qualification": ["Msc", "MA", "Msc", "Msc"],
    "Score 1": [56, 86, 77, 45],
    "Score 2": [50, 96, 60, 30],
}
df = pd.DataFrame(data)

print("------ Before Adding Column ------")
print(df)

address = ["NYC", "NJ", "CA", "PA"]
df["Address"] = address

print("\n------ After Adding Address Column ------")
print(df)
print("\n")


# Example 1.2: Adding a column derived from arithmetic operations
print("--- Example 1.2: Arithmetic Derived Column (Total_Score) ---")
df = pd.DataFrame(data)

print("------ Before ------")
print(df)

df["Total_Score"] = df["Score 1"] + df["Score 2"]

print("\n------ After Adding Total_Score Column ------")
print(df)
print("\n")


# Example 1.3: Calculating averages from derived columns
print("--- Example 1.3: Calculating Averages from Derived Columns ---")
df = pd.DataFrame(data)

print("------ Before ------")
print(df)

df["Total_Score"] = df["Score 1"] + df["Score 2"]
df["Total_Score_average"] = df["Total_Score"] / 2

print("\n------ After Adding Total_Score and Average Columns ------")
print(df)
print("\n")


# Example 1.4: Rearranging columns while creating a DataFrame
print("--- Example 1.4: Rearranging Columns During Construction ---")
df = pd.DataFrame(
    data, columns=["Score 1", "Score 2", "Name", "Qualification"]
)

print("------ Before ------")
print(df)

df["Total_Score"] = df["Score 1"] + df["Score 2"]

print("\n------ After Adding Total_Score Column ------")
print(df)
print("\n")


# Example 1.5: Creating a DataFrame from nested lists and vectorized calculation
print("--- Example 1.5: Derived Percentage Column from Nested List ---")
values = [
    ["Rohan", 455],
    ["Elvish", 250],
    ["John", 495],
    ["Sai", 400],
    ["Eric", 350],
    ["Adam", 450],
]
df_marks = pd.DataFrame(values, columns=["Name", "Univ_Marks"])

print("------ Data Frame Before Calculating Percentage ------")
print(df_marks)

df_marks["Percentage"] = df_marks["Univ_Marks"] / 500 * 100

print("\n------ Data Frame with Percentage Column ------")
print(df_marks)
print("\n")


# ------------------------------------------------------------------------------
# Method #2: Using DataFrame.insert() Function
# ------------------------------------------------------------------------------

# Example 2.1: Inserting a column at a specific index
print("--- Example 2.1: Inserting Column at Index Position 2 (.insert()) ---")
df = pd.DataFrame(data)

print("------ Before ------")
print(df)

df.insert(2, "Age", [21, 23, 24, 21], True)

print("\n------ After Inserting Age Column at Index 2 ------")
print(df)
print("\n")


# ------------------------------------------------------------------------------
# Method #3: Using DataFrame.assign() Function
# ------------------------------------------------------------------------------

# Example 3.1: Using assign() to add new columns
print("--- Example 3.1: Adding Column via .assign() ---")
df = pd.DataFrame(data)

print("------ Before ------")
print(df)

df = df.assign(address=["NYC", "NJ", "CA", "PA"])

print("\n------ After Adding Address via assign() ------")
print(df)
print("\n")
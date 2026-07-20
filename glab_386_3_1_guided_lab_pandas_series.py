import pandas as pd

# ==============================================================================
# Guided Lab - 386.3.1 - Pandas Series
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1.1: Dictionary to Series
# ------------------------------------------------------------------------------
print("--- Example 1.1: Standard Dictionary ---")
d1 = {"b": 1, "a": 0, "c": 2, "d": 100}
s1_1 = pd.Series(d1)
print(s1_1)
print("\n")

# ------------------------------------------------------------------------------
# Example 1.2: Dictionary with Float Values
# ------------------------------------------------------------------------------
print("--- Example 1.2: Float Dictionary ---")
d2 = {"a": 0.0, "b": 1.0, "c": 2.0}
s1_2 = pd.Series(d2)
print(s1_2)
print("\n")

# ------------------------------------------------------------------------------
# Example 1.3: Reordering and Missing Data (NaN)
# Passing a custom index pulls matching keys and inserts NaN for missing ones.
# ------------------------------------------------------------------------------
print("--- Example 1.3: Custom Index Alignment ---")
s1_3 = pd.Series(d2, index=["b", "c", "d", "a"])
print(s1_3)
print("\n")

# ------------------------------------------------------------------------------
# Example 2.1: Key/Value Objects as Series
# ------------------------------------------------------------------------------
print("--- Example 2.1: Calories Series ---")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar1 = pd.Series(calories)
print(myvar1)
print("\n")

# ------------------------------------------------------------------------------
# Example 2.2: Filtering Dictionary Items with Index
# ------------------------------------------------------------------------------
print("--- Example 2.2: Selected Days Only ---")
myvar2 = pd.Series(calories, index=["day1", "day2"])
print(myvar2)
print("\n")

# ------------------------------------------------------------------------------
# Example 3: Creating Series from a Scalar Value
# When data is a scalar (single number), an index MUST be provided.
# The value repeats across all index labels.
# ------------------------------------------------------------------------------
print("--- Example 3: Scalar Value Series ---")
s_scalar = pd.Series(5.0, index=["a", "b", "c", "d", "e"])
print(s_scalar)
print("\n")
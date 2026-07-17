import numpy as np
import pandas as pd

# ====================================
# ---   problem 1 ---
# ====================================

# Provided Setup Data
mylist = list("abcdefghijklmnopqrstuvwxyz")
myarray = np.arange(26)
mydict = dict(zip(mylist, myarray))

# ====================================
# ---   Solution 1A ---
# ====================================

# 1A. Convert the list to a Series and print the first 5 rows
print("--- Series from List ---")
series_from_list = pd.Series(mylist)
print(series_from_list.head())
print("\n")

# ====================================
# ---   Solution 1B ---
# ====================================

# 1B. Convert the NumPy array to a Series and print the first 5 rows
print("--- Series from NumPy Array ---")
series_from_arr = pd.Series(myarray)
print(series_from_arr.head())
print("\n")

# ====================================
# ---   Solution 1C ---
# ====================================

# 1C. Convert the dictionary to a Series and print the first 5 rows
print("--- Series from Dictionary ---")
series_from_dict = pd.Series(mydict)
print(series_from_dict.head())
print("\n")

# ====================================
# ---   problem 2 ---
# ====================================

# ====================================
# ---   Solution 2 ---
# ====================================

# 2. Create the series with the name parameter and print the first 5 rows
print("--- Named Series ---")
ser2 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'), name='alphabet')
print(ser2.head())
print("\n")

# ====================================
# ---   problem 3 ---
# ====================================

# ====================================
# ---   Solution 3 ---
# ====================================

# 3. Assign the name after creation using the .name attribute and verify
print("--- Renamed Series (After Creation) ---")
ser3 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser3.name = 'alphabet1'
print(ser3.head())
print("\n")

# ====================================
# ---   problem 4 ---
# ====================================

# Provided Setup Data
ser1 = pd.Series([2, 4, 6, 8, 10])
ser2_math = pd.Series([1, 3, 5, 7, 9])

# ====================================
# ---   Solution 4 ---
# ====================================

# 4A. Addition
print("--- Addition (ser1 + ser2) ---")
ser_add = ser1 + ser2_math
print(ser_add)
print("\n")

# 4B. Subtraction
print("--- Subtraction (ser1 - ser2) ---")
ser_sub = ser1 - ser2_math
print(ser_sub)
print("\n")

# 4C. Multiplication
print("--- Multiplication (ser1 * ser2) ---")
ser_mult = ser1 * ser2_math
print(ser_mult)
print("\n")

# 4D. Division
print("--- Division (ser1 / ser2) ---")
ser_div = ser1 / ser2_math
print(ser_div)
print("\n")

# ====================================
# ---   problem 5 ---
# ====================================

# Provided Setup Data
ser1_comp = pd.Series([2, 4, 5, 8, 10])
ser2_comp = pd.Series([1, 3, 5, 7, 10])

# ====================================
# ---   Solution 5 ---
# ====================================

# 5A. Check if elements are equal
print("--- Equal to (ser1 == ser2 ---)")
ser_equal =ser1_comp == ser2_comp
print(ser_equal)
print("\n")

# 5B. Check if elements are greater than
print("--- Greater Than (ser1_comp > ser2_comp) ---")
ser_greater = ser1_comp > ser2_comp
print(ser_greater)
print("\n")

# 5C. Check if elements are less than
print("--- Less Than (ser1 < ser2) ---")
ser_less = ser1_comp < ser2_comp
print(ser_less)
print("\n")
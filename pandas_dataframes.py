import pandas as pd

grades_dict = {"Wally": [87, 96, 70], "Eva": [100, 87, 90], 
            "Sam": [94, 77, 90], "Katie": [100, 81, 82],
            "Bob": [83, 65, 85]}

grades = pd.DataFrame(grades_dict)

print(grades)

print("\n\n")

grades.index = ["Test 1", "Test 2", "Test 3"]
print(grades)

print("\n\n")

print(grades.Sam)

print("\n\n")

# If you want to pull up a column or row based on a key, we can use "loc" and "iloc" functions...

# "loc" uses row indices
print(grades.loc[["Test 1", "Test 2"], ["Eva", "Katie"]])

print("\n\n")

print(grades.iloc[[0, 1], 1:3])

print(grades)
print("\n\n")

print(grades[grades > 90])
print(grades[(grades > 80) & (grades < 89)])
grades.at["Test2", "Eva"] = 100
print(grades.at["Test2", "Eva"])

print("\n\n")
print(grades)
print(grades.iat[1, 2])
print("\n\n")

pd.set_option("precision", 2)
print(grades.describe())

print("\n\n")

print(grades.mean())

print("\n\n")

print(grades.T.mean())      # "T" means "transpose"

print("\n\n")

print(grades.sort_index(ascending = False))
print(grades.sort_index(axis = 1))         # for the future - in the "axis" function - "0" is for "x (or columns)"    "1" is for "y (or rows)" 

print(grades.sort_values(by = "Test1", axis = 1, ascending = False))
print(grades.T.sort_values(by = "Test1", ascending = False))

print(grades.loc["Test1"].sort_values(ascending = False))       # python's dot notation is EXTREMELY powerful; 

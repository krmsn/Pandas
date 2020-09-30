import pandas as pd

grades = pd.Series([87, 100, 94])
# print(grades)

myarray = pd.Series(98.6, range(3))
# print(myarray)

# print(grades[0])

# print(grades.describe())

print("\n\n")

# Pandas can associate string values with integers, either the "list" way...
grades = pd.Series([87, 100, 94], index = ["Wally", "Eva", "Sam"])
print(grades)

# or the "dictionary" way...
grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})
print(grades)

print("\n\n")

print(grades["Eva"])

print(grades.Eva)

print(grades[1])

print(grades.dtype)

hardware = pd.Series(["Hammer", "Saw", "Wrench"])

a = hardware.str.contains("a")
print(a)

b = hardware.str.upper()
print(b)



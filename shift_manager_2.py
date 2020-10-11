import csv
import pandas as pd

print("\n\n\n\n\n")

# import the .csv file and format it to a DataFrame, with "csv_read()."
sched = pd.read_csv("Holiday Schedule Ranking 2019.csv", index_col = 0).T
sched_prefs = pd.read_csv("Holiday Schedule Ranking 2019.csv", index_col = 0)

sched["col_sum"] = sched.apply(lambda x:x.sum(), axis = 1)
sched = sched.sort_values(by = "col_sum", ascending = False)
print(sched)

print("\n\n\n\n\n")

print(sched_prefs)

print("\n\n\n\n\n")

# create a list of dates from the DataFrame 
# (where dates have been sorted by the lambda function), 
# then store them as keys in a dictionary.

employee_list = list(sched_prefs.index)
if "Employee" in employee_list:
    employee_list.remove("Employee")
employee_dict = dict.fromkeys({a for a in employee_list}, [])
print(sched_prefs.index)

print(employee_list)

print("\n\n\n\n\n")

print(employee_dict)

print("\n\n\n\n\n")

# create a list of employees from the DataFrame,
# then store them as keys in a dictionary.

date_list = list(sched.index)
date_dict = dict.fromkeys({b for b in date_list}, [])
print(date_list)

print("\n\n\n\n\n")

print(date_dict)

print("\n\n\n\n\n")

# nested loops
#

# iterate over dates in "col_sum" ordered list.
for c in date_list:
# will loop until each key in "date_dict" has 3 items.
    date_count = 1
    if len(date_dict[c]) < 3:
        emp_count = 1
        if emp_count < 4:
            for d in employee_list:
                if len(employee_dict[d]) < 2:
                    if sched_prefs.at[d, c] == emp_count:
                        print(emp_count)
                        print(sched_prefs.at[d, c])
                        print(d)
                        print(c)
                        date_dict[c].append(d)
                        employee_dict[d].append(c)
                        emp_count += 1
                    

"""

for c in sched.columns:
    sched[c].values[:] = 0  

sched.replace(, , inplace = True)
sched.to_csv("final_schedule.csv")

"""

print(employee_dict)
print("\n\n\n\n\n\n")
print(date_dict)

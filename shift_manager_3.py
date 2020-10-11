import csv
from datetime import datetime
import pandas as pd
import itertools

schedule = pd.read_csv("Holiday Schedule Ranking 2019.csv", index_col = 0).T

data = pd.DataFrame(data = 0, columns = schedule.columns, index  = schedule.index).T

"""
for c in schedule.columns:
    schedule[c].values[:] = 0
"""

schedule["col_sum"] = schedule.apply(lambda x:x.sum(), axis = 1)

schedule = schedule.sort_values(by = "col_sum", ascending = False)

date_dict = schedule.T.to_dict("dict")

schedule = schedule.T

for date in schedule.columns:
    date_series = schedule[date].nsmallest(5, keep = "all")
    date_series = date_series.to_dict()
    date_dict[date] = date_series

"""
    print(date_series)
    slot_count = 0
    if slot_count < 3:
        
        slot_count += 1
"""



for key, value in date_dict.items():

    print(key, value)

"""

MAX_SHIFTS = 3

trimmed_date_dict = dict(itertools.islice(date_dict.items(), MAX_SHIFTS))

print(trimmed_date_dict)
"""

"""

schedule.replace(0, "", inplace = True)
schedule.to_csv("final_schedule.csv")

print(data)

"""

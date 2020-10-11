import pandas as pd

schedule = pd.read_csv("Holiday Schedule Ranking 2019.csv", index_col = 0)

print(schedule)

schedule["col_sum"] = schedule.apply(lambda x:x.sum(), axis = 1)

schedule = schedule.sort_values(by = "col_sum", ascending = False)

schedule = schedule.T
    
print(schedule)

for date in schedule.columns:
    date_series = schedule[date].nsmallest(5, keep = "all")
    slot_count = 0
    print(date)
    print(date_series)

schedule.replace(0, "", inplace = True)
schedule.to_csv("final_schedule.csv")
print("done")

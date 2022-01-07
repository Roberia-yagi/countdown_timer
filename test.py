import datetime

time_now = datetime.datetime.now()
time_goal = datetime.datetime(year=2022, month=12, day=31, hour=23, minute=59)
print(time_now)
print(time_goal)
td = time_goal - time_now
print(td.total_seconds())

# date and time function

import datetime as dt

date = dt.date(2025, 1, 21)
date_today = dt.date.today()
time = dt.time(10, 10,10)
time_today = dt.datetime.now()

time_today = time_today.strftime("%H:%M:%S %Y-%m-%d")


target_datetime = dt.datetime(2024, 1, 3, 11, 11, 1)
current = dt.datetime.now()

if target_datetime < current:
    print("Target date time has been passed already!")
else:
    print("Target date time has not been passed!")

# print(date)
# print(date_today)
# print(time)
# print(time_today)
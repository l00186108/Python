'''
Script: mytime.py
By: NMC
Purpose: Getting the current time, date and year. 
Date: 26NOV23
'''
from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)
# print out the year, month, day, hour, minute, second

current_time = today.strftime("%Y-%m-%d %H:%M:%S")  # Year-month-day hours:minutes:seconds

print("Current Time and Date:", current_time)
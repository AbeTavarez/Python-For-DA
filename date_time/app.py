import datetime
from datetime import time 

# print(dir(datetime))

# Create a date object
curr_date = datetime.date(2024, 2, 29)
print(curr_date)

# =========== Due Date in the future ==================
due_date = datetime.date(2026, 3, 7)
due_time = time(11, 59)

formatted_due_date = due_date.strftime("%b %d")
print('DUE DATE: ', f"{formatted_due_date} at {due_time} pm")


print('DAY: ', curr_date.day)
print('MONTH: ', curr_date.month)
print('YEAR: ', curr_date.year)

print(curr_date.weekday())

print("TODAY: ", datetime.date.today())

today = datetime.date.today()
print(f"Today is {today.month}/{today.day}/{today.year}")


print(datetime.datetime(2026, 3, 5))
print(datetime.datetime.today())
print(datetime.datetime.now())
print(type(datetime.datetime.now())) #type


# ============ Time ==============
# t = time(7, 10, 34)

t = time(hour=7, minute=10, second=34, microsecond=40004)

print(t)



print('# ================================')
from datetime import datetime

dt = datetime.now() # create datetime object

print("Datetime is:", dt)

# Get date, time, and timestamp
print('Date:', dt.date()) 
print('Time:', dt.time())
print('Timestamp:', dt.timestamp())

# Get Attributes
print('Year:', dt.year)
print('Month:', dt.month)
print('Day:', dt.day)
print('Hours:', dt.hour)
print('Minutes:', dt.minute)
print('Seconds:', dt.second)
print('Microseconds:', dt.microsecond)

print('# ============= String Format Date ===================')

# Get current Date and time
current_Date = datetime.now()
print('Current Date:', current_Date)

# convert to string and print in different formats
# Represent Dates in numerical format
print("dd-mm-yy HH:MM:SS:", current_Date.strftime("%d-%m-%y %H:%M:%S"))
print("dd-mm-yyyy:", current_Date.strftime("%d-%m-%Y"))
print("dd-mm-yy Format:", current_Date.strftime("%d-%m-%y"))

year = current_Date.strftime("%Y")
print("year:", year)
month = current_Date.strftime("%m")
print("month:", month)
day = current_Date.strftime("%d")
print("day:", day)
time = current_Date.strftime("%H:%M:%S")
print("time:", time)
date_time = current_Date.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
type(date_time)

print('# ============= String Format Name Day and Month ===================')
# Get current Date
x_date = datetime.now()

print('Current Date:', x_date)

# Represent Dates in full textual format
print("dd-MonthName-yyyy:", x_date.strftime("%d-%B-%Y"))
print("DayName-dd-MonthName-yyyy:", x_date.strftime("%A,%d %B, %Y"))

# Represent dates in short textual format
print("dd-MonthName-yyyy:", x_date.strftime("%d-%b-%Y"))
print("DDD-dd-MMM-yyyy:", x_date.strftime("%a,%d %b, %Y"))



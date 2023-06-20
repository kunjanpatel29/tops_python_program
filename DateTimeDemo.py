# get the Current date and time
import datetime

now = datetime.datetime.now()

print(now)

# Get Current Date
import datetime
c_date = datetime.date.today()
print(c_date)


# Python datetime.date Class
import datetime
c_date = datetime.date(2023,6,20)
print(c_date)

# Print today's year, month and day
from datetime import date

today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Print hour, minute, second and microsecond
from datetime import time

a = time(11,18,34)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)

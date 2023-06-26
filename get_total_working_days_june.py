from datetime import date, timedelta
d1 = date(2023, 6, 1) 
d2 = date(2023, 6, 30)
d = d2-d1
days = 0
for i in range(d.days+1):
    day = d1 + timedelta(days=i)
    if(day.weekday()<5):
        days = days + 1
print(days)    


"""
# Python3 code to demonstrate working of
from datetime import datetime, timedelta

test_date1, test_date2 = datetime(2023,6,1), datetime(2023, 6, 30)

# printing dates
print("The original range : " + str(test_date1) + " " + str(test_date2))

# generating dates
dates = (test_date1 + timedelta(idx + 1)
		for idx in range((test_date2 - test_date1).days))

# summing all weekdays
res = sum(1 for day in dates if day.weekday() < 5)

# printing
print("Total business days in range : " + str(res))
"""

"""
import numpy as np
a = np.busday_count('2023-06-01', '2023-06-30')
print(a)
"""

# Using busday_count method
import numpy as np
from datetime import date
d1 = date(2023, 6, 1) 
d2 = date(2023, 6, 30)
days = np.busday_count(d1,d2)
print(days)    
 
# Using Weekdays Method
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
 

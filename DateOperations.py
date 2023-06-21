# Get Today Date and Time
from datetime import datetime

now = datetime.now()

print(now)

# First Format
date = now.strftime("%d/%m/%y")
print(date)

# Second Format
date = now.strftime("%m/%d/%y")
print(date)

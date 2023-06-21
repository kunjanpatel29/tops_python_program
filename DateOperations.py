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

# Third Format
date = now.strftime("%b-%d-%y")
print(date)

# Fourth Format
date = now.strftime("%b-%d-%Y")
print(date)

# Fifth Format
date = now.strftime("%B %d,%Y")
print(date)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

# Format with hour,minute and seconds
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1:", s1)




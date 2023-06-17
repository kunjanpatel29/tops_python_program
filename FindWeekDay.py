# Find the day of the week of a given date

from datetime import datetime

given_date = datetime(2023,6,17)

# to get weekday as integer
print(given_date.today().weekday())

# To get the english name of the weekday
print(given_date.strftime('%A'))

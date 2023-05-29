""" Python Datetime module comes built into Python, so there is no need to install it
externally. It can work with the date as well as time. """

# Import Datetime Module
from datetime import date

today = date.today()

# Get Today’s Year, Month, and Date
print("Current Year : ",today.year)
print("Current Month : ",today.month)
print("Current Day : ",today.day)


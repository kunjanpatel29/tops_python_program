# Calculate Number of Days Between Two dates.

from datetime import date

start_date = date(2023, 6, 1)
end_date = date(2023, 6, 15)

delta = end_date - start_date

print("Number of Days is : ",delta.days)


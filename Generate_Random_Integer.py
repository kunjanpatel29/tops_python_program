# Write Python Program to generate random integer.

import random
import datetime

print("Generate a random integer between 0 and 6:")
print(random.randrange(5))

print("Generate random integer between 5 and 10, excluding 10:")
print(random.randrange(start=5, stop=10))

print("Generate random integer between 0 and 10, with a step of 3:")
print(random.randrange(start=0, stop=10, step=3))

print("\nRandom date between two dates:")
start_dt = datetime.date(2023, 5, 1)
end_dt = datetime.date(2023, 6, 1)
time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days



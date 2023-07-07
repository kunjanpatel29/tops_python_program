"""
Write a Python Program for Remove duplicates from a list and create a tuple and find the minimum and maximum number.
"""

my_list = [87, 52, 44, 53, 54, 87, 52, 53]
print("Original list", my_list)

my_list = list(set(my_list))
print("unique list", my_list)

t = tuple(my_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))

"""
Write a Python program to calculate the difference between the two lists.
"""

lst = [1,2,3,4,5,6,8]
lst1 = [1,4,5,6,8,9]

d1 = list(set(lst) - set(lst1))
d2 = list(set(lst1) - set(lst))

result = d1 + d2
print(result)

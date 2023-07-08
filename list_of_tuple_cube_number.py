"""
Write a Python program to create a list of tuples from given list having number and its cube in each tuple
"""

lst = [2,3,4,6,8,9]

result = [(value, pow(value,3)) for value in lst]

print(result)

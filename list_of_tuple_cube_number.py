"""
Write a Python program to create a list of tuples from given list having number and its cube in each tuple
"""

lst = [2,3,4,6,8,9]

# Using Pow Function
result = [(value, pow(value,3)) for value in lst]

# Using ** Operator
result1 = [(value, value ** 3) for value in lst]

print(result)
print(result1)

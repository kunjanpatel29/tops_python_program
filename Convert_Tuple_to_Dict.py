"""
Write a Python Program to Convert Tuple to a Dictionary.
"""

my_tuple = ((1,"K"),(2,"U"),(3,"N"),(4,"J"))
print(my_tuple)

result = dict((i,j) for i,j in my_tuple)
print(result)

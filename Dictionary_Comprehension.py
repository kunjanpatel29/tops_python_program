"""
Dictionary Comprehension : we have two lists named keys and value and we are iterating
over them with the help of zip() function.
"""

#Example
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

my_dict = {k:v for (k,v) in zip(keys,values)}
print(my_dict)

"""
Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""

lst = [1,2,3,4,2,2,2,1,5]
lst1 = []

def distinct_list(lst):
    for i in lst:
        if i not in lst1:
                lst1.append(i)
    return lst1

result = distinct_list(lst)
print(result)

# Using Set
lst = [1,2,3,4,2,2,2,1,5]
lst1 = list(set(lst))
print(lst1)

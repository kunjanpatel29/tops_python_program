"""
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = []

def even_num_from_list(lst):
    for i in lst:
        if i % 2 == 0:
            lst1.append(i)
    return lst1

result = even_num_from_list(lst)
print(result)

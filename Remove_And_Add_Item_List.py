"""
Write a Python Program For Remove and add item in a list
"""

my_list = [34, 54, 67, 89, 11, 43, 94]
print("Original list ", my_list)

my_list.pop(4)
print("List After removing element at index 4 ", my_list)

my_list.insert(2, 15)
print("List after Adding element at index 2 ", my_list)

my_list.append(29)
print("List after Adding element at last ", my_list)

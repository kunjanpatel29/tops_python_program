"""
Write a Python program to remove duplicates from a list.
"""

# Using For Loop
lst = [1,2,3,4,2,2,3,4,5,6,1,2]
lst1 = []

for i in lst:
    if i not in lst1:
        lst1.append(i)

print(lst)
print(lst1)

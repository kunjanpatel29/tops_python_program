"""
Write a Python program to print even length words in a string
"""

mystr = "My Name is Kunjan Patel"

s = mystr.split()

for i in s:
    if len(i) % 2 == 0:
        print(i)

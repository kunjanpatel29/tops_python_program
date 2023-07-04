"""
Write a Python Program check if string is a valid identifier or not.
"""

import re

mystr = input("Enter a String : ")
regex = '^[A-Za-z_][A-Za-z0-9_]*'

if re.search(regex,mystr):
    print("Valid Identifier")
else:
    print("Invalid Identifier")

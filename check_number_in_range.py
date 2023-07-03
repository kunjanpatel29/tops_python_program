"""
Write a Python function to check whether a number falls within a given range.
"""

def check_num_given_range(num):

    if num in range(2,9):
        print("Num is in given range")

    else:
        print("Num is not in given range")

check_num_given_range(5)

"""
Write a Python Function to revese a string.
"""

string = input("Enter a String : ")

def reverse_string(string):
    string = string[::-1]
    return string

string = reverse_string(string)
print(string)


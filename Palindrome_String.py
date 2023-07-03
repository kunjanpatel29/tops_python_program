"""
Write a Python function that checks whether a passed string is a palindrome or not.
"""

string = input("Enter a String : ")

def palindrome_string(string):
    return string == string[::-1]

result = palindrome_string(string)
if result:
        print("String is Palindrome")
else:
        print("String is not a Palindrome")

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

# Taken Input from the user
s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

print("Before Swap First Two Character of each string :",s1," ",s2)

# For Swap the First two character of a each string 
a1 = s2[:2] + s1[2:]
b1 = s1[:2] + s2[2:]

print("After Swap First Two Character of each string :",a1," ",b1)

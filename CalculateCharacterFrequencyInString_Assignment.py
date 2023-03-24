# Write a Python program to count the number of characters (character frequency) in string.

# Taken Input from the user
mystr = input("Enter a String: ").lower()
d = {}  # Create Dictionary

# Loop for count the number of character frequency in string
for i in mystr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print("The Number of Character Frquency in string is : ",d)

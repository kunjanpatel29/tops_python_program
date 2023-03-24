# Write a Python program to count occurrences of a substring in a string.

# Taken Input from the user
mystr = input("Enter a String: ")
substring = input("Enter a SubString: ")

# Count function for Counting the occurrences of substring in string 
count = mystr.count(substring)  # Substring
#count = mystr.count(substring,2,18) # Substring,start,end

print("Number of Occurrences of substring in stirng is: ",count)

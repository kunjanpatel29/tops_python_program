# Write a Python program to count the occurrences of each word in a given sentence.

# Taken Input from the user
mystr = input("Enter a String: ")
count = dict() # Create Dictionary

words = mystr.split(" ") # Use inbuilt function for split the string in words

# Use loop for count the occurrences of each word in string
for word in words:
    if word in count:
        count[word] += 1
    else:   
        count[word] = 1

print("Occurrence of Each Word Count in string is:",count)
    

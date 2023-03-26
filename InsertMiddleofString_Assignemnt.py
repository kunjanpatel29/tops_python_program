# Write a Python function to insert a string in the middle of a string.

# Function For Insert a string in the middle of a string.
def InsertStringMiddleof(mystr,word):
    return mystr[:2] + word + mystr[2:]

print(InsertStringMiddleof('Itis',"Python"))

#Write a Python function that takes a list of words and returns the length of the longest one.

# Define list
lst = ["Python","Java","PHP","Android","C++"]

# Function for return length of longest one from the words
def count_word_length(lst):
    counter = 0
    for item in lst:
        if len(item) >= counter:
            counter = len(item)
    return counter

print("Longest Word Length is: ",count_word_length(lst))

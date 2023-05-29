# Map Function 

def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# Define a function that doubles even numbers and leaves odd numbers
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
 
# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6]
 
# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))
 
# Display the result
print(result)  

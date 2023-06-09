# List Comprehension
#Example 1
lst = [1,5,15,18,25,22,14,45,92]

result = [x for x in lst if x % 2 == 0]

print(result)

# Example 2
result = [x**3 for x in range(10)]

print(result)

# Dictionary Comprehension
# Example 1
lst = [1,2,5,9,8,6,4,3]

result = {x:x ** 3 for x in lst if x % 2 != 0}

print(result)

# Example 2
name = {"Kunjan","Sanjay","Umang","Jay"}
age = {23,25,24,22}

d = {key:value for key,value in zip(name,age)}

print(d)

# Set Comprehension
# Example 1
s = [1,5,15,18,25,22,14,45,92]

result = {x for x in s if x % 2 == 0}

print(result)

# Example 2
result = {x**3 for x in range(10)}

print(result)

# List Comprehension
#Example 1
lst = [1,5,15,18,25,22,14,45,92]

result = [x for x in lst if x % 2 == 0]

print(result)

# Example 2
lst = [1,5,15,18,25,22,14,45,92]

result = [x**3 for x in range(10)]

print(result)

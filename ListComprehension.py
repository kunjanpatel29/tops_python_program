# List Comprehension

# Iteration with List comprehension
List = [character for character in [1, 2, 3]]
print(List)

List = [character for character in range(1,30)]
print(List)

# Even list using list comprehension
my_list = [i for i in range(1,101) if i % 2 == 0]
print(my_list)

#Matrix using List comprehension
matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)

List = [character for character in 'KunjanPatel']
print(List)

#Print a Table of 10
numbers = [i*10 for i in range(1, 6)]
print(numbers)

#Using lambda to print table of 10
numbers = list(map(lambda i : i*10,[i for i in range(1,9)]))
print(numbers)


# Python List Comprehension using If-else.
lis = ["Even number" if i % 2 == 0
       else "Odd number" for i in range(8)]
print(lis)

# Nested IF with List Comprehension
lis = [num for num in range(100)
	if num % 5 == 0 if num % 10 == 0]
print(lis)


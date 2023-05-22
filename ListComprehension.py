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


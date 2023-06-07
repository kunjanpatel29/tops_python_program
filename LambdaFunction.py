''' Lambda Function : Functions are anonymous function means that the function is without
a name. As we already know that the def keyword is used to define a normal function in Python.
Similarly, the lambda keyword is used to define an anonymous function in Python. '''

my_str = "kunjan patel"
rev_upper = lambda string : string.upper()[::-1]
print(rev_upper(my_str))


# Addition
x = lambda a,b : a + b 
print(x(5,14))

x = lambda a, b, c : a + b + c
print(x(10, 6, 2))

# Substraction
x = lambda a,b : a - b
print(x(10,5))

# Multiplication
x = lambda a,b : a * b
print(x(9,8))

# Lambda Function with List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

for item in is_even_list:
    print(item())

# Lambda Fuction with if-else
Max = lambda a,b : a if a > b else b
print(Max(1,2))

# Using Filter and Lambda Function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list  = list(filter(lambda x : (x % 2 != 0),li))
print(final_list)

# Using Filter and Lambda Function
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)

# Using Map and Lambda Function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2,li))
print(final_list)

# Using Map and Lambda Function
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: animal.upper(), animals))
print(uppered_animals)

# Return Cube of a Number
lambda_cube = lambda y: y*y*y
print("The Value of Cube is : ", lambda_cube(5))

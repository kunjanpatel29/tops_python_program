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

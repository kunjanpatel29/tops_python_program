''' Lambda Function : The Functions are anonymous function means that the function is without
a name. As we already know that the def keyword is used to define a normal function in Python.
Similarly, the lambda keyword is used to define an anonymous function in Python. '''

my_str = "kunjan patel"
rev_upper = lambda string : string.upper()[::-1]
print(rev_upper(my_str))


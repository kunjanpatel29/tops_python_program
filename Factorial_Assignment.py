# Using if-else
print("Using If Else")
n = int(input("Enter a Number: "))
fact = 1

if n < 0:
    print("Factorial of Negative value is Not Possible")
elif n == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact = fact * i
    print("The Factorial of ",n,"is ",fact)

# Using Recursion
print("Using Recursion")
def fact(x):
    if x == 1:
        return 1
    else:
        return (x*fact(x-1))

n = int(input("Enter a Number: "))
result = fact(n)
print("The factorial of",n,"is",result)

# Using Math Module
print("Using Math Module")
n = int(input("Enter a Number: "))

import math
print("The Factorial of Number is: ",math.factorial(n))

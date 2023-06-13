"""
Operator Precedence:Operator precedence in Python simply refers to the order of operations.
Operators are used to perform operations on variables and values.

P - Parentheses
E - Exponentiation
M - Multiplication
D - Division
A - Addition
S - Substraction
"""

print(4 + 3)

print(3 + 3 / 3)

print((3 + 5)/2)

print( ((((13+5)*2)-4)/2)-13 )
#13+5 gives us 18
#18*2 gives us 36
#36-4 gives us 32
#32/2 gives us 16.0
#16-13 gives us 3.0

print(10 % 5 / 3 - 5)
print(10 % 2 // 3 - 5)
print(8 / 2 + 4 - 1)

print(9 and True)
print(10 or True)

print(20 and 30)
print(20 or 30)

print(True and False or True)
print(True or False and True)

print(0 or "Python" and 1)
print(1 and "Python" or 5)
print(5 or 6 and 9)

print(3 * 5 // 4)
print(3 * (5//4))
print(10-5)/5

print((3**2)**2)
print(2**3**2)
print(45 % 10 / 2)

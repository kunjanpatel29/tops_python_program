"""
Write a Python Program For a Modulo of tuple elements
"""

tup1 = (15,25,32,45)
tup2 = (8,4,34,29)

print(tup1)
print(tup2)

result = tuple(val1 % val2 for val1,val2 in zip(tup1,tup2))
print("The Modulus Tuple is : ",result)

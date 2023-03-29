"""
Exception : It is an abnormal condition that occurs during the Runtime of a program.

Exception Handling Keyword : Try, Except & Finally
try : The try keyword is used to specify a block where we should place an exception code.
except : The except block is used to handle the exception if try block raises an error.
finally : The finally block will Always be Executed if the try block raises an error or not.
"""

print("Start Code")

try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))

    c=a/b

    print("Division : ",c)
    l=[1,2,3,4,5]
    index = int(input("Enter a Index Number : "))
    print(l[index])

except Exception as e:   # The Parent Class of All Exception Classes
    print("Exception Caught : ",e)

finally:
    print("I am Finally Block Always Be Executed")

# Inbuilt Exception Classes or Types of Exceptions
""" except ZeroDivisionError as e:
    print("Exception Caught : ",e)
except ValueError as e:
    print("Exception Caught : ",e)
except IndexError as e:
    print("Exception Caught : ",e) """

print("End Code")


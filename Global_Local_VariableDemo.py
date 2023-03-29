"""
Global Variable : Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

Local Variable : Local variables in Python are those which are initialized inside a function and belong only to that particular function.
"""

# For Global Variable
global x  # Declare Global Keyword with Variable
x=10

def test1():
    global y
    y=20   
    print("X : ",x," Y : ",y)
    y=y+20
def test2():
    print("X : ",x," Y : ",y)

# Call Function
test1()
test2()

# For Local Variable
def test1():

    a = 10  # Local Variable
    print("A : ",a)

# Call Function
test1()
#print(a)      #Raise Error Because local variable can not be accessed outside a function.

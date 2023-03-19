"""
Function is a Set of Instructions.
It is a Block of code which only runs when it is called.
"""

# Function with no argument and no return value.

def printLine():
    print("*"*50)

printLine()
print("Welcome To User Defined Function In Python")
printLine()

# Function with argument and no return value.

def add(a,b):
    print("Addition is : ",a+b)

printLine()
x = int(input("Enter Value: "))   # Take Input from the user
y = int(input("Enter Value: "))
add(x,y)
#add(20,30)         # Pass Direct Value
printLine()

# Function with argument and return value.

def sub(a,b):
    return a - b

printLine()
x = int(input("Enter Value: "))  # Take Input from the user
y = int(input("Enter Value: "))
ans = sub(x,y)                        # Store value in variable which is used anywhere
print("Substraction is : ",ans)       
#print("Substraction is : ",sub(x,y)) # Direct Store value in print statement which is not used anywhere
printLine()

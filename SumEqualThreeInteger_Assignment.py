# Taken Input from the user
n1 = int(input("Enter Value of n1: "))
n2 = int(input("Enter Value of n2: "))
n3 = int(input("Enter Value of n3: "))

# Checking for if two values are equal sum will be zero
if n1==n2 or n2==n3 or n3==n1:
    print("Sum is : ", 0)
else:
    print("Sum of Three Number is : ",n1+n2+n3)  # Print Sum of Three Integer


""" # Using Function
def SumofThreeInteger(a,b,c):
    if a == b or b == c or c == a:
        print("Sum is : ",0)
    else:
        print("Sum of Three Number is: ",a+b+c)

n1 = int(input("Enter Value of n1: "))
n2 = int(input("Enter Value of n2: "))
n3 = int(input("Enter Value of n3: "))

SumofThreeInteger(n1,n2,n3) """

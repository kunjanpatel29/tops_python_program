# Swap Two Number Using Temp variable
print("**Swap two Number Using Temp variable**")
# Take input from The User
n1 = int(input("Enter value of n1: "))
n2 = int(input("Enter value of n2: "))

print ("Before swapping: ")
print("Value of n1 : ", n1, " and n2 : ", n2)

# Make Temp variable and swap the value
temp = n1
n1 = n2
n2 = temp

print ("After swapping: ")
print("Value of n1 : ", n1, " and n2 : ", n2)


# Swap Two Number Without Using Temp variable
print("\n**Swap two Number Without Using Temp variable**")
# Take input from The User
n1 = int(input("Enter value of n1: "))
n2 = int(input("Enter value of n2: "))

print ("Before swapping: ")
print("Value of n1 : ", n1, " and n2 : ", n2)

n1,n2 = n2,n1
print ("After swapping: ")
print("Value of n1 : ", n1, " and n2 : ", n2)

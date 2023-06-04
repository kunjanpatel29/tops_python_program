# Simple pyramid pattern
n = int(input("Enter Number of Rows : "))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()

# Printing Downward half Pyramid
n = int(input("Enter Number of Rows : "))
for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print("* ",end="")
    print()


# Number Pattern
n = int(input("Enter Number of Rows : "))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()

# Half pyramid pattern with the number
n = int(input("Enter Number of Rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

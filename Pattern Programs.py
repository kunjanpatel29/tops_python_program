# Simple pyramid pattern
n = int(input("Enter Number of Rows : "))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()


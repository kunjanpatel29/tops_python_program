# Right Pascal Triangle
n = int(input("Enter Number of Rows : "))

# upper triangle
for i in range(n):
    for j in range(i + 1):
        print('*', end="")
    print()
    
# lower triangle
for i in range(n):
    for j in range(n - i - 1):
        print('*', end="")
    print()

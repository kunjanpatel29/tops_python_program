# Inverted Half Pyramid Using Number
n = int(input("Enter Number of Rows : "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Inverted Full Pyramid Pattern

num = int(input("Enter Number of Rows : "))
for i in range(1,num+1):
    for j in range(i-1):
        print(" ",end='')
    for j in range(2*(num-i)+1):
        print("*",end='')
    print()

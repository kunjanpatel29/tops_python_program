# Reverse Number Pattern
num = int(input("Enter Number of Rows : "))
for i in range(num,0,-1):
    num = i
    for j in range(0,i):
        print(num,end=' ')
    print()
        

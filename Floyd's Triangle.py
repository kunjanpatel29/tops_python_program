# Floyd's Triangle

num = int(input("Enter Number of Rows : "))
value = 1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(value, end=" ")
        value += 1
    print()
        

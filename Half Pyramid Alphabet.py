# Half pyramid using alphabets
n = int(input("Enter Number of Rows : "))
value = 65
for i in range(n):
    for j in range(i+1):
        char = chr(value)
        print(char,end=' ')
    value += 1
    print()

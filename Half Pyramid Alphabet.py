# Half pyramid using alphabets

n = int(input("Enter Number of Rows : "))
number = 65
for i in range(n):
    for j in range(i+1):
        character = chr(number)
        print(character,end=' ')
    number += 1
    print()

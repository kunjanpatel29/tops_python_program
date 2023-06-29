lst = []
n = int(input("Enter a How many time you want to enter string : "))

for i in range(n):
    string = input("Enter a String : ")

    if string[0].islower() and string.isalpha() and string[0] not in 'aeiouAEIOU':
        lst.append(string)

print(lst)

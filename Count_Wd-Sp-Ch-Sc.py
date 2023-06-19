# Count Word,Special Character,Character & Space Program

my_str = input("Enter a String : ")

wd = 1
ch = 0
sp = 0
dt = 0
sc = 0

for i in my_str:
    if i.isalpha():
        ch = ch + 1
    elif i.isspace():
        sp = sp + 1
        wd = wd + 1
    elif i.isnumeric():
        dt = dt + 1
    else:
        sc = sc + 1

print("Total Words is : ",wd)
print("Total Character is : ",ch)
print("Total Space is : ",sp)
print("Total Digit: ",dt)
print("Total Special Character is : ",sc)

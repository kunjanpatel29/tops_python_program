#Calculate the sum of all numbers from 1 to a given number

s = 0
num = int(input("Enter Number : "))

for i in range(1, num + 1):
    s += i   # add number to sum variable
    
print("Sum is: ", s)

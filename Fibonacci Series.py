# Take Input From the user
n = int(input("Enter a Number:"))
a,b = 0,1
print("Fibonacci series:",a,end=" ")

while b<n:
    print(b,end=" ")
    a,b = b,a+b

print()


"""n = int(input("Enter a Number: "))
a,b = 0,1
print("Fibonacci series:",a,b, end=" ")
for i in range(2,n):
    c = a + b
    a = b
    b = c
    print(c,end=" ")
print()"""

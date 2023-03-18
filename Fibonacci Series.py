# Take Input From the user
n = int(input("Enter a Range:"))
a,b = 0,1

if n == 0:
    print(n)
elif n < 0:
    print("Invalid Input")
else:
    print("Fibonacci series:",a,end=" ")
    
while b<n:
    print(b,end=" ")
    a,b = b,a+b


"""# Take Input From the user
n = int(input("\nHow many terms You want to print: "))
a,b = 0,1

if n == 0:
    print(n)
elif n < 0:
    print("Invalid Input")
else:
    print("Fibonacci series:",a,end=" ")

for i in range(2,n):
    c = a + b
    a = b
    b = c
    print(c,end=" ")"""

# Take input From the user
n1 = int(input("Enter a start Value:"))
n2 = int(input("Enter a Last Value:"))

a = 0

# loop for start value to end value
while n1 < n2:
    print(n1)
    a,n1 = n1,a+n1

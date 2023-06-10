# HourGlass Star Pattern
num = int(input("Enter Number of Rows : "))

# downward pyramid
for i in range(num-1):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(num-i)-1):
        print('*', end='')
    print()
    
# upward pyramid
for i in range(num):
    for j in range(num-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()

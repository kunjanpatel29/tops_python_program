for i in range(10):     # Print the Square of Number
    print(i*i,end="")
print("\n")
    
print("Print Star Pattern is: ")
for i in range(1,10):         # Print Star Pattern 
    print(" "*(9-i)," *"*i) 
print("\n")

print("Print Pyramid Star Pattern is: ")
for i in range(0,5):        # Print Pyramid Star Pattern
    for j in range(0,i+1):
        print("*",end=" ")
    print()

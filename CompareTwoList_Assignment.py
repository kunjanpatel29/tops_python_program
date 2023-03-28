# Write a Python Program For Compare Two list.

# Define Empty List
list1 = []
list2 = []

# Taken input from the user
x = int(input("Enter length of list1 : "))
for i in range(x):
    value = int(input("Enter a Number in list1 : "))
    list1.append(value)

y = int(input("Enter length of list2 : "))
for i in range(y):
    value = int(input("Enter a Number in list1 : "))
    list2.append(value)


# Sort the List of Elements
list1.sort()
list2.sort()

# Display List of Elements
print(list1)
print(list2)

# Checking for Comparing Two list of Element are equal or not
if list1 == list2:
    print("Both List of Elements are Equal")
else:
    print("Both List of Elements are not Equal")

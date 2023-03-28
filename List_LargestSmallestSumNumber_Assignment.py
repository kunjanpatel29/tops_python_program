# Write a Python function to get the largest number, smallest num and sum of all from a list. 

# Define list
my_list = []

# Taken Input from the user
x = int(input("Enter length of my_list : "))
for i in range(x):
    value = int(input("Enter a Number in my_list : "))
    my_list.append(value)

print("Largest Number is:",max(my_list)) # Get Largest Number from the list
print("Smallest Number is:",min(my_list)) # Get Smallest Number from the list

# Loop for Get the Sum of all Element from the list
sum = 0    # Initialize sum to 0
for i in my_list:
    sum = sum + i
print("The list of Element sum is: ",sum)

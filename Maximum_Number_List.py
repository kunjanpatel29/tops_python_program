# Write Python program to find the maximum of two numbers

def maxOfTwoNum(num1,num2):
	
	if num1 >= num2:
		return num1
	else:
		return num2
	    
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
print(maxOfTwoNum(num1, num2))


#Using max() function
"""
num1 = 5
num2 = 9

max_num = max(num1,num2)
print(max_num)
"""

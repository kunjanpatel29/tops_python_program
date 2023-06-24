# Python program to swap first and last element of a list

# Swap function
def SwapList(lst):
	size = len(lst)
	
	# Swapping
	temp = lst[0]
	lst[0] = lst[size - 1]
	lst[size - 1] = temp
	
	return lst
	
lst = [12, 35, 9, 56, 24]
print(SwapList(lst))


# Swap function
def SwapList(lst):
	
	lst[0], lst[-1] = lst[-1], lst[0]

	return lst
	
# Driver code
lst = [12, 35, 9, 56, 24]
print(SwapList(lst))

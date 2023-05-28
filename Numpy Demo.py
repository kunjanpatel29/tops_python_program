""" Numpy : NumPy is a Python library used for working with arrays. It also has functions
for working in domain of linear algebra, fourier transform, and matrices. It Stands For Numerical Python. """ 

import numpy as np

# Creating Array object
arr=np.array([[1,2,3],[4,5,6]])

# Printing the array
print(arr)

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

# Get the first array from the array
print("Get the First array : ",arr[0])

# Get the 3rd element on 2nd row
print('3rd element on 2nd row: ', arr[1, 2])


myarr = np.array([1,2,3,4,5,6,7,8])
#Slice elements from index 1 to index 5
print("Slice elements from index 1 to index 5 : ",myarr[1:5])

#Slice elements from index 3 to the end of the array
print("Slice elements from index 3 to the end of the array : ",myarr[3:])

#Slice elements from the beginning to index 4(Not Included)
print("Slice elements from the beginning to index 4 : ",myarr[:4])

# Negative Slicing
print("Slice from the index 4 from the end to index 1 : ",myarr[-4:-1])

#Use Step
print("Return every other element from index 1 to index 5 : ",myarr[1:5:2])

# Addition
print("Addition Element from Array : ",myarr[2] + myarr[5])

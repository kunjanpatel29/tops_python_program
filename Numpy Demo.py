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

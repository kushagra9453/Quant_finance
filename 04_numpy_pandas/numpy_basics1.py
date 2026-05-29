# 1. Create a 1D array of numbers 1 to 10
# 2. Create a 2D array of shape (3,3) with all zeros
# 3. Create a 2D array of shape (2,4) with all ones
# 4. Create a 3x3 identity matrix
# 5. Create an array of 5 random numbers between 0 and 1

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr) 

arr1=np.zeros((3,3))
print(arr1)

arr2=np.ones((2,4))
print(arr2)

arr3=np.eye(3)
print(arr3)

arr4=np.random.rand(5)
print(arr4)

# Given this array:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Find:
# 1. Shape of arr
# 2. Size (total elements)
# 3. Data type
# 4. Number of dimensions

ar=arr.shape
print(ar)

arr1=np.size(arr)
print(arr1)

arr2=arr.dtype
print(arr2)

arr3=arr.ndim
print(arr3)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Extract:
# 1. First 3 elements
# 2. Last 3 elements
# 3. Elements from index 2 to 6
# 4. Every 2nd element
# 5. Reverse the array
arr1=arr[:3]
print(arr1)

arr2=arr[-3:]
print(arr2)

arr3=arr[2:7]
print(arr3)

arr4=arr[:2]
print(arr4)

arr5=arr[5:]
print(arr5)
import numpy as np 
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 1. Sum of all elements
# 2. Sum along axis 0 (column-wise)
# 3. Sum along axis 1 (row-wise)
 
ar=np.sum(arr)
print(ar)

ar1=np.sum(arr,axis=0)
print(ar1)

ar2=np.sum(arr,axis=-1)
print(ar2)

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# 1. Sort the array
# 2. Get indices that would sort the array 
# 3. Find the smallest element
# 4. Find the largest element
arr=np.sort(arr)
print(arr)

arr1=np.argsort(arr)
print(arr1)

arr2=np.min(arr)
print(arr2)

arr3=np.max(arr)
print(arr3)

# Reshape and concatenate
arr = np.array([1, 2, 3, 4, 5, 6])

# 1. Reshape to (2, 3)
# 2. Reshape to (3, 2)
# 3. Flatten to 1D
# 4. Concatenate arr with i
arr=arr.reshape(2,3)
print(arr)

arr1=arr.reshape(3,2)
print(arr1)

ar2=arr.flatten()
print(ar2)

ar3=np.concatenate([arr,arr])
print(ar3)

arr = np.array([10, 25, 30, 45, 50, 65, 70, 85])

# 1. Find indices where arr > 50
# 2. Get values where arr > 50
# 3. Replace all values > 50 with 100
import numpy as np

arr1 = np.where(arr > 50, 100, arr)

print(arr1)

import numpy as np

arr = np.array([10, 20, 60, 70, 30, 80])

result = arr[arr > 50]

print(result)
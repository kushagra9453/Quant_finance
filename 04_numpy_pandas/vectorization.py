import numpy as np
arr = np.array([1, 2, 3, 4, 5])
# Compute square of each element
ar1=arr*arr
print(ar1)
 # CUBE
ar3= arr**3
print(ar3)

#ading two element wise
arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])
arr2=arr+arr1
print(arr2)

# COMPONENT
arr=np.array([1,2,3,4])
t=np.exp(arr)
print(t)

#clip wise
arr = np.array([1, 3, 6, 2, 8, 4])
result = np.clip(arr, 2, 5)
print(result)

##bollean
arr = np.array([1, 4, 2, 5, 3, 6])
mask = arr > 3
print(mask)


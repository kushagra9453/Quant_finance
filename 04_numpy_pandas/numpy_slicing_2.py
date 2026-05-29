import numpy as np
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

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Extract:
# 1. First row
# 2. Last column
# 3. Element at row 1, column 2
# 4. First two rows
# 5. Last two columns

print(arr[0])        
print(arr[:, -1])      
print(arr[1, 2])       
print(arr[:2] )        
print(arr[:, -2:])     



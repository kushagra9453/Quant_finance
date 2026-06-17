import numpy as np
arr = np.array([1, 2, 3, 4, 5])
# Replace all elements greater than 3 with 99
ar=np.where(arr>3,99,arr)
print(arr)

arr = np.array([10, 15, 20, 25, 30])
# Replace even numbers with 0, odd numbers with 1
at=np.where(arr%2==0,0,1)
print(at)

arr = np.array([-3, -1, 0, 4, 8])
# Replace negative numbers with 0, keep others unchanged
d=np.where(arr <0,1,arr)
print(d)
arr = np.array([5, 12, 18, 25, 30, 42])
# Find indices where arr > 20
u=np.where(arr > 20)
print(u)

arr = np.array([5, 12, 18, 25, 30, 42])
# Replace values between 10 and 20 (inclusive) with -1
i=np.where((arr>10)&(arr<20),-1,arr)
print(i)


arr = np.array([5, 12, 18, 25, 30, 42])
# Replace values less than 10 OR greater than 30 with 0
p=np.where((arr<10) | (arr>30),0,arr)
print(p)

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
# Where a is even, take from b; otherwise take from a
k=np.where(a%2==0,b,a)
print(k)

arr = np.array([1, 5, 10, 15, 20])
# Clip values to be between 5 and 15 (inclusive)
# If value < 5 → 5, if value > 15 → 15, else keep value
result = np.where(arr < 5, 5, np.where(arr > 15, 15, arr))
print(result)

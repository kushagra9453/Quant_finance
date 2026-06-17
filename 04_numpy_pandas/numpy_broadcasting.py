#scalar boradcasting
from numpy import mean
from numpy import newaxis
import numpy as np 
arr=np.ones((2,3))
print(arr*2)
arr.shape

#2d + 1d row
arr1=np.ones((3,4))
arr2=np.ones(4)
print(arr1+arr2)

## NEW AXIS
arr = np.ones((3, 4))
col = np.array([1, 2, 3])[:, np.newaxis]   
result = arr + col
result.shape

#multipledimession
cube = np.ones((2, 3, 4))
mat = np.ones((3, 4))
result = cube + mat
result.shape

###############################################
# 252 trading days, 2 stocks
high = np.random.rand(252, 2) * 100  
low = np.random.rand(252, 2) * 100    

# Task: Compute the daily range (high - low) for both stocks
# Result shape should be (252, 2)
range=high-low
print(range.shape)

prices = np.array([100, 102, 101, 103, 105, 104, 106])

# Task: Compute daily simple returns using broadcasting
# Formula: (price[t] - price[t-1]) / price[t-1]
# Result shape: (6,)
returns = (prices[1:] - prices[:-1]) / prices[:-1]
print(returns)
returns.shape

# 240 months, 500 stocks
monthly_returns = np.random.randn(240, 500)

# Task: Compute z‑score for each stock (center and scale by its own mean and std)
# Output shape: (240, 500)
mean=monthly_returns.mean(axis=0)
std=monthly_returns.std(axis=0)
z=(monthly_returns-mean)/std
print(z)
print(z.shape)

daily_returns = np.random.randn(252, 50)   # 50 stocks
weights = np.random.rand(50)               # portfolio weights (sum = 1, but not required)

# Task: Compute daily portfolio return for each day
# Result shape: (252,)
daily_portfolio=np.sum(daily_returns*weights,axis=1)
print(daily_portfolio)
print(daily_portfolio.shape)

X = np.random.rand(1000, 5)   # 1000 samples, 5 features
# Task: Create a new matrix X_aug with shape (1000,6) where the first column is all 1s
ones=np.ones((1000,1))
X_aug=np.hstack([ones,X])
print(X_aug)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
# Create a (3,3) matrix where element [i,j] = a[i] + b[j] using broadcasting
result = a[:, np.newaxis] + b
print(result)

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
row_mean = data.mean(axis=1)   # shape (3,)
# Subtract row mean from each element of its ro
m=data-row_mean[:,np.newaxis]
print(m)




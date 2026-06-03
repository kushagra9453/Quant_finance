import numpy as np
# Q1: Basic percentile (median)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Compute the 50th percentile (median)
arr1=np.percentile(arr,50)
print(arr1)

#Q2: Multiple percentiles at once
arr = np.arange(1, 101)  # numbers 1 to 100
# Compute 25th, 50th, and 75th percentiles in one call
arr1=np.percentile(arr,[25,50,5])
print(arr1)


# Q3: Lower and upper percentiles (for outlier range)
data = np.random.randn(1000)
# Find the 5th and 95th percentiles
ae=np.percentile(data,[5,95])
print(ae)

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
col_percentile = np.percentile(arr_2d, 50, axis=0)
# Compute 50th percentile for each row (axis=1)
row_percentile = np.percentile(arr_2d, 50, axis=1)
print(col_percentile)  
print(row_percentile)  

## QUANTILES
arr = np.array([10, 20, 30, 40, 50])
# Compute the 0.5 quantile (same as 50th percentile)
arr1=np.quantile(arr,0.5)
print(arr1)

arr = np.arange(1, 11)
# Compute quantiles [0.25, 0.5, 0.75]
e=np.quantile(arr,[.25,.50,.75])
print(e)

#Q8: Value at Risk (VaR) - simplified
daily_returns = np.array([-0.02, -0.01, 0.00, 0.01, 0.02, -0.03, 0.03, -0.015, 0.005, -0.025])
# Compute 95% VaR (5th percentile) as a positive loss amount
p=np.percentile(daily_returns,95)
print(e)

##  NAN 
# Q1: Detect NaNs
arr = np.array([1, 2, np.nan, 4, 5])
# Create a boolean mask where values are NaN
s=np.isnan(arr)
print(s)

## count how many NaNs
arr = np.array([1, np.nan, 3, np.nan, 5])
s=np.count_nonzero(np.isnan(arr))
print(s)

# Mean ignoring NaNs
arr = np.array([1, 2, np.nan, 4, 5])
mean_without_nan = np.nanmean(arr)
print(mean_without_nan)

#Standard deviation ignoring NaNs
arr = np.array([1, 2, np.nan, 4, 5])
s=np.nanstd(arr)
print(s)
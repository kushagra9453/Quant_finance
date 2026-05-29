from numpy.random import randint
from numpy.random import rand
import numpy as np

# Q1: Generate 5 random numbers between 0 and 1
a=np.random.randint(0,5)
print(a)


# Q2: Generate 10 random integers between 10 and 50
b=np.random.randint(10,50,10)
print(b)

# Q3: Generate 3x4 array of random numbers between 0 and 1
c=np.random.rand(3,4)
print(c)

# Q4: Generate 1000 random numbers from normal distribution with mean=0, std=1
# Then calculate mean and std (should be close to 0 and 1)
a1=np.random.normal(0,1,1000)
print(np.mean(a1))
print(np.std(a1))


# Q5: Generate 500 random numbers with mean=100, std=15
# Calculate mean and std of your sample
b1=np.random.normal(10,15,500)
print(np.mean(b1))
print(np.std(b1))


# Q6: Generate 5 random numbers from standard normal (mean=0, std=1) using randn()
c=np.random.randn(5)
print(c)

# Q7: Set seed to 42. Generate 3 random numbers. Run again. Should be same.
t=np.random.seed(42)
print(np.random.rand(3))

# Q9: Generate same 5 random numbers twice using seed
np.random.seed(123)
arr1 = np.random.rand(5)

np.random.seed(123)
arr2 = np.random.rand(5)
print(arr1,arr2)

# Q10: Monte Carlo Simulation for Stock Price
# Start price = 100
# Daily return mean = 0.001 (0.1%)
# Daily return std = 0.02 (2%)
# Simulate 252 trading days (1 year)
# Generate 5 different possible price paths (5 simulations)
# Store each simulation in an array

# Steps:
# 1. Create array of daily returns using np.random.normal()
# 2. Convert returns to price: price[t] = price[t-1] * (1 + return[t])
# 3. Use np.cumprod() for efficiency
np.random.seed(42)
start_price=100
return_mean=0.001
return_std=0.02
num_simulations=5
trading_days=252

daily_returns = np.random.normal(return_mean, return_std, 
                                  (num_simulations, trading_days))
price_paths = start_price * np.cumprod(1 + daily_returns, axis=1)

print("Monte Carlo Simulation Results:")
print(f"Shape: {price_paths.shape}")  # (5, 253)
print(f"Final prices after 1 year: {price_paths[:, -1]}")
# Convert this to lambda: def square(x): return x * x
square=lambda x:x*x
print (square(4))


#MAP FUNCTION
# Double all prices using map
prices = [2400, 1300, 1600, 3800, 520]
prices=list(map (lambda x:x*2,prices))
print(prices)

buy_prices = [2400, 1300, 1600]
current_prices = [2650, 1180, 1720]
quantities = [50, 30, 40]
# Use map to calculate P&L for each stock
# Formula: (current - buy) × quantity
# Expected: [12500, -3600, 4800]
profit_loss=list(map(lambda b,c,q:(c-b)*q, current_prices,buy_prices,quantities))
print(profit_loss)

#FILTERS
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use filter to keep only even numbers
# Expected: [2, 4, 6, 8, 10]
even=list(filter (lambda x:x%2==0,numbers))
print(even)

pnl_values = [12500, -3600, 4800, -1200, 8000]
# Use filter to keep only profitable (positive) P&L
# Expected: [12500, 4800, 8000]
profit=list(filter(lambda x:x>0,pnl_values))
print(profit)
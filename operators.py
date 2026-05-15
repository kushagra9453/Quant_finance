bought_Tata_motors=785
sold_Tata_motors=923
total_share=-200
gross_profiit=0

Total_investment=bought_Tata_motors*total_share
total_profit=sold_Tata_motors*total_share-Total_investment
gross_profit=total_profit-Total_investment
profit_percentage=total_profit/Total_investment*100
print(f"total profit:{total_profit}")

print(f"gross profit :{gross_profit}")
print(profit_percentage)
print(Total_investment)

####comparision operator
current_price = 1520
buy_price = 1200
target_price = 1600
stop_loss = 1100

# 1. Is current price above buy price?
print("Above buy price:", current_price > buy_price)

# 2. Has target been reached?
print("Target reached:", current_price >= target_price)

# 3. Has stop loss been triggered?
print("Stop loss triggered:", current_price <= stop_loss)

# 4. Is current price between buy and target?
print("Between buy and target:", buy_price < current_price < target_price)
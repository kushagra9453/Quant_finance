# Create dictionary for a single stock:
# Keys: "name", "buy_price", "current_price", "quantity"
# Values: "RELIANCE", 2400, 2650, 50
# Print the current_price
# Update current_price to 2700
# Add new key "target_price" with value 3000
# Print the entire dictionary

stock={"name":"relaince",
"buy_price":2400,
"current_price":2650,
"quantity":50}
print(stock["current_price"])
stock["current_price"]=2700
stock["target_price"]=3000
print(stock)

# Given dictionary:
stock = {"name": "INFOSYS", "buy": 1300, "current": 1180, "qty": 30}
# Loop through and print each key and value
# Format: "key: value"
for key,value in stock.items():
    print(f"{key}:{value}")





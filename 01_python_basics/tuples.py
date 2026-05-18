# Create a tuple called 'stock_prices' with these values: 2450, 2480, 2420, 2460, 2500
stock_prices=(2450,2480,2420,2460,2500)
print(stock_prices)
print(type(stock_prices))

# Given tuple: stock_info = ("RELIANCE", 2400, 50, "BUY")
# Unpack into variables: name, buy_price, quantity, action
# Print each variable separately
stock_info=("reliance",2400,50,"buy")
name=stock_info[0]
buy_price=stock_info[1]
quantity=stock_info[2]
action=stock_info[3]
print(f"name:{name}")

print(f"buy_price:{buy_price}")

print(f"quantity:{quantity}")

print(f"action:{action}")

# Create a tuple without using parentheses (just commas)
# Example: stock1, stock2, stock3 = "RELIANCE", "INFOSYS", "HDFC"
# Create 3 stock names this way and print them
s1,s2,s3="relaince","infosys","hdfc"
print(s1,s2,s3)


# Create a list and a tuple with same values [1,2,3] and (1,2,3)
# Add a new element 4 to the list (append)
# Try to add a new element 4 to the tuple (observe error)
# Convert the tuple to a list, add 4, convert back to tuple
lst=[1,2,3]
tpl=(1,2,3)
lst.append(4)
print(lst)
tpl1=list(tpl)
print(tpl1)
tpl=tuple(lst)
print(tpl)

stock = "reliance industries"

# Do these operations:
# 1. Print in UPPERCASE
# 2. Print in Titlecase
# 3. Print total length of name
# 4. Print first 8 characters only
# 5. Replace "industries" with "Ltd"
# 6. Check if "reliance" is in the name
print(stock.upper())
print(stock.title())
print(len(stock))
print(stock[0:8])
print(stock.replace("industries" ,"ltd"))
print(stock=="reliance")

##float rounding
price = 1456.7823
percentage = 12.34567
tax_rate = 0.18

# Calculate:
# 1. Round price to 2 decimal places
# 2. Round percentage to 2 decimal places
# 3. Calculate tax on price, round to 2
# 4. Final price after tax, round to 2
print(round(price,2))
print(round(percentage,2))
print(round(price/tax_rate*100,2))
print(round(price+tax_rate,2))

from operators import profit_percentage
buy_price = 500
current_price = 620

# Calculate profit percentage
# Then classify:
# - profit % > 20 → "Excellent trade"
# - profit % > 10 → "Good trade"
# - profit % > 0  → "Small profit"
# - profit % == 0 → "Breakeven"
# - profit % < 0  → "In loss"

# # Print the profit % and classification
print(f"profit_percentage:{(current_price-buy_price/buy_price*100)}")
if profit_percentage>20:
    print("excellent")
elif profit_percentage>10:
    print("good")
elif profit_percentage>0:
    print("small profit")
elif profit_percentage==0:
    print("breakeven")
else:
    print("loss")
    
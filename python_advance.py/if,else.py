buy_price = 500
current_price = 620

profit_percentage = ((current_price - buy_price) * 100) / buy_price

print(f"profit_percentage: {profit_percentage}")

if profit_percentage > 20:
    print("Excellent trade")

elif profit_percentage > 10:
    print("Good trade")

elif profit_percentage > 0:
    print("Small profit")

elif profit_percentage == 0:
    print("Breakeven")

else:
    print("Loss")
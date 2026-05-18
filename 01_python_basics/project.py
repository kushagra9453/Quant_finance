#ORDER BOOK
order_book = {
    "BUY": [(2400, 10), (2395, 20), (2390, 15)],
    "SELL": [(2405, 5), (2410, 10), (2420, 25)]
}

# Best BUY price (highest)
best_buy = max(order_book["BUY"], key=lambda x: x[0])
print(f"Best BUY: {best_buy[0]} for {best_buy[1]} shares")

# Best SELL price (lowest)
best_sell = min(order_book["SELL"], key=lambda x: x[0])
print(f"Best SELL: {best_sell[0]} for {best_sell[1]} shares")

# Total quantities
total_buy_qty = sum(qty for price, qty in order_book["BUY"])
total_sell_qty = sum(qty for price, qty in order_book["SELL"])
print(f"Total BUY quantity: {total_buy_qty}")
print(f"Total SELL quantity: {total_sell_qty}")

# Spread
spread = best_sell[0] - best_buy[0]
print(f"Spread: {spread}")
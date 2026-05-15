# Professional way - Use data structures
stocks = [
    {"name": "Reliance", "buy_price": 2400, "current_price": 2650, "qty": 50},
    {"name": "Infosys", "buy_price": 1300, "current_price": 1180, "qty": 30},
    {"name": "HDFC Bank", "buy_price": 1600, "current_price": 1720, "qty": 40}
]

total_invested = 0
total_current = 0

print("\n" + "="*50)
print("PORTFOLIO SUMMARY")
print("="*50)

for stock in stocks:
    invested = stock["buy_price"] * stock["qty"]
    current = stock["current_price"] * stock["qty"]
    pnl = current - invested
    pnl_percent = (pnl / invested) * 100
    
    total_invested += invested
    total_current += current
    
    status = "PROFIT " if pnl > 0 else "LOSS " if pnl < 0 else "BREAK EVEN"
    
    print(f"\n{stock['name']}:")
    print(f"  Invested: ₹{invested:,.2f}")
    print(f"  Current:  ₹{current:,.2f}")
    print(f"  P&L:      ₹{pnl:+,.2f} ({pnl_percent:+.2f}%) {status}")

print("\n" + "="*50)
print("TOTAL PORTFOLIO")
print("="*50)
total_pnl = total_current - total_invested
total_return = (total_pnl / total_invested) * 100
print(f"Total Invested:  ₹{total_invested:,.2f}")
print(f"Total Current:   ₹{total_current:,.2f}")
print(f"Total P&L:       ₹{total_pnl:+,.2f}")
print(f"Total Return:    {total_return:+.2f}%")


# Stock prices for 5 days: [2450, 2480, 2420, 2460, 2500]
# Target price: 2470
# Loop through prices, print:
# - "Day 1: Below target" if price < target
# - "Day 2: Target hit!" if price >= target
# Also count how many days hit the target
 
prices=[2450, 2480, 2420, 2460, 2500]
target=2470
count=0
for i in range(len(prices)):
    if prices[i]<=target:
        print("below target")

    else:
        print("target hit")
        count+=1
        

    


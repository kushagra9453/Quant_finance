# save_portfolio.py

import csv

portfolio = {
    "RELIANCE": {"buy": 2400, "current": 2650, "qty": 50},
    "INFOSYS": {"buy": 1300, "current": 1180, "qty": 30},
    "HDFC": {"buy": 1600, "current": 1720, "qty": 40}
}

# Save to CSV
with open('portfolio.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Stock', 'Buy Price', 'Current Price', 'Quantity', 'P&L'])
    
    for stock, data in portfolio.items():
        pnl = (data['current'] - data['buy']) * data['qty']
        writer.writerow([stock, data['buy'], data['current'], data['qty'], pnl])

print("portfolio.csv created!")



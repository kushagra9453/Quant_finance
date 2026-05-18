# portfolio.py

portfolio_data = {
    "RELIANCE": {"buy": 2400, "current": 2650, "qty": 50},
    "INFOSYS": {"buy": 1300, "current": 1180, "qty": 30},
    "HDFC": {"buy": 1600, "current": 1720, "qty": 40}
}

def get_portfolio():
    """Return the portfolio dictionary"""
    return portfolio_data

def total_invested():
    """Calculate total amount invested"""
    total = 0
    for stock, data in portfolio_data.items():
        total += data["buy"] * data["qty"]
    return total

def total_current_value():
    """Calculate total current value"""
    total = 0
    for stock, data in portfolio_data.items():
        total += data["current"] * data["qty"]
    return total

def total_pnl():
    """Calculate total profit/loss"""
    return total_current_value() - total_invested()
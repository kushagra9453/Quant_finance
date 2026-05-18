# quant_utils.py

def calculate_pnl(buy_price, current_price, quantity):
    """Calculate profit or loss for a stock"""
    return (current_price - buy_price) * quantity

def calculate_return(buy_price, current_price):
    """Calculate percentage return"""
    return ((current_price - buy_price) / buy_price) * 100

def is_profitable(buy_price, current_price):
    """Return True if profitable"""
    return current_price > buy_price
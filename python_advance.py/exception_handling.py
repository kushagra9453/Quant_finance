#Write a function that divides two numbers
# Handle ZeroDivisionError gracefully
from typing_extensions import Concatenate
from contextlib import contextmanager
def divide(a,b):
    try:
        divison=a/b
        return divison
    except ZeroDivisionError:
        return "the no not found"
# Create function get_stock_price(data, symbol)
# Handle:
# - KeyError (symbol not found)
# - TypeError (data is not a dictionary)

def get_stock_price(data,symbol):
    try:
        return data[symbol]
    except KeyError:
        return f"the key{symbol} is wrong"
    except TypeError:
        return "invalid syntax"

stocks = {
    "RELIANCE": 2400,
    "TCS": 3800
}

print(get_stock_price(stocks, "RELIANCE"))
print(get_stock_price(stocks, "HDFC"))

# Write function read_portfolio(filename)
# - Try to open and read file
# - Else: print "File read successfully" and return content
# - Finally: print "File operation attempted" (always run)
# - Handle FileNotFoundError

def read_portfolio(filename):
    try:
        file=open(filename,"r")
        content=file.read()
    except FileNotFoundError:
        print(f"file {filename} not found")
        return None
    else:
        print("file read succesfully")
        return content
    finally:
        print ("file operation attempted")
        if "file" in locals():
            file.close()

read_portfolio("existing.txt")  
read_portfolio("missing.txt") 

# Create function validate_trade(price, quantity, balance)
# Raise ValueError if:
# - price <= 0
# - quantity <= 0
# - price * quantity > balance
# Return "Trade valid" if all checks pass
def validate_trade(price,quantity,balance):
    if price<=0:
        raise ValueError
    if quantity<=0:
        raise ValueError
    if price*quantity>balance:
        raise ValueError
    return "trade valid"
try:
    validate_trade(1000,30,20000)
    print("trade valid")
except ValueError as e:
    print("trade invalid")

#CUSTOM HANDLING
#Create custom exception class InsufficientBalanceError
# Create class TradingAccount with:
# - __init__(self, balance)
# - withdraw(self, amount) - raises InsufficientBalanceError if amount > balance
class InsufficientBalanceError(Exception):
    """Raised when account balance is insufficient"""
    pass

class TradingAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"Need {amount}, have {self.balance}")
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

# Test
acc = TradingAccount(10000)
acc.withdraw(5000) 

try:
    acc.withdraw(6000)  # Raises error
except InsufficientBalanceError as e:
    print(f"Error: {e}")
    
# Write function write_portfolio(filename, data)
# Always close the file even if error occurs
# Handle permission errors

def write_portfolio(filename, data):
    file=None
    try:
        file=open(filename,"w")
        file.write(data)
    except PermissionError:
        print("file cant be written")
    except Exception as e:
        print(f"error is{e}")
    finally:
        if "file" in locals():
            file.close()

write_portfolio("portfolio.txt", "RELIANCE,2400,50")

# Create class TradingBot with:
# - buy(symbol, price, quantity) - raises custom exceptions
# - sell(symbol, price, quantity) - raises custom exceptions
# Custom exceptions: InsufficientBalanceError, InvalidTradeError, NoPositionError
class InsufficientBalanceError(Exception):
    pass

class InvalidTradeError(Exception):
    pass

class NoPositionError(Exception):
    pass

class TradingBot:
    def __init__(self, balance):
        self.balance = balance
        self.positions = {}
    
    def buy(self, symbol, price, quantity):
        if price <= 0 or quantity <= 0:
            raise InvalidTradeError(f"Invalid price={price} or quantity={quantity}")
        
        cost = price * quantity
        if cost > self.balance:
            raise InsufficientBalanceError(f"Need {cost}, have {self.balance}")
        
        self.balance -= cost
        self.positions[symbol] = self.positions.get(symbol, 0) + quantity
        print(f"BOUGHT {quantity} {symbol} @ {price}")
    
    def sell(self, symbol, price, quantity):
        if symbol not in self.positions:
            raise NoPositionError(f"No position in {symbol}")
        
        if quantity > self.positions[symbol]:
            raise InvalidTradeError(f"Only have {self.positions[symbol]} shares")
        
        proceeds = price * quantity
        self.balance += proceeds
        self.positions[symbol] -= quantity
        
        if self.positions[symbol] == 0:
            del self.positions[symbol]
        
        print(f"SOLD {quantity} {symbol} @ {price}")

# Test
bot = TradingBot(100000)

try:
    bot.buy("RELIANCE", 2400, 30)  # Works
    bot.buy("RELIANCE", -100, 10)  # Error
except InvalidTradeError as e:
    print(f"Error: {e}")

try:
    bot.buy("RELIANCE", 2400, 100)  # Error
except InsufficientBalanceError as e:
    print(f"Error: {e}")

try:
    bot.sell("INFOSYS", 1300, 10)  # Error
except NoPositionError as e:
    print(f"Error: {e}")
        





    
        
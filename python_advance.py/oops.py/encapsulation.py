# Create class 'Stock' with:
# - Private attribute __price
# - Public attribute symbol
# - Getter method get_price()
# - Setter method set_price() with validation (price > 0)

class Stock:
    def __init__(self,symbol,price):
        self.symbol=symbol
        self.__price=price

    def get_price(self):
        return self.__price
    def set_price(self,price):
        if price>0:
            self.__price=price
        else:
            return None

s = Stock("RELIANCE", 2400)
print(s.symbol)           
print(s.get_price())      
s.set_price(2650)

# Create class 'TradingAccount' with:
# - Private __balance
# - @property balance (getter - returns balance)
# - @balance.setter (setter - only allows positive values)
# - @property is_profitable (read-only - returns True if balance > 0)

# Write your code here:
class Tradingaccount:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance_setter(self,balance_setter):
        if balance_setter>0:
            self.__balance=balance_setter
        else:
            raise Exception
    @property
    def is_profitable(self):
        return self.__balance > 0

# Create class 'SecretStrategy' with:
# - Private __algorithm = "SuperSecretAlpha"
# - Private method __run_backtest()
# - Public method get_algorithm() returns __algorithm
# Then demonstrate:
#   1. How to access private attribute directly (using name mangling)
#   2. Why you should NOT do this

class SecretStrategy:
    def __init__(self):
        self.__algorithm = "SuperSecretAlpha"
        self.__backtest_result = 0.85
    
    def __run_backtest(self):
        return f"Backtest result: {self.__backtest_result}"
    
    def get_algorithm(self):
        return self.__algorithm
    
    def get_backtest(self):
        return self.__run_backtest()

s = SecretStrategy()
print(s.get_backtest())    


print(s._SecretStrategy__algorithm)        
print(s._SecretStrategy__run_backtest())               

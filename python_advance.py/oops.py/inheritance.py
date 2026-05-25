#INHERITANCE (Single)


# Create a parent class 'Animal' with:
# - __init__(self, name)
# - method speak() that prints "Animal speaks"

# Create child class 'Stock' that inherits from Animal
# Add attribute 'price' in __init__
# Override speak() to print "Stock: [name] speaks market"

# Create stock object "RELIANCE" with price 2400
# Call speak()

import statistics

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print ("Animal speaks")


a = Animal("Dog")
print(a.name)
a.speak()


class Stock(Animal):

    def __init__(self,name,price):
        super().__init__(name)
        self.price=price

    def speak(self):
        print(f"Stock: {self.name} speaks market")


s = Stock("reliance",2400)
s.speak()



# Create parent class 'Investment' with:
# - __init__(self, amount, years)
# - method calculate() returns amount * years

# Create child class 'StockInvestment' that:
# - Uses super() to call parent __init__
# - Adds attribute 'return_rate'
# - Override calculate() to return amount * years * return_rate/100

# Test: amount=100000, years=5, return_rate=12


class Investment:

    def __init__(self,amount,years):
        self.amount=amount
        self.years=years

    def calculate(self):
        return self.amount*self.years


class StockInvestment(Investment):

    def __init__(self,amount,years,price,return_rate):
        super().__init__(amount,years)

        self.price=price
        self.return_rate=return_rate

    def calculate(self):
        return self.amount*self.years*self.return_rate/100


d = StockInvestment(100000,5,2400,12)
print(d.calculate())



# Create parent class 'Trade' with:
# - __init__(self, symbol, quantity)
# - method info() prints symbol and quantity

# Create child class 'EquityTrade' that:
# - Inherits from Trade
# - Adds attribute 'exchange' (NSE/BSE)
# - Add method get_exchange() returns exchange

# Test with symbol="RELIANCE", quantity=50, exchange="NSE"


class Trade:

    def __init__(self,symbol,quantity):
        self.symbol=symbol
        self.quantity=quantity

    def info(self):
        print(f"{self.symbol}, {self.quantity}")


class EquityTrade(Trade):

    def __init__(self,symbol,quantity,exchange):
        super().__init__(symbol,quantity)

        self.exchange=exchange

    def get_exchange(self):
        return self.exchange

    def info(self):
        return self.symbol,self.quantity,self.exchange



# Create parent class 'BaseStrategy' with:
# - method signal(price) returns "BUY" if price < 100 else "SELL"

# Create child class 'AdvancedStrategy' that:
# - Inherits from BaseStrategy
# - Override signal() but ALSO call parent's signal
# - Return parent signal + " with confirmation"

# Test with price=2400 and price=50


class BaseStrategy:

    def signal(self,price):
        return "buy" if price < 100 else "sell"


class AdvancedStrategy(BaseStrategy):

    def signal(self,price):

        parent_signal = super().signal(price)

        return parent_signal + " with confirmation"


s = AdvancedStrategy()

print(s.signal(2400))
print(s.signal(50))



#MULTIPLE INHERITANCE

# Class A: method info() prints "Class A"
# Class B: method info() prints "Class B"
# Class C: inherits from A and B (order: A, B)
# Create C object and call info() - which one runs?

# Then change order to (B, A) and see difference


class A:

    def info(self):
        print("Class A")


class B:

    def info(self):
        print("Class B")


class C(A,B):
    pass


c = C()
c.info()


class D(B,A):
    pass


d = D()
d.info()



# Create mixin class 'Buyable' with method buy(qty): prints "Bought {qty}"
# Create mixin class 'Sellable' with method sell(qty): prints "Sold {qty}"
# Create class 'Stock' that inherits from Buyable, Sellable
# Add __init__(self, symbol, price)

# Create Stock("RELIANCE", 2400) and test buy(10), sell(5)


class Buyable:

    def buy(self,qty):
        print(f"Bought {qty}")


class Sellable:

    def sell(self,qty):
        print(f"Sold {qty}")


class Stock(Buyable,Sellable):

    def __init__(self,symbol,price):
        self.symbol=symbol
        self.price=price


s = Stock("Reliance",2400)

s.buy(10)
s.sell(50)



# Create three classes:
# 1. 'PriceCalculator' - method price(data) returns average of data
# 2. 'RiskAnalyzer' - method risk(returns) returns standard deviation
# 3. 'Backtester' - inherits from both PriceCalculator and RiskAnalyzer
#    - Add method run(data) that prints price and risk

# Test with stock prices: [2400, 2420, 2450, 2480, 2500]


class PriceCalculator:

    def price(self,data):
        return sum(data)/len(data)


class RiskAnalyzer:

    def risk(self,returns):
        return statistics.stdev(returns) if len(returns) > 1 else 0


class Backtester(PriceCalculator,RiskAnalyzer):

    def run(self,data):

        avg_price = self.price(data)

        returns = [(data[i] - data[i-1])/data[i-1] for i in range(1, len(data))]

        vol = self.risk(returns)

        print(f"Average Price: {avg_price:.2f}")
        print(f"Volatility: {vol:.4%}")


prices = [2400, 2420, 2450, 2480, 2500]

bt = Backtester()

bt.run(prices)
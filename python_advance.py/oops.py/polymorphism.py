# Create 3 different stock classes: Reliance, Infosys, HDFC
# Each has a method get_current_price() returning different values
# Create a function print_price(stock) that works with any stock

class Relaince:
    def current_price(self,price):
        return price
class infosys:
    def current_price(self,price):
        return price
class hdfc:
    def current_price(self,price):
        return price
    
    def print_price(self,price):
        print(price)
r=Relaince()
i=infosys()
h=hdfc()
print(r.current_price(2400))
print(i.current_price(400))
print(h.current_price(240))

# Create parent class 'Instrument' with method calculate_pnl()
# Create child classes: Stock, Option, Future
# Each overrides calculate_pnl() with their own formula
# Create list of instruments and loop through

# Write your code here:
class insturment:
    def calculate_pnl(self):
        pass
class stock(insturment):
    def __init__(self,buy,current,qty):
        self.buy=buy
        self.current=current
        self.qty=qty
    def calculate_pnl(self):
        return (self.current - self.buy) * self.qty
class option(insturment):
    def __init__(self, entry, current, qty):
        self.entry = entry
        self.current = current
        self.qty = qty
    
    def calculate_pnl(self):
        return (self.current - self.entry) * self.qty

class future:
    def __init__(self, entry, current, qty):
        self.entry = entry
        self.current = current
        self.qty = qty
    
    def calculate_pnl(self):
        return (self.current - self.entry) * self.qty



# Test
instruments = [
    stock(2400, 2650, 50),
    option(50, 80, 10),
    future(22000, 22500, 25)
]

for inst in instruments:
    print(f"P&L: ₹{inst.calculate_pnl():,}")


# Create 3 classes: Nifty, BankNifty, FinNifty
# Each has method get_current_value() returning different values
# Create a function display_value(index) that works with any class

class Nifty:
    def get_current_value(self):
        return 24500

class BankNifty:
    def get_current_value(self):
        return 52000

class FinNifty:
    def get_current_value(self):
        return 22500

def display_value(index):
    print(f"Current Value: {index.get_current_value()}")


display_value(Nifty())    
display_value(BankNifty())   
display_value(FinNifty())    

# Create 3 UNRELATED classes: NewsAnalyzer, TechnicalAnalyzer, SentimentAnalyzer
# Each has method analyze() returning different signals
# Create function get_signal(analyzer) that calls analyze()

class NewsAnalyzer:
    def analyze(self):
        return "BUY: Positive earnings report"

class TechnicalAnalyzer:
    def analyze(self):
        return "SELL: RSI above 70, overbought"

class SentimentAnalyzer:
    def analyze(self):
        return "HOLD: Mixed social media sentiment"

def get_signal(analyzer):
    print(f"Signal: {analyzer.analyze()}")

get_signal(NewsAnalyzer())
get_signal(TechnicalAnalyzer())
get_signal(SentimentAnalyzer())

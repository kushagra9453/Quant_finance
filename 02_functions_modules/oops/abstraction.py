# Create abstract class 'Vehicle' with abstract methods:
# - start_engine()
# - stop_engine()
# Create concrete class 'Car' that implements both methods
from abc import ABC ,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start_engine(Self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(vehicle):
    def start_engine(self):
        print("engine start")
    def stop_engine(self):
        print("stop")
c = Car()
c.start_engine()
c.stop_engine()
# Try to create object of abstract class Vehicle
# What error do you get?
from abc import ABC ,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
v=vehicle()
print(v)

# Create abstract class 'TradingStrategy' with:
# - abstract method generate_signal(price_data)
# - abstract method set_stop_loss(entry_price)
# Create concrete class 'MovingAverageStrategy' implementing both

from abc import ABC, abstractmethod
class Tradingstrategy(ABC):
    @abstractmethod
    def generate_signal(self,price_data):
        pass
    @abstractmethod
    def set_stop_loss(self,entry_price):
        pass

class MovingAverageStrategy(Tradingstrategy):
    def __init__(self,short_window,long_window):
        self.short_window=short_window
        self.long_window=long_window
    def generate_signal(self, price_data):
        if len(price_data) < self.long_window:
            return "HOLD"
        
        short_ma = sum(price_data[-self.short_window:]) / self.short_window
        long_ma = sum(price_data[-self.long_window:]) / self.long_window
        
        if short_ma > long_ma:
            return "BUY"
        elif short_ma < long_ma:
            return "SELL"
        return "HOLD"
    
    def set_stop_loss(self, entry_price):
        return entry_price * 0.95 

# Create abstract class 'Analyzer' with:
# - concrete method calculate_average(data) - returns sum(data)/len(data)
# - abstract method analyze(data)
# Create class 'StockAnalyzer' implementing analyze()
from abc import ABC , abstractmethod
class Analyzer(ABC):
    def calculate_average(self,data):
        return sum(data)/len(data)
    @abstractmethod
    def analyze(self,data):
        pass
class StockAnalyzer(Analyzer):
    def analyze(self,data):
        avg = self.calculate_average(data)
        latest = data[-1]
        if latest > avg:
            return f"BULLISH: Latest {latest} > Average {avg:.2f}"
        elif latest < avg:
            return f"BEARISH: Latest {latest} < Average {avg:.2f}"
        return f"NEUTRAL: Latest {latest} = Average {avg:.2f}"


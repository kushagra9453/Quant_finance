# Input: buy_price, current_price, quantity
# Output: profit/loss amount

def profit_loss(buy_price,current_price,quantity):
    profit=current_price*quantity-buy_price*quantity
    return profit
    loss=buy_price*quantity-current_price*quantity
    return loss

print(profit_loss(2400,2650,50))

# Create a function that returns "PROFIT" or "LOSS"

def profit(buy_price,current_price):
    if current_price>buy_price:
        return "profit"
    else:
        return "loss"

print(profit(2400,2650))
print(profit(1300,1177))

#Function with default parameter
# Create function that calculates percentage return
# Default decimal_places = 2

def percentage_return(buy_price,current_price,decimal_places=2):
    profit=current_price-buy_price
    percentage=profit/buy_price*100
    return round(percentage,decimal_places)

result=percentage_return(2400,2650,2)
print(result)
# Question 4: Multiple parameters and validation
# Add error handling for negative prices

def validation(buy,current,quantity):
    if buy<0 or current<0 or quantity<0:
        return "error"
    else:
        return "valid"
print(validation(2400,2650,-1))

# Question 5: Function calling another function
# Create portfolio summary using your calculate_pnl function

portfolio = {
    "RELIANCE": {"buy": 2400, "current": 2650, "qty": 50},
    "INFOSYS": {"buy": 1300, "current": 1180, "qty": 30},
    "HDFC": {"buy": 1600, "current": 1720, "qty": 40}
}
def portfolio():
    print("portfolio")
    for key,values in portfolio.items():
        print(key,values) 
    def calculate_pnl(buy,current,qty):
        pnl=current*qty-buy*qty
        return pnl
        return profit()


# Celsius To Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Area of a Rectangle
def area(length,breadth):
    return length*breadth
print(area(7,8))

# Distance Covered by a Vehicle
def distance(speed,time):
    return speed*time
print(distance(48,8))
# Number of Rounds of Lift
def rounds(distance,tracklength):
    return distance//tracklength


        


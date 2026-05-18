from package.quant_utils import calculate_return
from package.quant_utils import calculate_pnl
from package.quant_utils import is_profitable
pnl =calculate_pnl(2400, 2650, 50)
print(f"P&L: ₹{pnl}")

return_pct =calculate_return(2400, 2650)
print(f"Return: {return_pct:.2f}%")

profit_status =is_profitable(2400, 2650)
print(f"Profitable: {profit_status}")


import portfolio
print(f"Total Invested: ₹{portfolio.total_invested()}")
print(f"Total Current: ₹{portfolio.total_current_value()}")
print(f"Total P&L: ₹{portfolio.total_pnl()}")

##ADDING BOTHB THE MODULES
from package import quant_utils
import portfolio
print(f"Total Invested: ₹{portfolio.total_invested()}")
print(f"Total Current: ₹{portfolio.total_current_value()}")
print(f"Total P&L: ₹{portfolio.total_pnl()}")
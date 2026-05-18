pe_ratio = 18
debt_to_equity = 0.4
profit_growth = 22
dividend_yield = 2.5

# A stock is GOOD to buy if ALL of these:
# - PE ratio less than 25
# - Debt to equity less than 1
# - Profit growth more than 15%
# - Dividend yield more than 1%

# Print whether stock is good to buy or not
# Also print which conditions passed
pe_check= pe_ratio<25 
debt=debt_to_equity<1
profit=profit_growth>0.15
dividend=dividend_yield>0.1

if pe_check and debt and profit and dividend:
    print("good the stock is good to buy")

# Given list with duplicates: stocks = ["RELIANCE", "INFOSYS", "RELIANCE", "HDFC", "INFOSYS", "TCS"]
# Convert to set to remove duplicates
# Convert back to list
# Print the unique stocks list

stocks = ["RELIANCE", "INFOSYS", "RELIANCE", "HDFC", "INFOSYS", "TCS"]
set1=set(stocks)
print(set1)
lst1=list(set1)
print(lst1)

# Portfolio A: {"RELIANCE", "TCS", "HDFC", "WIPRO"}
# Portfolio B: {"INFOSYS", "HDFC", "TATASTEEL", "RELIANCE"}
# Find stocks in BOTH portfolios (intersection)
# Find ALL unique stocks from both (union)
set1={"RELIANCE", "TCS", "HDFC", "WIPRO"}
set2={"INFOSYS", "HDFC", "TATASTEEL", "RELIANCE"}
print(set1.intersection (set2))
print(set1.union (set2))


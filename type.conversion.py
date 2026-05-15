price_string = "1500"
quantity_string = "50"
rate_string = "12.5"

# Do these:
# 1. Convert price to integer
# 2. Convert quantity to integer
# 3. Convert rate to float
# 4. Calculate total investment using converted values
# 5. Print type of each variable

print(int(price_string))
print(int(quantity_string))
print(float(rate_string))

print(f"total investment:{int(price_string)*int(quantity_string)}")
print(f"type of varialble:{type(price_string)}")
print(f"type of varialble:{type(quantity_string)}")
print(f"type of varialble:{type(rate_string)}")
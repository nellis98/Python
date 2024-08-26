# Define variables for kilogram values
kg_value_1 = 2
kg_value_2 = 6
kg_value_3 = 10
kg_value_4 = 15

# Convesion factor : 1 kg = 2.20462 lbs
conversion_factor = 2.20462

#Calculate pounds for each kilogram value
lb_value_1 = kg_value_1 * 2.20462
lb_value_2 = kg_value_2 * 2.20462
lb_value_3 = kg_value_3 * 2.20462
lb_value_4 = kg_value_4 * 2.20462

#Output the results
print(f"{kg_value_1} kilograms is equal to {lb_value_1} pounds.")
print(f"{kg_value_2} kilograms is equal to {lb_value_2} pounds.")
print(f"{kg_value_3} kilograms is equal to {lb_value_3} pounds.")
print(f"{kg_value_4} kilograms is equal to {lb_value_4} pounds.")

#Output the results rounded to two decimal places
print(f"\n{kg_value_1} kilograms is equal to {lb_value_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lb_value_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lb_value_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lb_value_4:.2f} pounds.")
#This program finds what percent of your budget is spent in different areas
#This section allows the user to input their budget and ecpenses
Total_Budget = float(input("Total Budget: "))
Housing = float(input("Housing Cost: "))
Utilities = float(input("Utilities Cost: "))
Groceries = float(input("Groceries Cost: "))
Transportation = float(input("Transportation Cost: "))
Health_Care = float(input("Health Care Cost: "))
Personal_Care = float(input("Personal Care Cost: "))
Clothing = float(input("Clothing Cost: "))
Debt = float(input("Debt: "))
#This section solves for the percentage each expense takes from the budget
Housing_percent = Housing / Total_Budget * 100
Utilities_percent = Utilities / Total_Budget * 100
Groceries_percent = Groceries / Total_Budget * 100
Transportation_percent = Transportation / Total_Budget * 100
Health_Care_percent = Health_Care / Total_Budget * 100
Personal_Care_percent = Personal_Care / Total_Budget * 100
Clothing_percent = Clothing / Total_Budget * 100
Debt_percent = Debt / Total_Budget * 100
#This section prints the cost of the expense compared to the total budget as well as the percentage of the budget that expense uses.
print(f"\n{Housing} dollars of the total available {Total_Budget} dollars accounts for {Housing_percent} % of the budget")
print(f"{Utilities} dollars of the total available {Total_Budget} dollars accounts for {Utilities_percent} % of the budget")
print(f"{Groceries} dollars of the total available {Total_Budget} dollars accounts for {Groceries_percent} % of the budget")
print(f"{Transportation} dollars of the total available {Total_Budget} dollars accounts for {Transportation_percent} % of the budget")
print(f"{Health_Care} dollars of the total available {Total_Budget} dollars accounts for {Health_Care_percent} % of the budget")
print(f"{Personal_Care} dollars of the total available {Total_Budget} dollars accounts for {Personal_Care_percent} % of the budget")
print(f"{Clothing} dollars of the total available {Total_Budget} dollars accounts for {Clothing_percent} % of the budget")
print(f"{Debt} dollars of the total available {Total_Budget} dollars accounts for {Debt_percent} % of the budget")
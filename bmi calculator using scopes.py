#declare variables
pounds = 0
inches = 0
#make KILOGRAMS and METERS variables global
global KILOGRAMS
global METERS
#declare variables
KILOGRAMS = 0.453592
METERS = 0.0254
#define the function that will solve for bmi and display the results
def bmi_calculator():
    #convert pounds to kilograms
    weight = pounds * KILOGRAMS
    #convert inches to meters
    height = inches * METERS
    #solve for bmi
    bmi = weight / (height * height)
    #display results using if elif else to create 4 distinct catagories
    if bmi < 18.5 and bmi > 0:
        print(f"Your BMI is {bmi:,.2f}: Underweight")
    elif bmi >= 18.5 and bmi < 24.9:
        print(f"Your BMI is {bmi:,.2f}: Normal weight")
    elif bmi >= 25 and bmi < 29.9:
        print(f"Your BMI is {bmi:,.2f}: Overweight")
    elif bmi >= 30:
        print(f"Your BMI is {bmi:,.2f}: Obese")
#create a loop
while pounds <= 0 or inches <= 0:
    #accept input for pounds and inches
    pounds = float(input("Enter your weight in pounds: "))
    inches = float(input("Enter your height in inches: "))
    #display a message that to tell the user to input again if outside of acceptable parameters
    if pounds <= 0 or inches <= 0:
        print("Please reenter your weight and height")
    #else executes the function
    else:
        bmi_calculator()
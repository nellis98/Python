#define the function that calculates the interest
def calculate_interest(principal, rate, time):
    #assign the formula for the interest equal to a variable
    simple_interest = principal * rate * time / 100
    #print the full sentance explaination of the results with a rounded principal and simple interest
    print(f"The simple interest for a principal amount of ${principal:,.2f} \
at an interest rate of {rate}% over a period of \
{time} years is: ${simple_interest:,.2f}")
#accepts user input for the variables
principal = int(input("principal amount: "))
rate = int(input("rate of interest as %: "))
time = int(input("time invested in years: "))
#sets the user input as the variables of the interest equation
calculate_interest(principal, rate, time)
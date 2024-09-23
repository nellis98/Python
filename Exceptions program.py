#create the variable number
number = 0
#define the function that will square the input
def square_number():
    #use try for error testing
    try:
        #accept user input
        number = input("Enter a number to square: ")
        #squares the input
        squared_number = int(number) ** 2
    #when there is a value error the following is executed
    except ValueError:
        #value unacceptable will be desplayed 
        print("Value unacceptable")
        #the user will be prompted again to enter a number to square
        square_number()
    #if the except is not met the else is executed
    else:
        #print the number and its square
        print(f"The square of {number} is {squared_number}.")
#call the function
square_number()
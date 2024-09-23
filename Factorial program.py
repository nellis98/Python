#define the equation for the factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#define the fuction that will run
def main():
    #request user input
    n = int(input("enter a non-negative number: "))
    #execute the factorial function using the user input
    factorial(n)
    #print the results
    print(f"The factorial of {n} is {factorial(n)}")
#execute the function
main()
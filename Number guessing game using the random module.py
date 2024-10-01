#import the module random
import random
#use randrange to create a ramdom number between 1 and 100
random_number = random.randrange(1, 101)
#define the main function
def main():
    #create the variable number
    number = 0
    #use try and except statements to look for errors
    try:
        #create a while loop
        while int(number) != int(random_number):
            #allow for input of an integer
            number = int(input("Enter a number between 1 and 100: "))
            #determine the distance between the two numbers
            distance_from_number = abs(int(random_number) - int(number))
            #display a message stating how close the user is to guessing the correct number
            if distance_from_number > 25:
                print("Cold")
            elif distance_from_number <= 25 and distance_from_number > 15:
                print("Cool")
            elif distance_from_number <= 15 and distance_from_number > 5:
                print("Hot")
            elif distance_from_number <= 5 and distance_from_number != 0:
                print(" Very Hot")
            elif distance_from_number == 0:
                print("You did it!")
    except ValueError:
        #value error will be desplayed 
        print("Value error")
#call the main function
main()
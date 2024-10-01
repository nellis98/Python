import random
random_number = random.randrange(1, 101)
def main():
    number = 0
    try:
        while int(number) != int(random_number):
            number = int(input("Enter a number between 1 and 100: "))
            distance_from_number = abs(int(random_number) - int(number))
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
main()
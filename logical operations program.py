number1 = int(input("Enter an integer:"))
number2 = int(input("Enter another integer:"))
if number1 > 20 and number2 > 20:
    print("Both numbers are greater than 20: ", int(number1) > 20 and int(number2) > 20)
else:
    print("Both numbers are greater than 20: ", int(number1) > 20 and int(number2) > 20)
if number1 < 80 and number2 < 80:
    print("Both numbers are less than 80: ", int(number1) < 80 and int(number2) < 80)
else:
    print("Both numbers are less than 80: ", int(number1) < 80 and int(number2) < 80)
if number1 % 2 == 0 or number2 % 2 == 0:
    print("Either one or both of the numbers is even:", int(number1) % 2 == 0 or int(number2) % 2 == 0)
else:
    print("Either one or both of the numbers is even:", int(number1) % 2 == 0 or int(number2) % 2 == 0)
if number1 % 2 == 1 or number2 % 2 == 1:
    print("Either one or both of the numbers is odd:", int(number1) % 2 == 1 or int(number2) % 2 == 1)
else:
    print("Either one or both of the numbers is odd:", int(number1) % 2 == 1 or int(number2) % 2 == 1)
if not number1 == number2:
    print("Number one is not equal to number two:", number1 != number2)
else:
    print("Number one is not equal to number two:", number1 != number2)
if not number2 == 5:
    print("Number one is not 5:", number2 != 5)
else:
    print("Number one is not 5:", number2 != 5)
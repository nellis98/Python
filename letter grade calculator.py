#accepts input of a numeric value representing a grade
numericgrade = int(input("Enter your numeric grade:"))
#finds values outside of the accepted 0-100
if numericgrade >= 100:
    print("Value outside of grade scale")
elif numericgrade < 0:
    print("Value outside of grade scale")
#displays a letter grade equivalent to the numeric grade
elif numericgrade >= 90:
    print("Your letter grade is: A")
elif numericgrade >= 80:
    print("Your letter grade is: B")
elif numericgrade >= 70:
    print("Your letter grade is: C")
elif numericgrade >= 60:
    print("Your letter grade is: D")
elif numericgrade < 60:
    print("Your letter grade is: F")
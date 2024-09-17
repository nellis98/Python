#define the square function
def square (side):
    #solve for the area of the square using the defined function for square
    area_square = side * side
    #print the area of the square
    print(f"The area of the square is {str(area_square)} square units")
#define the circle function
def circle (radius):
    #solve for the area of the circle using the defined function for circle
    area_circle = 3.14 * radius ** 2
    #print the area of the circle
    print(f"The area of the circle is {str(area_circle)} square units")
#test the area of the square with a side length of 4
square(4)
#test the area of the circle with a radius of 5
circle(5)
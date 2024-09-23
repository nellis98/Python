#define a function
def main():
    #create a tulpe of the classes
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")
    #create a for loop that prints the classes in the tulpe
    for classes in programming_classes:
        print(classes)
    #print a sentance expaining how long the tulpe is
    print("The tulpe has", len(programming_classes), "classes.")
#execute the function
main()
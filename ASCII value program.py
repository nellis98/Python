#define the main function
def main():
    #prompt for user input
    user_input = input("enter a character: ")
    #create a loop that exists as long as the input length is not 1
    while len(user_input) != 1:
        #print a message asking for a single character
        print("Please enter exactly one character or the loop will continue.")
        #ask for user input again
        user_input = input("Enter a character: ")
    #convert the character to its ASCII value
    ascii_value = ord(user_input)
    #print a statement telling the user what the ASCII value of the character is
    print(f"The ASCII value of {user_input} is {ascii_value}")
main()
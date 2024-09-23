#create a dictionary for the nato phonetic alphabet
nato_alphabet = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}
#define a function
def spell_word():
    #accept user input
    user_word = input("Enter a Word: ")
    #convert user input to uppercase
    upper = user_word.upper()
    #create a for loop that will print the nato phonetic for each letter in the uppercase version of the word
    for letter in upper:
        print(nato_alphabet[letter])
#define a main function
def main():
    #call the nato convertion function
    spell_word()
#call the main function
main()

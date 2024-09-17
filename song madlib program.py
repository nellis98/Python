#define the function and its 8 variables
def custom_song (type_of_weather, emotion, plural_noun, color, time_of_day, pronoun, bodypart, emote):
    #print the song with the 8 variables inserted
    print(f"You are my {type_of_weather}, my only {type_of_weather}, you make me {emotion}, when {plural_noun} are {color}, you'll never know dear how much I love {pronoun}, please don't take my {type_of_weather} away, the other {time_of_day}, dear, As I lay sleeping, I dreamed I held you in my {bodypart}, when I awoke, dear, I was mistaken, so I hung my head and {emote}, you are my {type_of_weather}, my only {type_of_weather}, you make me {emotion}, when {plural_noun} are {color}, you'll never know, dear, how much I love {pronoun}, please don't take my {type_of_weather} away.")
#collect user input
type_of_weather = input("type of weather: ")
emotion = input("emotion: ")
plural_noun = input("plural noun: ")
color = input("color: ")
time_of_day = input("time of day: ")
pronoun = input("pronoun: ")
bodypart = input("bodypart: ")
emote = input("emote: ")
#call the function with the user input
custom_song(type_of_weather, emotion, plural_noun, color, time_of_day, pronoun, bodypart, emote)

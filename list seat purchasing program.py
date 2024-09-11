#create the list of seats
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#create a loop that prompts the user to buy a ticket
while seats:
    print(f"Available seats: {seats}")
    seat = int(input("Select a seat: "))
    #sends an alternate message when the seat is outside of range or no longer available
    if seat < 0 or seat > 20 or seat not in seats:
        print("Sorry! That seat is not available")
    #removes the selected seat if it is between 1 and 20 and is available
    if seat > 0 and seat in seats and seat <= 20 :
        del seats[int(seat-1)]
        #ends the program by user input of 0
        if seat == 0:
            break
    
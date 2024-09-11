#sets variable n equal to 99
n = 99
#creates a loop that sings the nth verse of the bottle of beer song
while n > 1:
    print(f"{n} bottles of beer on the wall \n {n} bottles of beer \n Take one down, pass it around \n {n-1} bottles of beer on the wall!")
    #reduces n by 1 each time a verse is sung
    n -= 1
#creates a print statement for the last verse of the song
else:
    print(f"1 bottle of beer on the wall \n 1 bottle of beer \n Take one down, pass it around \n No bottles of beer on the wall!")
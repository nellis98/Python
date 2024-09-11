#create the list names
names = []
#create the variable swapped
swapped = True
#create a loop that allows for the input of 5 names
for i in range(5):
    name = input("Enter name here: ")
    #add these names to the list titled names
    names.append(name)
    #print the unsorted list
    print(f"unsorted list: {names}")
#use the bubble sort algorithm to sort the names in alphabetical order
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True
            names[i], names[i + 1] = names[i + 1], names[i]
#print the alphabetical list
print(f"\nSorted: {names}")
#reverse the list
names.reverse()
#print the reversed list
print(f"Reversed list: {names}")
#create list of time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
#create empty list for storing heart rates
rates = []
#create empty list for storing heart rates with their time of day
heart_rates = []
#create total heart rate variable
total_heart_rate = 0
#create loop for input of heart rate
for i in time_slots:
    heart_rate = int(input(f"Enter heart rate in beats per minute in the {i}: "))
    #store heart rates with their time of day
    heart_rates.append([i, heart_rate])
    #store a list of heart rates
    rates.append(heart_rate)
# solve for the total of those heart rates
for i in range(len(rates)):
    total_heart_rate += rates[i]
#create a variable for the average
average = 0
#solve for the average
average = total_heart_rate / len(rates)
#print the average
print(f"Average heart rate: {average}")

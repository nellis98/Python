days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = []
total_steps = 0
average = 0
for i in days:
    daily_steps = int(input(f"How many steps did you walk on {i}:"))
    steps.append(daily_steps)
print(f"Steps on Monday: {steps[0]}")
print(f"Steps on Tuesday: {steps[1]}")
print(f"Steps on Wednesday: {steps[2]}")
print(f"Steps on Thursday: {steps[3]}")
print(f"Steps on Friday: {steps[4]}")
print(f"Steps on Saturday: {steps[5]}")
print(f"Steps on Sunday: {steps[-1]}")
for i in range(len(steps)):
    total_steps += steps[i]
print(f"\nTotal steps: {total_steps}")
average = round(total_steps / len(steps))
print(f"Average number of steps taken per day: {average}")
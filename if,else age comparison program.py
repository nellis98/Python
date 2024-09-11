#prompts and saves the users input of age
age = int(input("Age:"))
#prints age: and the age
print(f"Age:{age}")
#if the age is higher or equal to 16 print legal to drive
if age >= 16:
    print("Of legal age to drive")
#if the age is lower than 16 print too young to drive
else:
    print("Too young to drive")
#if the age is higher or equal to 18 print legal to vote
if age >= 18:
    print("Of legal age to vote")
#if the age is lower than 18 print too young to vote
else:
    print("Too young to vote")
#if the age is higher or equal to 21 print legal to buy alcohol
if age >= 21:
    print("Of legal age to buy alcohol")
#if th age is lower than 21 print too young to buy alcohol
else:
    print("Too young to buy alcohol")
#if the age is older than or equal to 65 print eligible for senior discount
if age >= 65:
    print("Eligible for a senior discount")
#if the age is less than 65 print too young for senior discount
else:
    print("Too young for senior discount")
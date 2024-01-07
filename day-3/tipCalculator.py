print("Welcome to the tip calculator")
amount = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? %"))
peopleSplit = int(input("How many people to split the bill? "))

if percentage == 10:
    percentage = 10/100
elif percentage == 12:
    percentage = 12/100
elif percentage == 15:
    percentage = 15/100

amountPerPerson = float(amount / peopleSplit)
tipPerPerson = (amountPerPerson * percentage) + amountPerPerson
print(f"Each person should pay: ${round(tipPerPerson, 2)}")
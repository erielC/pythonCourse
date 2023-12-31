from coffeeData import MENU, resources

cust_Drink = input("What would you like? (espresso, latte, cappuccino)")

resources["money"] = 0  # Declare resources["money"] as a global variable
change = 0

def check_Enough_Resources():
    if cust_Drink not in MENU:
        print("Sorry, that drink is not available.")
    elif MENU[cust_Drink]["ingredients"]["water"] > resources["water"]:
        print(f"Sorry there isn't enough water.")
    elif MENU[cust_Drink]["ingredients"]["milk"] > resources["milk"]:
        print(f"Sorry there isn't enough milk.")
    elif MENU[cust_Drink]["ingredients"]["coffee"] > resources["coffee"]:
        print(f"Sorry there isn't enough coffee.")
        
def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['milk']}")
    print(f"Money: {resources['money']}")  # Print resources["money"] globally

def process_Coins():
    global change
    drink_Water = MENU[cust_Drink]["ingredients"]["water"]
    drink_Milk = MENU[cust_Drink]["ingredients"]["milk"]
    drink_Coffee = MENU[cust_Drink]["ingredients"]["coffee"]
    print("Please insert coins")
    amount_Quarters = int(input("How many quarters:  "))
    amount_Dimes = int(input("How many dimes: "))
    amount_Nickels = int(input("How many nickels:  "))
    amount_Pennies = int(input("How many pennies:  "))
    drink_Cost = MENU[cust_Drink]["cost"]
    cust_total = (amount_Quarters * 0.25) + (amount_Dimes * 0.10) + (amount_Nickels * 0.05) + (amount_Pennies * 0.01)
    if cust_total > drink_Cost:
        change = cust_total - drink_Cost 
        resources["money"] += drink_Cost # Update resources["money"]
        resources["water"] -= drink_Water
        resources["milk"] -= drink_Milk
        resources["coffee"] -= drink_Coffee
        return resources, change
    elif cust_total == drink_Cost:
        resources["money"] += cust_total  # Update resources["money"]
        resources["water"] -= drink_Water
        resources["milk"] -= drink_Milk
        resources["coffee"] -= drink_Coffee
        return resources
    elif cust_total < drink_Cost:
        answer = "Sorry that's not enough money"
        print(answer)

check_Enough_Resources()        
process_Coins()
if change > 0:
    print(f"Here is {change} in change")
print(f"Here is your {cust_Drink}. Enjoy!")
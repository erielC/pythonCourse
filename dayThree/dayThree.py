print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 
ride_for_free = False

if height > 120:
  print("You can ride on the rollercoaster")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Pay $5")
  elif age <=18:
    bill = 7 
    print("Pay $7")
  elif age >= 45 and age <=55:
    print("You ride for free")
  else: 
    bill = 12
    print("Pay $12")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo.upper() == "Y":
    bill += 3
    print(f"Your final bill is {bill} dollars")
  else:
    print(f"Your total bill is {bill} dollars")
else: 
  print(f"You cannot ride on the rollercoaster the required height of 120cm doesnt match your height of {height}")
  


  

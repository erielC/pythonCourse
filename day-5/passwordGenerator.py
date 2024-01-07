#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Letter Portion of Password
newLetter = ""
for n in range(0,nr_letters):
  x = random.randint(0, (len(letters) - 1))
  newLetter += letters[x]
  
#Sybmol 
newSymbol = ""
for n in range(0,nr_symbols):
  y = random.randint(0, (len(symbols) - 1))
  newSymbol += symbols[y]

newNumber = ""
for n in range(0,nr_numbers):
  z = random.randint(0, (len(numbers) - 1))
  newNumber += numbers[z]
print(f"Not reshuffled password is: newLetter + newSymbol + newNumber")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Via course not mine code 
password_List = []

for char in range(1, nr_numbers + 1):
  password_List += random.choice(letters)
for char in range(1, nr_symbols + 1):
  password_List += random.choice(symbols)
  
for char in range(1, nr_numbers + 1):
  password_List += random.choice(numbers)

print(f" password list: {password_List}")
random.shuffle(password_List)
print(password_List)

#print array in string format

password = ""
for char in password_List:
  password += char
print(password)
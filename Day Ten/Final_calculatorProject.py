import os

from art import logo
print(logo)

def clear_terminal(): #clearing terminal if more bidders to the auction 
    os.system('cls' if os.name == 'nt' else 'clear')

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

choice = True

while choice: 
  x = float(input("What's the first number?: "))
  calc_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
  }
  for symbol in calc_operations:
    print(symbol)
  operation = input("Pick an operation: ")
  y = float(input("What's the next number?: "))

  if operation == '+':
    result = add(x, y)
    print(f"{x} + {y} = {result}")
  elif operation == '-':
    result = subtract(x, y)
    print(f"{x} - {y} = {result}")
  elif operation == '*':
    result = multiply(x, y)
    print(f"{x} * {y} = {result}")
  elif operation == '/':
    result = divide(x, y)
    print(f"{x} / {y} = {result}")
  else:
    print("Invalid input")
    
  contiue_statement = input("Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: ")
  if contiue_statement == "n":
    choice = False
  elif contiue_statement == "y":
    clear_terminal()
    
  
  # TODO Make this calculator more efficient and cleaner
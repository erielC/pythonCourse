from art import logo
import os

print(logo)
continue_auction = True
auction = []

def clear_terminal(): #clearing terminal if more bidders to the auction 
    os.system('cls' if os.name == 'nt' else 'clear')
    
def add_to_auction(n, b): #add bidder to the auction 
  auction_Details = {} 
  auction_Details["Name"] = n
  auction_Details["Bid"] = b
  auction.append(auction_Details)
  
def compare_bidders(auction): # Written with github Copilot
  highest_bid = 0
  winner = ""
  for bidder in auction: #This loop is used to iterate over each item in a collection. In this case, the collection is auction, and each item is referred to as bidder within the loop.
    
    # Code (below) is accessing the values associated with the keys "Name" and "Bid" from the dictionary bidder. It assigns these values to the variables name and bid respectively.
    name = bidder["Name"]
    bid = bidder["Bid"]
    if bid > highest_bid:
      highest_bid = bid
      winner = name
  print(f"The winner is {winner} with a bid of ${highest_bid}")



while continue_auction:
  print("Welcome to the secret auction program.")
  name = input("What is your name? ")
  bidAmount = int(input("What's your bid?: $"))
  add_to_auction(n=name, b=bidAmount)
  decision = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if decision == "no":
    continue_auction = False
  elif decision == "yes":
    clear_terminal()
    continue_auction = True


compare_bidders(auction)

from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCards = []
computerCards = []
continue_Game = True

def deal_User_Card():
  userCards.append(random.choice(cards))
  userCards.append(random.choice(cards))
  return userCards

def deal_User_Again(userCards):
  userCards.append(random.choice(cards))
  print(f"Your final cards: {userCards}, final score: {sum(userDeck)}")
  
def deal_Comp_Card():
  computerCards.append(random.choice(cards))
  return computerCards

def win_Or_Lose(userDeck, compDeck): 
  userSum = sum(userDeck)
  compSum = sum(compDeck)
  if userSum > 21:
    print("You went over. You lose")
  elif userSum == 21: 
    print("Blackjack. You Win")
  elif compSum == 21: 
    print("Computer has blackjack. You Lose.")
  elif userSum < compSum:
    print("Computer Deck was bigger than yours. You lose.")
  elif userSum > compSum and userSum <= 21:
    print("Your deck is bigger than computer. You win")
    
def clear_terminal():  
    os.system('cls' if os.name == 'nt' else 'clear')
    
while continue_Game: 
  print(logo)
  userDeck = userCards # created so when the sum() function used it adds up the cards in the deck correctly 
  compDeck = computerCards
  print(f"Your cards: {deal_User_Card()}, current score: {sum(userDeck)}")
  print(f"Computer's first card: {deal_Comp_Card()}")
  dealChoice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

  #Game deciding whether you lose or win based off final deck
  if dealChoice == "n": 
    print(f"Your final cards: {userDeck}, final score: {sum(userDeck)}")
    print(f"Computer's final hand: {deal_Comp_Card()}, final score: {sum(compDeck)}")
    win_Or_Lose(userDeck, compDeck)
  elif dealChoice == "y":
    deal_User_Again(userCards)
    print(f"Computer's final hand: {deal_Comp_Card()}, final score: {sum(compDeck)}")
    win_Or_Lose(userDeck, compDeck)
  
  #Decides if game continues or not
  gameContinuation = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if gameContinuation == "n":
    continue_Game = False
    print("Have a good day")
  elif gameContinuation == "y":
    continue_Game = True
    userDeck.clear()
    compDeck.clear()
    clear_terminal()
  
  
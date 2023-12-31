from art import logo, vs
from gameData import data
import random
import os


game_Decide = True
final_Score = 0
decide_game_lost = 1

def clear_terminal():  
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    print(logo)
    print(f"Compare A: {rChoiceA['name']}, {rChoiceA['description']}, from {rChoiceA['country']}")
    print(vs)
    print(f"Compare B: {rChoiceB['name']}, {rChoiceB['description']}, from {rChoiceB['country']}")
   
while game_Decide:  
    rChoiceA = random.choice(data)
    rChoiceB = random.choice(data)
    game()
    decision = input("Who has more followers? Type 'A' or 'B': ").upper()
    a_followers = rChoiceA['follower_count']
    b_followers = rChoiceB['follower_count']
    if decision == "A" and a_followers > b_followers:
        final_Score += 1
        z = (f"Correct! Current Score: {final_Score}")
        print(z)
    elif decision == "A" and a_followers < b_followers:
        decide_game_lost -= 1
    elif decision == "B" and b_followers > a_followers: 
        final_Score += 1
        z = (f"Correct! Current Score: {final_Score}")
        print(z)
    elif decision == "B" and b_followers < a_followers:
        decide_game_lost -= 1
    if decide_game_lost == 0: 
        clear_terminal()
        print(logo)
        print(f"Sorry that's wrong. Final score was {final_Score}")
        game_Decide = False
    
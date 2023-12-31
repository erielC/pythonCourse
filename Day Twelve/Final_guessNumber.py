import random
from art import logo

# Global Variables example
## HARD_LEVEL_GUESSES = 5 
## EASY_LEVEL_GUESSES = 10

#### FUTURE REFERENCE (MAKE MORE FUNCTIONS)
print(logo)
print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number_guessed = random.randint(1,100)

num_of_attempts = 0
if difficulty == "easy":
    num_of_attempts = 10
elif difficulty == "hard":
    num_of_attempts = 5
print(f"You  have {num_of_attempts} remaining to guess the number")

def num_guesses_left():
    print(f"You have a {num_of_attempts} remaining to guess the number")
while num_of_attempts > 0:
    guess = int(input("Make a guess: "))
    num_of_attempts -= 1
    if guess > number_guessed:
        print("Too High")
        num_guesses_left()
    elif guess < number_guessed:
        print("Too Low")
        num_guesses_left()
    else: 
        print("Youve guessed the right number")
        break
if num_of_attempts == 0:
    print(f"You have run out of guesses the number was {number_guessed}")
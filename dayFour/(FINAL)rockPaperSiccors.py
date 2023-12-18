import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
forms = [rock, paper, scissors]

humanChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(forms[humanChoice])

print("Computer chose:")
computerChoice = random.randint(0,2)
print(forms[computerChoice])

win_or_lose = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

if (humanChoice == 0 and computerChoice ==2) or (humanChoice == 1 and computerChoice ==0) or (humanChoice == 2 and computerChoice == 1): 
  print("You Win")
elif (humanChoice == computerChoice):
  print("Its a tie")
else:
  print("You Lose")
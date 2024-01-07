import random

#starter code before the while loop
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for underscore in chosen_word:
  display.append("_")

tracker = 0
while tracker != len(chosen_word):
  guess = input("Guess a letter: ").lower()
  for position in range (0, len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      tracker += 1
      print(display)


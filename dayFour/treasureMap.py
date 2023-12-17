line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?


letter = position[0].lower() #Gets letter at first index
abc = ["a", "b", "c"]
letterIndex = abc.index(letter)
numberIndex = int(position[1])-1 
map[numberIndex][letterIndex] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
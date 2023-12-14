print(len(str(1526)))
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

num_char = len(input("What is your name?\n"))
print("Your name is " + str(num_char) + " characters long.")

# BMI Calculator
height = input()
weight = input()

height = float(height)
weight = float(weight)
BMI = int((weight / (height ** 2)))
print(BMI)

#f-Strings
score = 0
height = 1.8
isWinning = True
print(f"Hello your score is {score} and height is {height} plus lets see if your winning T or F? :\n Answer: {isWinning}")

#Weeks left in a Lifetime
age = input()
WeeksYear = 52
age = int(age)
WeekLeft = (52*90)-(52*age)
print(f"You have {WeekLeft} weeks left.")
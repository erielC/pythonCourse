from turtle import Turtle, Screen
import random

is_race_on = False 
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

starting_x_coords = -230
starting_y_cords = -80
turtle_num = 0
all_turtles = []

for color in rainbow_colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(rainbow_colors[turtle_num])
    new_turtle.goto(x=starting_x_coords, y=starting_y_cords)
    starting_y_cords += 30
    turtle_num += 1
    all_turtles.append(new_turtle)

if user_bet: # Used to check if the input user_bet exist
    is_race_on = True
    
while is_race_on:
  
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                            
    
        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    
screen.exitonclick()
from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Creates snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Moves Sake
game_is_on = True
while game_is_on: 
    screen.update()
    time.sleep(0.1) #one second delay when each segment moves
    
    snake.move()

 

screen.exitonclick()
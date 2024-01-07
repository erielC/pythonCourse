from turtle import Turtle, Screen 
# Drawing a squre
eriel = Turtle()
eriel.shape("turtle")
for num in range(4):
    eriel.forward(100)
    eriel.left(90)

import random as r
# Different way to print out the name 
hello = r.choice([1,2,3])


screen = Screen()
screen.exitonclick()
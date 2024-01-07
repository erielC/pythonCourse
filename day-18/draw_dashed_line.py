from turtle import Turtle, Screen

eriel = Turtle()
for num in range(10):
    eriel.forward(5)
    eriel.penup()
    eriel.forward(5)
    eriel.pendown()
screen = Screen()
screen.exitonclick()
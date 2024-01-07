from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_foward():
    t.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_foward) # When using functions as arguements dont include parenthesis at the end 
screen.exitonclick()
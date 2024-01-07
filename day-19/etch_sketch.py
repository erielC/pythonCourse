from turtle import Turtle, Screen

bol = Turtle()
screen = Screen()

def move_forward():
    bol.forward(30)
    
def move_backward():
    bol.backward(30)
    
def turn_left():
    bol.setheading(bol.heading() + 10)
    
def turn_right():
    bol.setheading(bol.heading() - 10)
    

def clear_screen():
    bol.clear()
    bol.penup()
    bol.home()
    bol.pendown()
    bol.setheading(0)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()

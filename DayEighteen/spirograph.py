import turtle as t
import random

tirly = t.Turtle()
tirly.speed('fastest')
t.colormode(255)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b 
    
for num in range(0,360,5):
    tirly.color(random_colors())
    tirly.circle(150,360)
    tirly.setheading(num)

screen = t.Screen()
screen.exitonclick()

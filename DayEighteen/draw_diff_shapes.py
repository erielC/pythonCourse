from turtle import Turtle, Screen
import random

t = Turtle()

colors = ['white', 'yellow', 'orange', 'red', 'pink', 'purple', 'blue', 'green', 'brown', 'black', 'gray', 'lightgray', 'darkgray', 'gold', 'silver', 'maroon', 'crimson', 'coral', 'salmon', 'tomato', 'sienna', 'chocolate', 'saddlebrown', 'olive', 'darkolivegreen', 'lime', 'seagreen', 'teal', 'cyan', 'deepskyblue']

def random_color():
    return random.choice(colors)

def draw_shape(num_sides):
    angle = 360 / num_sides
    t.color(random_color())
    for _ in range(num_sides):
        t.forward(40)
        t.right(angle)

for shape_sides in range(3,11):
    draw_shape(shape_sides)

screen = Screen()
screen.exitonclick()
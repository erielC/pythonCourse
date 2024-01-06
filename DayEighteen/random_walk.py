import turtle as t
import random

tom = t.Turtle()
tom.pensize(15)
tom.speed(10)

# Generate random colors
t.colormode(255)


# colors = ['red', 'pink', 'purple','green', 'brown', 'black', 'gray', 'gold', 'silver', 'maroon', 'crimson', 'coral', 'salmon', 'tomato', 'chocolate', '', 'olive', 'teal'] // Preset of colors

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

def direction_to_turn():
    directions = [0,90,180,270]
    return random.choice(directions)

for _ in range(100):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(direction_to_turn())
    
screen = t.Screen()
screen.exitonclick()
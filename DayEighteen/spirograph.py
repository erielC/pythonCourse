import turtle as t
import random

tirly = t.Turtle()
tirly.speed('fastest')
tirly.ht()
t.colormode(255)
t.bgcolor("black")
t.setup(width=1300, height=800)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b 
    
def make_circle():
    for num in range(0,365,5):
        # tirly.color(random_colors())
        tirly.color("white")
        tirly.circle(150,360)
        tirly.setheading(num)

make_circle()
# tirly.up()
# tirly.goto(x=-330, y=80)
# tirly.down()
# make_circle()
# tirly.up()
# tirly.goto(x=-330, y=-80)
# tirly.down()
# make_circle()
# tirly.up()
# tirly.goto(x=330, y=80)
# tirly.down()
# make_circle()
# tirly.up()
# tirly.goto(x=330, y=-80)
# tirly.down()
screen = t.Screen()
screen.exitonclick()

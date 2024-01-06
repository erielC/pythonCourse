# import colorgram

# EXTRACTING COLORS FROM IMAGE

# color_list = colorgram.extract("DayEighteen/image.jpg", 35)
# color_palette = []

# for i in range(len(color_list)):
#     r = color_list[i].rgb.r
#     g = color_list[i].rgb.g
#     b = color_list[i].rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)

import turtle as t
import random

color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52), (179, 199, 184), (133, 41, 39), (76, 63, 49), (38, 79, 82)]

y = t.Turtle()

y.penup()
y.goto(-250, -200)
y.pendown()
y.speed(10)
t.colormode(255)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b 

def draw_row():
    for num in range(10):
        y.dot(20, random_colors())
        y.penup()
        y.forward(50)
        y.pendown()
    
x_coordinates = -250
y_coordinates = -200
start = 50
for _ in range(10):
    draw_row()
    y.penup()
    y.goto(x_coordinates, y_coordinates + start)
    y.pendown
    start += 50

   

screen = t.Screen()
screen.exitonclick()
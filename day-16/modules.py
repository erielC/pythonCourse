# from turtle import Turtle, Screen
# timmy = Turtle() #created a turtle class into ann object called timmy 
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkKhaki")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick() # Program continues running on screen until clicked on 

from prettytable import PrettyTable

table = PrettyTable() #constructing prettytable object
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# making your own function 

def myFunction():
  print("Hello and bye")

myFunction() #printing function 

# While Loop 
# Robot Game world Problem debug problemworld1 
# code i used: 
def turn_right():
    turn_left()
    turn_left()
    turn_left()



while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()

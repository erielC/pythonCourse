enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope 

def drinkPotion():
  potionStrength = 2
  print(potionStrength)

drinkPotion()
# print(potionStrength)

## Global Scope 
player_Health = 10
def game():
  def drink_oPotion():
    potion_strength = 2
    print(player_Health)

# drink_oPotion() will give an error becuase it is not in scope
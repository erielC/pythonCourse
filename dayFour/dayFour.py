import random
import myModule

random_int = random.randint(1,10)
print(random_int) # Random number generator between 1 and 10

#Printing variables from other python file
print(myModule.pi)
print(myModule.hello)

# Random float generator between 0.00-0.99........
random_Float = random.random()
print(random_Float)

randomFloatGenerator = random.random() * 5
print("{:.2f}".format(randomFloatGenerator)) # Random float number generator between 0.00-4.99........

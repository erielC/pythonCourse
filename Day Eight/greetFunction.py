# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
  print("Hello")
  print("Hello")
  print("Hello")
greet()

def greet_with_name(name):
  print(f"Hello {name} how are you doing today?")
greet_with_name(input("Enter name here: "))

#multiple inputs
def greet_with(name, location):
  print(f"Hello {name} I see you are from {location} I hear its nice!")
greet_with(input("Enter Name Here: "), input("Enter location here: "))


a = 4
b = 3
c = 6
def agruement_example(a=2,c=3,b=4):
  print(f"Your letter value of a: {a}")
  print(f"Your letter value of b: {b}")
  print(f"Your letter value of c: {c}")
agruement_example(2,3,4)
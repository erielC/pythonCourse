programming_dictionary = {
  "Bug" : "An error in a program that prevents the program from running as expected.",
  "Function" : "A piece of code that you can easily call over and over again.",
  "Loop" : "The action of doing something over and over again."
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Loop"])

programming_dictionary["Addition"] = "Adding two numbers together."
print(programming_dictionary)
 # TODO create an empty dictionary
empty_dictionary = {} 
empty_dictionary["Key"] = "Value" 
print(empty_dictionary)


# TODO Wipe a dictionary
empty_dictionary = {}
print(empty_dictionary)

# TODO Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# TODO Looping through a dictionary
for thing in programming_dictionary:
  print(thing)
  print(programming_dictionary[thing])
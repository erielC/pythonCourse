# Write your code below this line 👇
def prime_checker(number):
  numOfFactors = 0
  for i in range(1, number + 1):
       if number % i == 0:
           numOfFactors += 1
  if number > 2 and number % 2 == 0: #Base case since even numbers greater than 2 are only composite
    print("It's not a prime number.")
  elif numOfFactors > 2:
    print("It's not a prime number.")
  else: 
    print("It's a prime number.")
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)


#Instructor Code
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")   
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)
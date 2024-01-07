fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: 
  print(fruit)
  print(fruit + " Pie")
print(fruit)

#Adding all the numbers from 1-100  
total = 0
for number in range(1,101):
  total += number
print(total, end=" ")

#Adding all the numbers from 1-100 (evens only)
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
amt = 0
for n in range (0,target+1,2):
  amt += n
print(amt)
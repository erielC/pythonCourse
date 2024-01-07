alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plainText, amountShifted):
  cypher_text = ""
  for letter in plainText: #iterates through each letter of the word
    position = alphabet.index(letter) #finds the index in alphabet list of the letter in the word 
    new_position = position + amountShifted #amount shifted from regular position
    
    if new_position > len(alphabet)-1: #Exception breaker when ex. Z needs to be shifted (however since end of list) is subracted by list length
      new_position = new_position - len(alphabet)
      
    new_Letter = alphabet[new_position] #with shifted amount added will now allocate the newLetter(shifted from old letter) to new position on alphabet list b/c of addition of shift amount to regular ammout in (new_position)
    cypher_text += new_Letter #new_Letter is added to the empty string and keeps getting added until end of loopeno
  print(f"The encoded text is {cypher_text}")
def decrypt(plainText, amountShifted):
  
  cypherText = ""
  for letter in plainText:
    position = alphabet.index(letter)
    new_position = position - amountShifted
    
    #Exception if index subracted (ex. beginning of list) will give IndexOutOfBounds so use this if-statement
    if new_position < 0: 
      new_position = new_position + len(alphabet)

    new_Letter = alphabet[new_position]
    cypherText += new_Letter
  print(f"The decoded text is {cypherText}")
  

if direction == "encode": 
  encrypt(plainText=text, amountShifted=shift)
elif direction == "decode": 
  decrypt(plainText=text, amountShifted=shift)

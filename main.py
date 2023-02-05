#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pas=""
for x in range(1,nr_letters+1):
  pas+=random.choice(letters)
for x in range(1,nr_numbers+1):
  pas+=random.choice(numbers)
for x in range(1,nr_symbols+1):
  pas+=random.choice(symbols)
print(f"your password easy level is: " +pas)  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
newpas=[]
for x in range(1,nr_letters+1):
  newpas.append(random.choice(letters))
for x in range(1,nr_numbers+1):
  newpas.append(random.choice(numbers))
for x in range(1,nr_symbols+1):
  newpas.append(random.choice(symbols))
random.shuffle(newpas)
newpasw=""
for x in newpas:
  newpasw+=x
print(f"your password hard level is: " +newpasw)
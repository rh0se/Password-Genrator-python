#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
length = nr_letters + nr_numbers + nr_symbols

while length < 8:
  print(f"The length of your password will be {length}")
  print("Password length too short")
  print("An eight-character password is recommended because it's long enough to provide adequate security and still short enough for users to easily remember.")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  length = nr_letters + nr_numbers + nr_symbols

# no_letters = int(nr_letters)
# no_symbols = int(nr_symbols)
# no_numberrs = int(nr_numbers)
print(f"The length of your password will be {length}")
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

password_1 = []
for password in range(0, nr_letters):
  password_1.append(letters[password])
for password in range(0, nr_numbers):
  password_1.append(numbers[password])
for password in range(0, nr_symbols):
  password_1.append(symbols[password])

random.shuffle(password_1)

password_strings = ""
for i in password_1:
  password_strings += i

print("Your password is:" + password_strings)




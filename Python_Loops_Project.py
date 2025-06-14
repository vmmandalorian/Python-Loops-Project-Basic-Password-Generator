import random
import secrets
import string


all_letters = string.ascii_letters
unique_numbers = random.sample(range(1, 11), 10)
letters = all_letters
numbers = unique_numbers
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '/', '\\', '|', '?', '"', ':']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for char in range(1, nr_letters , +1):
    password_list.append(secrets.choice(letters))
for char in range(1, nr_symbols , +1):
    password_list.append(secrets.choice(symbols))
for char in range(1, nr_numbers , +1):
    password_list.append(secrets.choice(numbers))
password = ""
for char in password_list:
  password += f"{char}"

print(f"Your password is: {password}")


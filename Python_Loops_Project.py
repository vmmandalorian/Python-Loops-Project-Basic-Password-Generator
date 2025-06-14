import random
import secrets
import string


all_letters = string.ascii_letters
letters = all_letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
  password += char

print(f"Your password is: {password}")

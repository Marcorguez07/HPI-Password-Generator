# Hpi Group Work by Danilo, Raul, Bhomik, Muhhamed and Marco,
import random
import string

print("Welcome to the improved password generator!\n")

#### Ask how many passwords to generate
while True:
    try:
        count = int(input("How many passwords would you like to generate? "))
        if count > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#### Ask for password length
while True:
    try:
        length = int(input("Enter the desired length of each password: "))
        if length > 0:
            break
        print("Length must be greater than zero.")
    except ValueError:
        print("Invalid number, try again.")

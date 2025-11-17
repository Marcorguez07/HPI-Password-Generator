# Hpi Group Work by Danilo, Raul, Bhomik, Muhhamed and Marco,
import random
import string

print("Welcome to the improved password generator!\n")

# Ask how many passwords to generate
while True:
    try:
        count = int(input("How many passwords would you like to generate? "))
        if count > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Ask for password length
while True:
    try:
        length = int(input("Enter the desired length of each password: "))
        if length > 0:
            break
        print("Length must be greater than zero.")
    except ValueError:
        print("Invalid number, try again.")

# Ask which character types to include
use_letters = input("Include letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Build the character pool
letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()"
pool = ""

if use_letters: pool += letters
if use_numbers: pool += numbers
if use_symbols: pool += symbols 

if not pool:
    print("Error: No character types selected. Exiting program.")
    exit()

#### Basic strength calculator
def strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in symbols for c in password): score += 1
    if len(password) >= 12: score += 1
    return score 
#### Generate and display passwords
for i in range(count):
    pwd = "".join(random.choice(pool) for _ in range(length))
    score = strength(pwd)
    level = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"][score - 1]


print(f"\nPassword #{i+1}: {pwd}")
    print("Strength:", level)
    print("\nPassword generation complete!")
    ### End of the code, - bhomik

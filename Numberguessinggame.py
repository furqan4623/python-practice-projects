import random

secret_number = random.randint(1,100)

print("Welcome to Number Guess Game!")
print("I have selected a number between 1 to 100. ")

guess = int(input("Enter your Guess. "))

if guess == secret_number:
    print("Correct. ")
else:
    print("Wrong! The number was", secret_number)

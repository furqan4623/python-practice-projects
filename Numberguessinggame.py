import random

secret_number = random.randint(1,100)
attempts = 5

print("Welcome to Number Guess Game!")
print("I have selected a number between 1 to 100. ")

while attempts > 0:
    guess = int(input("Enter your Guess"))

    if guess == secret_number:
        print("Correct You Win ")
        break
    elif guess > secret_number:
        print("Too High ")
    else:
        print("Too Low ")

    attempts -= 1
    print("Attempts Left", attempts)

    if attempts == 0:
        print("Game Over ")
        print("The Number was is ", secret_number)

        
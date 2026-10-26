
import random

name = input("Enter your name: ")

secret_number = random.randint(1, 20)

print("Welcome", name, "!")
print("I have selected a number between 1 and 20.")
print("You have 6 attempts to guess the number.")

attempts = 0

while attempts < 6:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Your guess is too low.")

    elif guess > secret_number:
        print("Your guess is too high.")

    else:
        print("Congratulations,", name, "!")
        print("You guessed the correct number in", attempts, "attempts.")
        break

if guess != secret_number:
    print("Game over!")
    print("The correct number was", secret_number)


# Number Guessing Game

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")
        break
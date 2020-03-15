# Program that generates a random number and asks user to enter the number they think it is (between 0 and 20)

import random  # Importing the random library to generate the random numbers

randNum = random.randint(0, 21)  # Generates a random number between 0 and 20

# Welcome message and short introduction to the game
print("Welcome to the number guessing game")
print("Guess what number was selected between 0 and 20")
print("Enter -1 to exit the game")

# Makes sure that the program does not crash due to a non number input
isNum = False
while not isNum:
    try:
        user_Guess = int(input("Enter number: "))  # Taking input from user
        isNum = True
    except ValueError:
        print("Not a number")

# This loop keeps the game going until the user enters -1
while user_Guess != -1:

    correctGuess = False  # Variable that checks if the correct number was guessed so it goes onto next number

    if randNum == user_Guess:
        print("Correct guess")
        correctGuess = True

    # This loop keeps checking if the input is correct or gives a hint to user if wrong
    while not correctGuess:

        if randNum == user_Guess:
            print("Correct guess")
            correctGuess = True
            break
        elif user_Guess > randNum:
            print("Guess is greater than selected number")
        elif user_Guess < randNum:
            print("Guess is less than selected number")

        isNum = False
        while not isNum:
            try:
                user_Guess = int(input("Enter number: "))  # Taking input from user
                isNum = True
            except ValueError:
                print("Not a number")

    print("Enter number or if you want to exit then enter -1: ")

    isNum = False
    while not isNum:
        try:
            user_Guess = int(input("Enter number: "))  # Taking input from user
            isNum = True
        except ValueError:
            print("Not a number")

    randNum = random.randint(0, 21)

print("Game ended")

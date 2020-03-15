# Program randomly generates between rock, paper and scissors and user has to win against computer

import random  # Importing the random library to use to randomly pick between choices

# Welcome message and introduction to game
print("Welcome to the rock, paper, scissors game")
print("Game will continue forever until 'exit' is entered")

# Generates the choice which the user has to beat
choices = ["rock", "paper", "scissors", "exit"]
rand_Num = random.randint(0, 2)
comp_Choice = choices[rand_Num]

# Checks if the choice entered by user is a valid option
user_Choice = input("Enter your choice: ").lower()
while user_Choice not in choices:
    print("Not a valid choice")
    user_Choice = input("Enter your choice: ").lower()

# Loop keeps game going forever until 'exit' is entered
while user_Choice != "exit":

    # Checking the result of the game
    if user_Choice == "rock":
        if comp_Choice == "rock":
            print("Result: Draw")
        if comp_Choice == "paper":
            print("Result: You lose")
        if comp_Choice == "scissors":
            print("Result: You win")

    if user_Choice == "paper":
        if comp_Choice == "rock":
            print("Result: You win")
        if comp_Choice == "paper":
            print("Result: Draw")
        if comp_Choice == "scissors":
            print("Result: You lose")

    if user_Choice == "scissors":
        if comp_Choice == "rock":
            print("Result: You lose")
        if comp_Choice == "paper":
            print("Result: You win")
        if comp_Choice == "scissors":
            print("Result: Draw")

    rand_Num = random.randint(0, 2)
    comp_Choice = choices[rand_Num]

    user_Choice = input("Enter your choice: ").lower()
    while user_Choice not in choices:
        print("Not a valid choice")
        user_Choice = input("Enter your choice: ").lower()

print("Game ended")

import tkinter as tk
from num_guess_game import *

game = guess_num_game(0, 0)
game_made = False
game_over = False


def make_game():
    global game_made, game
    try:
        num1 = int(entr_first.get())
        num2 = int(entr_second.get())
    except ValueError:
        game_made = False
        lbl_display2["text"] = "Must enter two numbers"
        lbl_display1["text"] = "Game not ready"
        return
    if num1 >= num2:
        game_made = False
        lbl_display2["text"] = "First number must be smaller than second number"
        lbl_display1["text"] = "Game not ready"
        return
    lbl_display2["text"] = ""
    game = guess_num_game(num1, num2)
    game_made = True
    lbl_display1["text"] = "New game ready"


def make_guess():
    global game_made, game_over
    if not game_made:
        return
    if game_over:
        lbl_display1["text"] = "Game finished! Enter numbers again to play"
        return
    try:
        guess = int(entr_guess.get())
    except ValueError:
        lbl_display1["text"] = "Guess must be a number between the entered numbers (inclusive)"
        return
    if not (game.get_first_num() <= guess <= game.get_second_num()):
        lbl_display1["text"] = "Guess not in range"
        return
    if guess < game.get_guess_num():
        lbl_display1["text"] = "Guess is less than the number"
        return
    if guess > game.get_guess_num():
        lbl_display1["text"] = "Guess is greater than the number"
        return
    if guess == game.get_guess_num():
        lbl_display1["text"] = "You guessed the right number!"
        game_over = True


window = tk.Tk()
window.title("Number guessing game")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_display = tk.Label(master=window, text="Input the two numbers to start", fg="#5E6AE7")
lbl_display.grid(row=0, column=0)

lbl_first = tk.Label(master=window, text="First number:", bg="#D63636")
lbl_first.grid(row=1, column=0, sticky="nsew")
entr_first = tk.Entry(master=window)
entr_first.grid(row=1, column=1, sticky="nsew")

lbl_second = tk.Label(master=window, text="Second number:", bg="#D63636")
lbl_second.grid(row=2, column=0, sticky="nsew")
entr_second = tk.Entry(master=window)
entr_second.grid(row=2, column=1, sticky="nsew")

btn_apply = tk.Button(master=window, text="Click to apply", bg="#36D692", command=make_game)
btn_apply.grid(row=3, column=2, sticky="nsew")

lbl_display2 = tk.Label(master=window, fg="#5E6AE7")
lbl_display2.grid(row=3, column=0, sticky="nsew")

lbl_display1 = tk.Label(master=window, text="Game not ready", fg="#5E6AE7")
lbl_display1.grid(row=4, column=0)

lbl_guess = tk.Label(master=window, text="Guess", bg="#D63636")
lbl_guess.grid(row=5, column=0, sticky="nsew")
entr_guess = tk.Entry(master=window)
entr_guess.grid(row=5, column=1, sticky="nsew")
btn_guess = tk.Button(master=window, text="Click to guess", bg="#36D692", command=make_guess)
btn_guess.grid(row=5, column=2, sticky="nsew")

window.mainloop()

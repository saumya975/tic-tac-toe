import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize variables
current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = []

# Function to handle button click
def on_click(row, col):
    global current_player

    # If the clicked cell is empty, mark it with the current player's symbol
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        # Check if the current player has won
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif is_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This spot is already taken!")

# Function to check for a winner
def check_winner(player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the game is a tie
def is_tie():
    return all([spot != " " for row in board for spot in row])

# Function to reset the game board
def reset_game():
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            board[row][col] = " "
            buttons[row][col].config(text="")

# Create the Tic-Tac-Toe board (3x3 grid of buttons)
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text="", width=10, height=3, font=("Arial", 24),
                           command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Start the main event loop
root.mainloop()

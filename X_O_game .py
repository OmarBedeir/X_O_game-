

import tkinter as tk
import random
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        # Initialize the game
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initialize scores
        self.player_score = 0
        self.computer_score = 0

        # Create game interface
        self.create_widgets()
        self.restart_game()

    def create_widgets(self):
        # Create labels and buttons for the game interface
        self.score_label = tk.Label(root, text="You: 0 Computer: 0", font=('Helvetica', 12))
        self.score_label.grid(row=0, column=0, columnspan=3)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=1, column=0, columnspan=3)

        self.result_label = tk.Label(root, text="", font=('Helvetica', 12))
        self.result_label.grid(row=2, column=0, columnspan=3)

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                # Create buttons for the game grid
                self.buttons[i][j] = tk.Button(root, text="", font=('Helvetica', 24), width=5, height=2, command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i+3, column=j)

    def restart_game(self):
        # Restart the game
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.update_buttons_state()
        self.result_label.config(text="")

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(bg='SystemButtonFace')

    def make_move(self, row, col):
        # Handle player's move
        if self.board[row][col] == "" and not self.check_game_over():
            self.board[row][col] = self.current_player
            self.update_buttons_state()
            if self.check_game_over():
                self.update_score_label()
                self.show_result_message()
            else:
                self.switch_player()
                self.computer_move()

    def computer_move(self):
        # Handle computer's move
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if available_moves:
            computer_row, computer_col = random.choice(available_moves)
            self.board[computer_row][computer_col] = "O"
            self.update_buttons_state()
            if self.check_game_over():
                self.update_score_label()
                self.show_result_message()
            else:
                self.switch_player()

    def update_buttons_state(self):
        # Update the state of buttons in the game grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.board[i][j], state=tk.DISABLED if self.board[i][j] != "" else tk.NORMAL)

    def switch_player(self):
        # Switch between player X and O
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_game_over(self):
        # Check if the game is over
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                self.display_winner(self.board[i][0], [(i, 0), (i, 1), (i, 2)])
                return True

            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.display_winner(self.board[0][i], [(0, i), (1, i), (2, i)])
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.display_winner(self.board[0][0], [(0, 0), (1, 1), (2, 2)])
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.display_winner(self.board[0][2], [(0, 2), (1, 1), (2, 0)])
            return True

        if all(self.board[i][j] != "" for i in range(3) for j in range(3)):
            self.display_tie()
            return True

        return False

    def display_winner(self, winner, winning_positions):
        # Display the winner and highlight the winning positions
        if winner == "X":
            self.player_score += 1
        else:
            self.computer_score += 1
        self.update_score_label()
        self.result_label.config(text=f"{winner} wins!", fg='green')
        for position in winning_positions:
            self.buttons[position[0]][position[1]].config(bg='lightgreen')

    def display_tie(self):
        # Display a tie and highlight the entire grid
        self.result_label.config(text="It's a tie!", fg='red')

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(bg='red')

    def update_score_label(self):
        # Update the score label
        self.score_label.config(text=f"You: {self.player_score} Computer: {self.computer_score}")

    def show_result_message(self):
        # Display a message box to ask if the player wants to play again
        answer = messagebox.askyesno("Game Over", "Do you want to play again?")
        if answer:
            self.restart_game()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()


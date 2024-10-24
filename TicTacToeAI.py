import tkinter as tk
import numpy as np

# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = np.full((3, 3), EMPTY)
        self.current_player = PLAYER_X

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=EMPTY, font=("Arial", 36), width=6, height=3,
                                   command=lambda row=i, col=j: self.player_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def player_move(self, row, col):
        if self.board[row, col] == EMPTY:
            self.make_move(row, col, PLAYER_X)
            self.buttons[row][col].config(text=PLAYER_X)
            if not self.is_winner(PLAYER_X) and not self.is_full():
                self.master.after(500, self.ai_move)

    def ai_move(self):
        move = self.best_move()
        if move:
            self.make_move(move[0], move[1], PLAYER_O)
            self.buttons[move[0]][move[1]].config(text=PLAYER_O)
            if self.is_winner(PLAYER_O):
                self.end_game(f"Player {PLAYER_O} wins!")
            elif self.is_full():
                self.end_game("It's a draw!")

    def make_move(self, row, col, player):
        self.board[row, col] = player

    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i, j] == player for j in range(3)):
                return True
            if all(self.board[j, i] == player for j in range(3)):
                return True
        if all(self.board[i, i] == player for i in range(3)):
            return True
        if all(self.board[i, 2 - i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        return np.all(self.board != EMPTY)

    def best_move(self):
        best_score = -np.inf
        move = None
        for (i, j) in self.get_available_moves():
            self.make_move(i, j, PLAYER_O)
            score = self.minimax(False)
            self.board[i, j] = EMPTY  # Undo move
            if score > best_score:
                best_score = score
                move = (i, j)
        return move

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == EMPTY]

    def minimax(self, is_maximizing):
        if self.is_winner(PLAYER_O):
            return 1  # AI wins
        if self.is_winner(PLAYER_X):
            return -1  # Human wins
        if self.is_full():
            return 0  # Draw

        if is_maximizing:
            best_score = -np.inf
            for (i, j) in self.get_available_moves():
                self.make_move(i, j, PLAYER_O)
                score = self.minimax(False)
                self.board[i, j] = EMPTY  # Undo move
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = np.inf
            for (i, j) in self.get_available_moves():
                self.make_move(i, j, PLAYER_X)
                score = self.minimax(True)
                self.board[i, j] = EMPTY  # Undo move
                best_score = min(score, best_score)
            return best_score

    def end_game(self, message):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
        result_label = tk.Label(self.master, text=message, font=("Arial", 24))
        result_label.grid(row=3, column=0, columnspan=3)


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

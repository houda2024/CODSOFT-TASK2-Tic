import tkinter as tk
from tkinter import messagebox
from game import Game
from ai import minimax_alpha_beta  # Import your AI function

class TicTacToeUI:
    def __init__(self):
        self.game = Game()
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI")
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text='', width=10, height=3,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.game.make_move(row, col, self.game.human_player):
            self.buttons[row][col].config(text=self.game.human_player)
            winner = self.game.check_winner()
            if winner:
                self.handle_end_game(winner)
            else:
                self.ai_move()

    def ai_move(self):
        available_moves = self.game.get_available_moves()
        best_move = None
        best_value = -float('inf')
        for move in available_moves:
            self.game.make_move(move[0], move[1], self.game.ai_player)
            move_value = minimax_alpha_beta(self.game.board, 0, -float('inf'), float('inf'), False)
            self.game.board[move[0], move[1]] = None
            if move_value > best_value:
                best_value = move_value
                best_move = move
        if best_move:
            self.game.make_move(best_move[0], best_move[1], self.game.ai_player)
            self.buttons[best_move[0]][best_move[1]].config(text=self.game.ai_player)
            winner = self.game.check_winner()
            if winner:
                self.handle_end_game(winner)

    def handle_end_game(self, winner):
        if winner == 'Draw':
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def reset_game(self):
        self.game = Game()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')

    def run(self):
        self.window.mainloop()

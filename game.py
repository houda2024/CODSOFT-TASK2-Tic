import numpy as np

class Game:
    def __init__(self):
        self.board = np.array([[None] * 3 for _ in range(3)])
        self.current_player = 'X'  # Assume the player starts with 'X'
        self.ai_player = 'O'
        self.human_player = 'X'

    def make_move(self, row, col, player):
        if self.board[row, col] is None:
            self.board[row, col] = player
            return True
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for player in [self.human_player, self.ai_player]:
            if (any(np.all(self.board[i, :] == player) for i in range(3)) or
                any(np.all(self.board[:, i] == player) for i in range(3)) or
                np.all(np.diag(self.board) == player) or
                np.all(np.diag(np.fliplr(self.board)) == player)):
                return player

        # Check for a draw (no empty spaces)
        if not any(self.board[r, c] is None for r in range(3) for c in range(3)):
            return 'Draw'
        
        return None

    def get_available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r, c] is None]

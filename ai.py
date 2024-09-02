import numpy as np

def evaluate(board):
    for player in ['X', 'O']:
        for i in range(3):
            if np.all(board[i, :] == player):
                return 1 if player == 'O' else -1
            if np.all(board[:, i] == player):
                return 1 if player == 'O' else -1
        if np.all(np.diag(board) == player):
            return 1 if player == 'O' else -1
        if np.all(np.diag(np.fliplr(board)) == player):
            return 1 if player == 'O' else -1
    return 0  # Return 0 for draw or neutral position

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r, c] is None]

def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    winner = evaluate(board)  # Evaluate the board state
    if winner != 0:  # Return the evaluation if the game is over
        return winner
    if len(get_available_moves(board)) == 0:
        return 0  # Draw

    if is_maximizing:
        best = -float('inf')
        for move in get_available_moves(board):
            board[move[0], move[1]] = 'O'
            best = max(best, minimax_alpha_beta(board, depth + 1, alpha, beta, False))
            board[move[0], move[1]] = None
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for move in get_available_moves(board):
            board[move[0], move[1]] = 'X'
            best = min(best, minimax_alpha_beta(board, depth + 1, alpha, beta, True))
            board[move[0], move[1]] = None
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

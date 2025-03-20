from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize the game board
def init_board():
    return ['' for _ in range(9)]

# Check for win conditions
def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]
    return None

# Check if the board is full
def check_full(board):
    return all([cell != '' for cell in board])

# Minimax algorithm to choose the best move for the computer
def minimax(board, depth, is_maximizing):
    winner = check_win(board)
    
    # Base cases: Check if the game is over and return the score
    if winner == 'O':  # Computer wins
        return 1
    elif winner == 'X':  # Player wins
        return -1
    elif check_full(board):  # Tie
        return 0
    
    # Maximizing for 'O' (computer)
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    
    # Minimizing for 'X' (player)
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

# Choose the best move for the computer using Minimax
def computer_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json()
    board = data['board']
    player = data['player']
    
    # Player's move
    board[data['move']] = player
    winner = check_win(board)
    
    if not winner and not check_full(board):
        if data['mode'] == 'computer':
            # Computer's move
            comp_move = computer_move(board)
            board[comp_move] = 'O'
            winner = check_win(board)
    
    return jsonify({'board': board, 'winner': winner})

if __name__ == "__main__":
    app.run(debug=True)

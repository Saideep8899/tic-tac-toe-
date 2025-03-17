import math

# Initializing the board with empty spaces
def initialize_board():
    return [['-' for _ in range(3)] for _ in range(3)]

# Check if the current player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full (draw condition)
def is_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

# Evaluate the board for Minimax algorithm
def evaluate(board):
    if check_win(board, 'X'):
        return 1  # AI wins
    elif check_win(board, 'O'):
        return -1  # Human wins
    return 0  # Draw

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)

    # If the AI or human has won, return the score
    if score == 1 or score == -1:
        return score
    
    # If the board is full and there's no winner, it's a draw
    if is_full(board):
        return 0

    # Maximizing player (AI)
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'  # AI's move
                    best = max(best, minimax(board, depth + 1, alpha, beta, False))
                    board[i][j] = '-'  # Undo move
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best
    
    # Minimizing player (Human)
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'  # Human's move
                    best = min(best, minimax(board, depth + 1, alpha, beta, True))
                    board[i][j] = '-'  # Undo move
                    beta = min(beta, best)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best

# Find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'  # AI's move
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = '-'  # Undo move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Human vs AI Game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")

    while True:
        print_board(board)

        # Human's move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != '-':
            print("Cell is already taken. Try again.")
            continue

        board[row][col] = 'O'

        if check_win(board, 'O'):
            print_board(board)
            print("You win!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("AI wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
play_game()

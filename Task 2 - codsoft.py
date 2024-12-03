C:/Users/rajub/AppData/Local/Packages/Microsoft.ScreenSketch_8wekyb3d8bbwe/TempState/Recordings/20241130-1301-07.0540656.mp4import math

# Initialize the board
def create_board():
    return [' ' for _ in range(9)]  # A list of 9 spaces representing the board

# Display the board
def display_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Check for a winner
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check if the board is full (draw)
def is_draw(board):
    return ' ' not in board

# Get available moves
def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Minimax algorithm
def minimax(board, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):  # AI wins
        return 1
    if check_winner(board, 'X'):  # Human wins
        return -1
    if is_draw(board):  # Draw
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move] = 'O'
            eval = minimax(board, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move] = 'X'
            eval = minimax(board, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# AI makes a move
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move] = 'O'
        score = minimax(board, False, -math.inf, math.inf)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. The AI is 'O'.")
    display_board(board)

    while True:
        # Human move
        human_move = -1
        while human_move not in available_moves(board):
            try:
                human_move = int(input("Enter your move (0-8): "))
                if human_move not in available_moves(board):
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number (0-8).")
        board[human_move] = 'X'
        display_board(board)

        # Check if the human wins
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        ai_move_index = ai_move(board)
        board[ai_move_index] = 'O'
        display_board(board)

        # Check if the AI wins
        if check_winner(board, 'O'):
            print("The AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()

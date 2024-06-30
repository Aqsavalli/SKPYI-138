import numpy as np

# Initialize a 3x3x3 board with empty spaces
board = np.full((3, 3, 3), ' ')

def print_board(board):
    """ Print the current state of the board """
    for layer in range(3):
        print('Layer', layer + 1)
        for row in range(3):
            print('| ' + ' | '.join(board[layer, row, :]) + ' |')
            if row < 2:
                print('-' * 11)
        if layer < 2:
            print('+' * 11)

def check_winner(board, player):
    """ Check if the specified player has won """
    # Check layers
    for layer in range(3):
        # Check rows and columns
        for i in range(3):
            if (board[layer, i, :] == player).all() or \
               (board[layer, :, i] == player).all() or \
               (board[layer, :, :].diagonal() == player).all() or \
               (np.fliplr(board[layer, :, :]).diagonal() == player).all():
                return True
    
    # Check diagonals within layers
    for layer in range(3):
        if (board[layer].diagonal() == player).all() or \
           (np.fliplr(board[layer]).diagonal() == player).all():
            return True
    
    # Check vertical columns across layers
    for col in range(3):
        if (board[:, :, col].diagonal() == player).all() or \
           (np.fliplr(board[:, :, col]).diagonal() == player).all():
            return True
    
    # Check 3D diagonals
    if (board.diagonal(axis1=0, axis2=1) == player).all() or \
       (np.fliplr(board).diagonal(axis1=0, axis2=1) == player).all() or \
       (board.diagonal(axis1=1, axis2=2) == player).all() or \
       (np.fliplr(board).diagonal(axis1=1, axis2=2) == player).all() or \
       (board.diagonal(axis1=0, axis2=2) == player).all() or \
       (np.fliplr(board).diagonal(axis1=0, axis2=2) == player).all():
        return True
    
    return False

# Main game loop
current_player = 'X'
while True:
    print_board(board)
    print(f"Player {current_player}, it's your turn.")
    
    # Get player input
    while True:
        try:
            layer = int(input('Enter layer number (1-3): ')) - 1
            row = int(input('Enter row number (1-3): ')) - 1
            col = int(input('Enter column number (1-3): ')) - 1
            if layer in range(3) and row in range(3) and col in range(3) and board[layer, row, col] == ' ':
                board[layer, row, col] = current_player
                break
            else:
                print('Invalid move. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')
    
    # Check if the current player wins
    if check_winner(board, current_player):
        print_board(board)
        print(f"Congratulations! Player {current_player} wins!")
        break
    
    # Check if the board is full (tie condition)
    if np.all(board != ' '):
        print_board(board)
        print("It's a tie!")
        break
    
    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'
def initialize_board():
    """
    Initialize a 3x3x3 board for 3D Tic-Tac-Toe.
    """
    board = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    """
    Print the 3D Tic-Tac-Toe board.
    """
    for level in range(3):
        print(f"Level {level + 1}:")
        for row in range(3):
            print(" | ".join(board[level][row]))
            if row < 2:
                print("---------")
        if level < 2:
            print("#################")

def check_win(board, symbol):
    """
    Check if the specified symbol has won the game.
    """
    # Check rows and columns in each level
    for level in range(3):
        for i in range(3):
            if all(board[level][i][j] == symbol for j in range(3)):
                return True
            if all(board[level][j][i] == symbol for j in range(3)):
                return True
    
    # Check diagonals in each level
    for level in range(3):
        if all(board[level][i][i] == symbol for i in range(3)):
            return True
        if all(board[level][i][2 - i] == symbol for i in range(3)):
            return True
    
    # Check columns in different levels and diagonals across levels
    for i in range(3):
        if all(board[level][j][i] == symbol for level in range(3) for j in range(3)):
            return True
        if all(board[level][j][j] == symbol for level in range(3) for j in range(3) if j == i):
            return True
        if all(board[level][j][2 - j] == symbol for level in range(3) for j in range(3) if j == i):
            return True
    
    # Check diagonals across levels
    if all(board[level][i][i] == symbol for level in range(3) for i in range(3)):
        return True
    if all(board[level][i][2 - i] == symbol for level in range(3) for i in range(3)):
        return True

    return False

def is_board_full(board):
    """
    Check if the board is full.
    """
    for level in range(3):
        for row in range(3):
            for col in range(3):
                if board[level][row][col] is None:
                    return False
    return True

def is_valid_move(board, level, row, col):
    """
    Check if the move is valid.
    """
    return board[level][row][col] is None

def get_player_move(board, symbol):
    """
    Get valid player move coordinates.
    """
    while True:
        try:
            level = int(input(f"Enter level (1-3) for {symbol}: ")) - 1
            row = int(input(f"Enter row (1-3) for {symbol}: ")) - 1
            col = int(input(f"Enter column (1-3) for {symbol}: ")) - 1
            if level in range(3) and row in range(3) and col in range(3):
                if is_valid_move(board, level, row, col):
                    return level, row, col
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def play_game():
    """
    Main function to play the 3D Tic-Tac-Toe game.
    """
    board = initialize_board()
    current_symbol = 'X'

    while True:
        print_board(board)
        print(f"Player {current_symbol}'s turn.")
        level, row, col = get_player_move(board, current_symbol)
        board[level][row][col] = current_symbol

        if check_win(board, current_symbol):
            print_board(board)
            print(f"Player {current_symbol} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_symbol = 'O' if current_symbol == 'X' else 'X'

if __name__ == "__main__":
    play_game()

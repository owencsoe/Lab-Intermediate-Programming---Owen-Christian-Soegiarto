def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def get_cell_position():
    while True:
        try:
            position = input("Enter cell position (TopLeft = tl, TopCenter= tc, TopRight = tr, etc. =  ")
            
            positions = {
                'tl': (0, 0),
                'tc': (0, 1),
                'tr': (0, 2),
                'ml': (1, 0),
                'mc': (1, 1),
                'mr': (1, 2),
                'bl': (2, 0),
                'bc': (2, 1),
                'br': (2, 2)
            }
            return positions[position]
        except KeyError:
            print("Invalid position. Please enter a valid position.")


def tic_tac_toe():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        while True:
            print_board(board)

            # Get player move
            row, col = get_cell_position()

            # Check if the chosen cell is empty
            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print("Cell already taken. Try again.")
                continue

            # Check for a winner or a tie
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break


if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    tic_tac_toe()

# Initialize the game board as a list of 9 empty spaces
board = [" " for i in range(9)]

# Function to print the current state of the game board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle a player's move
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(icon))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("The space is taken!")

# Function to check if a player has won the game
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Main game loop
while True:
    # Print the current state of the board
    print_board()
    # Player X's turn
    player_move("X")
    # Check if Player X has won
    if is_victory("X"):
        print("X wins! Congratulations!")
        break  # End the game if X wins
    # Player O's turn
    player_move("O")
    # Check if Player O has won
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break  # End the game if O wins

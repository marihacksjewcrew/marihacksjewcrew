# Print the board
def print_board(board):
    print("\nLet's play tic tac toe!\n")
    print(" %s | %s | %s "   % (board[0],board[1],board[2]))
    print(" %s | %s | %s "   % (board[3],board[4],board[5]))
    print(" %s | %s | %s \n" % (board[6],board[7],board[8]))

# Check if there is a winner

# Horizontally
def checkHorizontal(board):
    for i in range(0,7,3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return True

# Vertically
def checkVertical(board):
    for i in range(0,3,1):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return True

# Diagonally
def checkDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != ' ' or (board[2] == board[4] == board[6] and board[2] != ' '):
        return True

# Check if there is a winner using the functions from above
def isWinner(board):
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        return True

# Initialize board array
board = [' ']*9
player = 'X'

# Preliminary print
print_board(board)

while True:
    # Get user input
    x = input("Give me a number from 1-9: ")
    x = int(x)

    # Put X into board
    board[x-1] = player
    print_board(board)
    
    if isWinner(board):
        print('You win!')
	break
    
    # Check for tie
    elif ' ' not in board:
        print('Tie game.')
        break
    
    # Switch players
    else:
	if player == 'X':
	    player = 'O'
        else:
            player = 'X'

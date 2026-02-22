# Changed to spaces so the board doesn't look squished
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def display():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def turn(player):
    print(f"Player {player} Turn")
    
    # NEW: Keep asking until they pick an empty spot
    valid_move = False
    while not valid_move:
        pos = input("Enter any number between 1-9: ")
        pos = int(pos) - 1
        
        # Check if the spot is a space (empty)
        if board[pos] == " ":
            board[pos] = player
            valid_move = True  # This breaks the loop
        else:
            print("That spot is already taken! Try again.")

# NEW: Pass 'player' into the function so we check for exact matches
def checkwin(player):
    # ROW
    if board[0] == board[1] == board[2] == player: return True
    if board[3] == board[4] == board[5] == player: return True
    if board[6] == board[7] == board[8] == player: return True

    # COLUMN
    if board[0] == board[3] == board[6] == player: return True
    if board[1] == board[4] == board[7] == player: return True
    if board[2] == board[5] == board[8] == player: return True

    # DIAGONAL
    if board[0] == board[4] == board[8] == player: return True
    if board[2] == board[4] == board[6] == player: return True
    
    return False

current_player = "X"
game_is_running = True
turn_count = 0

print("-----Welcome to tic tac toe------")
display()

while game_is_running:
    turn(current_player)
    display()

    # NEW: We pass the current_player to the checkwin function here
    if checkwin(current_player):
        print(f"Player {current_player} Wins!")
        game_is_running = False

    turn_count += 1

    if turn_count == 9 and game_is_running:
        print("It is a tie")
        game_is_running = False

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
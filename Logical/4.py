board = ["", "", "", "", "", "", "", "", ""]

def display():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def turn(player):
    print(f"Player {player} Turn")
    pos = input("Enter any number between 1-9 :")
    pos = int(pos) - 1
    board[pos] = player

def checkwin():
    # ROW
    if board[0] == board[1] == board[2] != "": return True
    if board[3] == board[4] == board[5] != "": return True
    if board[6] == board[7] == board[8] != "": return True

    # COLUMN
    if board[0] == board[3] == board[6] != "": return True
    if board[1] == board[4] == board[7] != "": return True
    if board[2] == board[5] == board[8] != "": return True

    # DIAGONAL
    if board[0] == board[4] == board[8] != "": return True
    if board[2] == board[4] == board[6] != "": return True
    
    return False

current_player = "X"
game_is_running = True
turn_count = 0

print("-----Welcome to tic tac toe------")
display()

while game_is_running:
    turn(current_player)
    display()

    if checkwin():
        print(f"Player {current_player} Wins")
        game_is_running = False

    turn_count +=1

    if turn_count ==9 and game_is_running:
        print("It is a tie")
        game_is_running = False

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

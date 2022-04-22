#--TURN HANDLER FUNCTION----------------------#
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        
        while position not in ["1","2","3","4","5","6","7","8","9",]: #Input validation for player 1
            position = input(player + " Choose a position from 1-9: ") 
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Spot already filled.")
    board[position] = player
    display_board()

#--FUNCTION TO SWAP PLAYER TURNS---------#
def flip_player():
    global current_player
    
    if current_player == "x": #if current player was x, change to o
        current_player = "o"
    elif current_player == "o": #if current player was o, change to x
        current_player = "x"
    return
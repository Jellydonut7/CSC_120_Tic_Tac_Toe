#--THIS CHECKS IF SOMEONE HAS WON OR THE GAME ENDS IN A TIE--#
def check_if_game_over():
    check_if_win()
    check_if_tie()

#--THIS INITIATES ROW, COLUMN, AND DIAGONAL SPACE WINNERS--#
def check_if_win():
    global winner 
    
    row_winner = check_rows() #Determins if game won by 3 in a row
    
    column_winner = check_columns() #Determins if game won by 3 in a column or up and down
    
    diagonal_winner = check_diagonals() #Determins if game won by 3 in a diagonal direction
    if row_winner:
       winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner: 
        winner = diagonal_winner
    else:
        winner = None
    return

#--ROW CHECK FOR A WINNER---------------------------#
def check_rows():
    global game_still_going
    
    row_1 = board[0] == board[1] ==board[2] != "-" #Check rows for same values
    row_2 = board[3] == board[4] ==board[5] != "-"
    row_3 = board[6] == board[7] ==board[8] != "-"
    if row_1 or row_2 or row_3: #if any row matches, declare win
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

#--COLUMN CHECK FOR A WINNER-----------------------#
def check_columns():
    global game_still_going
    
    column_1 = board[0] == board[3] ==board[6] != "-" #Check column for same values
    column_2 = board[1] == board[4] ==board[7] != "-"
    column_3 = board[2] == board[5] ==board[8] != "-"
    if column_1 or column_2 or column_3: #if any column matches, declare win
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

#--DIAGONAL CHECK FOR A WINNER---------------------#
def check_diagonals():
    global game_still_going
    
    diagonal_1 = board[0] == board[4] ==board[8] != "-" #Check diagonal for same values
    diagonal_2 = board[2] == board[4] ==board[6] != "-"
    if diagonal_1 or diagonal_2: #if any diagonal matches, declare win
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

#--BOARD CHECK FOR A TIE-----------------#
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False #Ends game in a tie
    return

#--PRINTS OUT THE WINNER OR A TIE------------#
    if winner == "x":  
        print("Player 1 " + winner + " won!")
    elif winner == "o":
        print("Player 2 " + winner + " won!")
    elif winner == None:
        print("It's a tie! :(")
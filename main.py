import tkinter #Libs
import random 

def next_turn(row, col): #called after every btn click
    global player
    if check_if_empty(row,col) :
        if player == "'O'" :
            game_btns[row][col].config(textvariable=varbtnO)
            player = "'X'"
        else :
            game_btns[row][col].config(textvariable=varbtnX)
            player = "'O'"
    v = check_winner()
    if v != None :
        if v != "DRAW":
            titlevar.set(v + " wins")
            btntitlevar.set("new game")
        else :
            titlevar.set("DRAW")
            btntitlevar.set("new game")

def check_winner():
    board = get_board()

    # Check rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != " ":
            return board[r][0]

    # Check columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != " ":
            return board[0][c]

    # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    # Check anti diagonal
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check draw (no spaces left)
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return None  # game not finished

    return "DRAW"

def check_if_empty(row, col):
    if check_winner() != None : # return 0 always if the game is done
        return 0
    var_name = game_btns[row][col].cget("textvariable")
    value = window.getvar(var_name)                       # "X" or "O" or " "
    return value == " "  

def start_new_game():
    try:
        # Try to access game_btns and reset if it's already defined
        if 'game_btns' in globals():
            global game_btns
            for row in range(3):
                for col in range(3):
                    game_btns[row][col].config(textvariable=emptyvar)  # Reset button text
        else :
            game_btns = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]
    finally :
        player = random.choice(["X","O"])
        titlevar.set(player+" first")
        btntitlevar.set("restart")
    return player,game_btns

def get_board():
    board = [[" " for _ in range(3)] for _ in range(3)]

    for r in range(3):
        for c in range(3):
            var_name = game_btns[r][c].cget("textvariable")
            board[r][c] = window.getvar(var_name)
    return board
    
#defining the window object
window = tkinter.Tk()
window.title("xo game ")
window.minsize(500,500)

#Stings
titlevar = tkinter.StringVar()
varbtnX = tkinter.StringVar()
varbtnO = tkinter.StringVar()
btntitlevar = tkinter.StringVar()
emptyvar = tkinter.StringVar()
varbtnX.set("X")
varbtnO.set("O")
emptyvar.set(" ")
btntitlevar.set("restart")

player,game_btns = start_new_game()
#Label 
label = tkinter.Label (textvariable=titlevar, font=('consolas', 40))
label.pack(side="top")

#Button
restart_btn =tkinter.Button (textvariable=btntitlevar, font=('consoals', 20) ,command=start_new_game)
restart_btn.pack(side="bottom")

#Grid
btns_fram = tkinter.Frame(window)
btns_fram.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = tkinter.Button(btns_fram, textvariable=emptyvar, font=('consolas', 50), width=4, heigh=1,
        command=lambda row=row , col=col : next_turn(row, col)) 
        game_btns[row][col].grid(row=row,column=col)


    
window.mainloop()

  
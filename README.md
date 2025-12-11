1.the project: "X" and "O" (tic-tac-toe)
2.Introduction:
this project is one of the best ideal projects for starting programming with python 
3.Main goal:
the main goal of this project is made famous simple game for 2 players (X,O)
4.The code:
The code successfully creates a 3*3 grid where two players, 'X' and 'O', can take turns. It handles the game logic, win conditions, draws, and provides a restart button
4.1)Initialization and Setup:
-tkinter is imported for the GUI
-random is used to decide which player goes first 
-window is defined with a title (xo game )
-titlevar holds the text for the status label ( ex : "DRAW ")
-varbtnX,varbtnO,emptyvar used to the boutton contents to "x","o" or empty ("")
-btntitlevar holds the text for the restart button 
4.2)game state management:
-star_new_game():
>it resets the bottons on the board by setting theair textvariables back to emptyvar ("")
>it used random.choice(["X","O"]) to select the starting player
>It updates the title label (titlevar) to announce who goes first
>It updates the restart button text (btntitlevar)
>It returns the starting player and the initialized game_btns list
-get_board():
>This function reads the current state of the 3x3 button grid
>It iterates through all buttons, retrieves the value of their associated StringVar, and returns the board as a 2D list (e.g., [['X', ' ', 'O'], [...], ...])
-cheak_if_empty(row,col)
>Checks two conditions before allowing a move:
If a winner or draw has already been determined (check_winner() != None), it returns 0 (False)
It checks if the selected button's value is currently " " (empty)
4.3)Game logic:
-next_turn(row, col): This is the core function called when a player clicks a button
>Check Validity: It first calls check_if_empty(),If the move is valid
>Place Mark: It sets the button's textvariable to "O" or "X" based on the current player
>Switch Player: It then toggles the player variable (EX:if it was 'O', it becomes 'X')
>Check Game End: It calls check_winner()
>Handle Game End: If check_winner() returns a winner ('X' or 'O') or "DRAW", it updates the titlevar and sets the btntitlevar to "new game"
-cheak_wimmer:
>It first retrieves the current board state using get_board()
>It checks for a win condition across rows, columns, the main diagonal (top-left to bottom-right), and the anti-diagonal (top-right to bottom-left). If a win is found, it returns the winning mark ('X' or 'O')
>If no winning condition is met, it checks if there are any empty spaces (" ") left. If there are, it returns None (game not finished)
>If all spaces are filled and no winner is found, it returns "DRAW"
4.4)layout:
>Label and Button: The titlevar label is packed at the top, and the restart_btn is packed at the bottom
>Board Frame: A tkinter.Frame (btns_fram) is used to group the 9 game buttons, which helps organize the layout
>Button Grid: A nested loop creates the 9 buttons (game_btns[row][col]) and places them using the grid() layout manager in a 3x3 formation
>The command attribute uses a lambda function to pass the specific button's row and col index to the next_turn function when clicked
4.5)Execution:
>window.mainloop(): This is the final line that starts the Tkinter event loop, allowing the GUI to run and respond to user input
5)some bugs we founds soluition for its :
>the restart button is not
>the game allows players to continue placing "X" or "O" after the game end
>he game allows players to place an X and O in the same spot

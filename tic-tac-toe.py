#set up a blank board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

#main function that guides game flow
def ready():
    printInstructions()
    printInstructionBoard()
    #add some space after instructions
    print("\n<<<<------------------------->>>>")
    game()

#print the game instructions
def printInstructions():
    print("")
    print("")
    print("Welcome to tic tac toe!")
    print("The board is arranged 1-9, left to right as shown below.")
    print("Make your first move by simply typing the number for the position you would like to choose.")
    print("Then player two goes next.")
    print("\n<<<<------------------------->>>>\n")

#print the board along with an outline of the board with the 1-9 positions
def printInstructionBoard():
    print(board[0] + " | " + board[1] + " | " + board[2] + "\t    \t" + "1" + " | " + "2" + " | " + "3")
    print("---------" + "\t    \t" + "---------")
    print(board[3] + " | " + board[4] + " | " + board[5] + "\t>>>>\t" + "4" + " | " + "5" + " | " + "6")
    print("---------" + "\t    \t" + "---------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\t    \t" + "7" + " | " + "8" + " | " + "9")

#function to print the board
def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#main function for the game itself
def game():
    currentPlayer = "X"
    currentGame = True
    move = 0
    usedMoves = []
    inputValid = False
    
    #loops until game is won
    while currentGame:
        #loops until user enters a number 1-9
        while not inputValid:
            move = None
            #loops until user enters a 1-9 int
            while move is None:
                print("")
                print("Player " + currentPlayer + ": ")
                try:
                    move = int(input())
                    print("")
                except ValueError:
                    print("Enter a number between 1 and 9.")
            #need to check if number is 1-9
            if move >= 1 and move <= 9:
                #need to ensure the choosen move has not already been taken                   
                if move not in usedMoves:
                    inputValid = True
                    continue
                else:
                    print("This position is already used.")
                    continue
            else:
                print("Enter a number between 1 and 9.")
                continue
        #make the move and update the board onscreen
        board[move - 1] = currentPlayer
        printBoard()
        #is player's move the winning move? 
        currentGame = checkBoard(currentPlayer)
        #swap to the next player
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"
        #keep track of the move just made
        usedMoves.append(move)
        #prepare for next input validation
        inputValid = False
        if len(usedMoves) == 9:
            currentGame = False
            print("")
            print("It's a draw!")
            print("")

#check board to see if the game has been won. takes the most recent player as input
#and if there is a winning move, that player wins. returns whether the game should keep
#going or not
def checkBoard(player):
    if (board[0] == player) and (board[1] == player) and (board[2] == player):
        win(player)
        return False
    elif (board[3] == player) and (board[4] == player) and (board[5] == player):
        win(player)
        return False
    elif (board[6] == player) and (board[7] == player) and (board[8] == player):
        win(player)
        return False
    elif (board[0] == player) and (board[3] == player) and (board[6] == player):
        win(player)
        return False
    elif (board[1] == player) and (board[4] == player) and (board[7] == player):
        win(player)
        return False
    elif (board[2] == player) and (board[5] == player) and (board[8] == player):
        win(player)
        return False
    elif (board[0] == player) and (board[4] == player) and (board[8] == player):
        win(player)
        return False
    elif (board[2] == player) and (board[4] == player) and (board[6] == player):
        win(player)
        return False
    else:
        return True

#print out the winning message
def win(player):
    print("")
    print("Player {player} won!".format(player=player))
    print("")

#run the game
ready()
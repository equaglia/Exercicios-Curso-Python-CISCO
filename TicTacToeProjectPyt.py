def DisplayBoard(board):
    print(
        """
        +-------+-------+-------+
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |       |       |       |
        +-------+-------+-------+
        """.format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]))
    return
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

def EnterMove(board):
    n = 0
    while int(n) <= 0 or int(n) >= 10:
        n = input("Enter your move: ")
#        n = int(input("Enter your move: "))
#        if not(type(n) == int):
#            n = 0
#            continue
        for line in range(3):
            for column in range(3):
                if n == board[line][column]:
                    board[line][column] = "O"
    return
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    freeSquares = []
    for line in range(3):
        for column in range(3):
            square = board[line][column]
            if square != "X" and square != "O":
                freeSquares.append((line, column))
    return freeSquares
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):
    if board[0][0] == board[0][1] == board[0][2] == sign \
    or board[1][0] == board[1][1] == board[1][2] == sign \
    or board[2][0] == board[2][1] == board[2][2] == sign \
    or board[0][0] == board[1][0] == board[2][0] == sign \
    or board[0][1] == board[1][1] == board[2][1] == sign \
    or board[0][2] == board[1][2] == board[2][2] == sign \
    or board[0][0] == board[1][1] == board[2][2] == sign \
    or board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    from random import randrange

    computerMove = randrange(len(freeSquares))
    line, column = freeSquares[computerMove]
    board[line][column] = "X"
    return
#
# the function draws the computer's move and updates the board
#

board = [["1","2","3"],["4","X","6"],["7","8","9"]]
freeSquares = MakeListOfFreeFields(board)
winX = winO = tie = False
DisplayBoard(board)
while not winX and not winO and not tie:
    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board, "O"):
        winO = True
        print("You won!")
        continue
    freeSquares = MakeListOfFreeFields(board)
    DrawMove(board)
    DisplayBoard(board)
    if VictoryFor(board, "X"):
        winX = True
        print("Computer won!")
        continue
    freeSquares = MakeListOfFreeFields(board)
    if len(freeSquares) == 0:
        tie = True
        print("Game ends with a tie!")

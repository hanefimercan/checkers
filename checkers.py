from common import *
from time import sleep
from validPathsKing import bestPathsForTurn

def initializeBoard():
    board = []
    for _ in range(rowCount):
        row = []
        for _ in range(colCount):
            row.append(emptyCell)
        board.append(row)
        
    remainder = 1  # first row, it will be zero, second row, it will be one, so on so forth
    for r in range(rowCount):   # first 3 rows
        if r < 3:
            for c in range(colCount):
                if c % 2 == remainder:
                    board[r][c] = "o"
        elif r >= rowCount - 3:
            for c in range(colCount):
                if c % 2 == remainder:
                    board[r][c] = "x"
        remainder = 1 - remainder
    return board

def printBoard(board):
    print()
    # draw horizontal coordinates on board 
    emptyLength1 = '    '
    emptyLength2 = '  '
    print(emptyLength1, end='')
    for c in range(colCount):
        print(emptyLength2 + str(c) + ' ', end='')
    print()

    line = ''.join(['-' for x in range(colCount * 4 + 1)])
    for i in range(rowCount):
        print(emptyLength1 + line)
        print(' ' + str(i) + '  ', end='')
        for j in board[i]:
            cell = j
            if j == emptyCell:
                cell = ' '
            print('| ' + cell + ' ', end='')
        print('|')
    print(emptyLength1 + line)
    print()
    print()
          
def playerTurn(player, player1, player2):
    piece = None
    if player == player1:
        player = player2
        piece = 'o'
    else:
        player = player1
        piece = 'x'
    return player, piece
                                  
def isGameOver(board):
    # only 2 kings on the board?
    xCount, oCount = getNoOfPiecesOnBoard(board)
    if xCount == 0 or oCount == 0:
        return True
    return False
    
def printMessages(player, path):
    print(player.name + " played: " + str(path) + "\n")
    input("Press any key to continue\n\n")
    print ("*****************************************************")
    print ("*****************************************************")
    print ("\n\n") 
    
def playGame(player1, player2):
    board = initializeBoard()
    printBoard(board)
    player = player2
    while not isGameOver(board):
        player, turn = playerTurn(player, player1, player2)
        print(player.name + " (" + turn + ") is playing\n")
        validPaths = bestPathsForTurn(board, turn)
        path = player.play(board, validPaths, turn)
        updateBoard(board, path)
        printBoard(board)
        printMessages(player, path)
















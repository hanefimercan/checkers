from common import *
from time import sleep
from validPathsKing import bestPathsForTurn, countNoOfRivalsInDirection

printInfos = True


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
    if not printInfos:
        return
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
                                  
def isGameOver(board, noMoveCount):
    # only 2 kings on the board?
    if noMoveCount == 2:
        return True
    xCount, oCount = getNoOfPiecesOnBoard(board)
    if xCount == 0 or oCount == 0:
        return True
    return False
    
def printMessages(player, path):
    if not printInfos:
        return
    print(player.name + " played: " + str(path) + "\n")
    input("Press any key to continue\n\n")
    print ("*****************************************************")
    print ("*****************************************************")
    print ("\n\n") 
    
def whoIsWinner(board, player, turn):
    xCount, yCount = getNoOfPiecesOnBoard(board)
    winner = "tie"
    if (turn == 'x' and yCount == 0) or (turn == 'o' and xCount == 0):
        if printInfos:
            print("\n\n" + player.name.capitalize() + " (" + turn + ") is the winner!.\n\n")
        winner = turn
    else:
        if printInfos:
            print("\n\nThere is no winner, it is tie game.\n\n")
    return winner
        
def playGame(player1, player2):
    board = initializeBoard()
    printBoard(board)
    player = player2
    noMoveCount = 0  # if no move can be played both for x and o, then it is a tie game
    while not isGameOver(board, noMoveCount):
        player, turn = playerTurn(player, player1, player2)
        if printInfos:
            print(player.name + " (" + turn + ") is playing\n")
        validPaths = bestPathsForTurn(board, turn)
        if len(validPaths) == 0:
            noMoveCount += 1
        else:
            noMoveCount = 0
        path = player.play(board, validPaths, turn)
        updateBoard(board, path)
        printBoard(board)
        printMessages(player, path)
    winner = whoIsWinner(board, player, turn)
    return winner














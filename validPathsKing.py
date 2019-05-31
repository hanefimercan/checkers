from common import *
from random import shuffle

def getJumpPathsForTwoLengthPaths(board, paths):
    # Eger en iyi path uzunlugu 2 ise, yani sadece bir move yapiliyorsa;
    # Jump yapan (karsi taraftan tas alan) bir hareket secilmeli
    # Eger oyle bir hareket yoksa, diger tum hareketler valid

    newPaths = []
    for path in paths:
        if len(path) != 2:
            raise SystemError("Sth is wrong")
        pos1 = path[0]
        pos2 = path[1]
        direction = getdirection(pos1, pos2)
        length = abs(pos1[0] - pos2[0]) 
        noOfrival = countNoOfRivalsInDirection(board, pos1, direction , length)
        if noOfrival == 1:
            newPaths.append(path)
        elif noOfrival > 1:
            raise SystemError('Sth is wrong 3')
    if not newPaths:  # if there is no path with jump
        return paths
    return newPaths

def createNewNode(piece, pos, board, noDirs = False, currentPath = []):
    if noDirs:
        newDirs = []
    elif isKing(piece):  # king check
        newDirs = [1,2,3,4]
    elif piece == 'x':
        newDirs = [1,2]
    elif piece == 'o':
        newDirs = [3,4]
    else:
        raise SystemError("Sth is wrong 2")
    currentPath.append(pos)
    boardNew = deepCopyBoard(board)
    updateBoard(boardNew, currentPath[-2:])
    node = {'dirs':newDirs, 'path':currentPath, 'board': boardNew}
    return node

def convert2King(board, player):
    if player == 'o':
        board[-1] = [e.replace('O','o') for e in board[-1]]
    if player == 'x':
        board[0] = [e.replace('X','X') for e in board[0]]
    return board

def getNextPosition(pos, dir, length):
    '''RETURNS THE COORDINATES OF A GIVEN STRIDE DIRECTION AND LENGTH'''
    # directions 1:left-up, 2:right-up, 3:right-down, 4:left-down
    (row,col) = pos
    if dir == 1:
        row -= length
        col -= length
    elif dir == 2:
        row -= length
        col += length
    elif dir == 3:
        row += length
        col += length
    elif dir == 4:
        row += length
        col -= length
    return (row, col)

def countNoOfRivalsInDirection(board, pos, dir, length):
    noOfRivalPiece = 0
    piece = board[pos[0]][pos[1]]
    for lng in range(1,length):
        rowNext, colNext = getNextPosition(pos, dir, lng)
        if isSamePlayerPiece(piece, board, rowNext, colNext):
            noOfRivalPiece = 1000  # jump is not possible
            break
        elif not isEmpty(board, rowNext, colNext): 
            noOfRivalPiece += 1
    return noOfRivalPiece

def isNextNodeValid(board, pos, dir, piece, length, path):
    '''CHECK IF NEXT NODE IS VALID, GIVEN ITS DIRECTION AND STRIDE LENGTH
       IF VALID, RETURNS THE NODE. IF NOT, RETURNS NONE'''
    nextNode = None
    rowNext, colNext = getNextPosition(pos, dir, length)
    noOfRivalPiece = 0
    rowMax = len(board)
    colMax = len(board[0])
    if rowNext < rowMax and rowNext >= 0 and colNext < colMax and colNext >= 0:
        if isEmpty(board, rowNext, colNext):
            nextPos = (rowNext,colNext)
            noOfRivalPiece = countNoOfRivalsInDirection(board, pos, dir, length)
            if noOfRivalPiece == 1:
                nextNode = createNewNode(piece, nextPos, board, currentPath=path)
            elif noOfRivalPiece == 0 and len(path) == 1: # no move has been done yet
                if isKing(piece) or length == 1: # non-king can move only 1 length
                    nextNode = createNewNode(piece, nextPos, board, noDirs = True, currentPath=path)
    return nextNode

def possibleNextNodesForPieceDirections(board, piece, pos, dir, path):
    '''RETURNS MOVE OR JUMP FOR A GIVEN DIRECTION'''
    # is piece a king? TODO
    nodes = []
    if isKing(piece):
        moveLengths = [x for x in range(1, min(rowCount, colCount))]  
    else:
        moveLengths = [1, 2]

    for length in moveLengths:
        newNode = isNextNodeValid(board, pos, dir, piece, length, path[:])
        if newNode:
            nodes.append(newNode) 
    return nodes

def validPathsForPiece(board, pos):
    '''GENERATE ALL POSSIBLE PATHS FOR A GIVEN PIECE POSITION'''
    piece = board[pos[0]][pos[1]]
    paths = [] # list of 2 element lists
    node = createNewNode(piece, pos, board, currentPath=[])  # initial position,  first node of paths
    stack = [node] # list of dictionarie(s) 
    # build a stack if there is a possible path and obtain all the moves
    while stack:
        topObj = stack.pop()
        
        pos = topObj['path'][-1]
        # for each direction search for possible paths
        newNodesFound = False
        for dir in topObj['dirs']:
            nextNodes = possibleNextNodesForPieceDirections(topObj['board'], piece, pos, dir, topObj['path']) # a dictionary (node)
            for nd in nextNodes:
                newNodesFound = True
                stack.append(nd)
        # if no path is generated go back one move and generate moves up to that point
        if not newNodesFound:
            paths.append(topObj['path'])
    return paths

def bestPathsForTurn(board, player):
    '''RETURN THE POSSIBLE LONGEST PATHS FOR THIS TURN'''
    # iterate over each position on board
    paths = []
    allPositions = [(i, j) for i in range(len(board)) for j in range(len(board[i]))]
    for (i, j) in allPositions: 
        # if a piece is found for that position return a list of available paths
        if board[i][j].lower() == player:
            pos = (i, j)
            paths += validPathsForPiece(board, pos)
            
    #return paths # for testing purposes
    longPathLength = -1
    for path in paths:
        # if there exists a path then return the longest one for that piece
        if len(path) > longPathLength:
            longPathLength = len(path)
    longestPaths = []
    for path in paths:
        # if there exists a path then return the longest one for that piece
        if len(path) == longPathLength:
            longestPaths.append(tuple(path))

    if longPathLength == 2: # Choose the path with jump if exists when there is only one move
        longestPaths = getJumpPathsForTwoLengthPaths(board, longestPaths)
    shuffle(longestPaths)
    return longestPaths


#TEST for validPathsForPiece()


"""

board1 = [['-','o','-','o','-','o'],
          ['-','-','o','-','-','-'],
          ['-','-','-','-','-','o'],
          ['o','-','o','-','-','-'],
          ['-','-','-','-','-','x'],
          ['-','-','x','-','x','-'],
          ['-','x','-','x','-','x']]



paths = bestPathsForTurn(board1, "x")
for p in paths:
    print(p)

pos = (2,1)
paths = validPathsForPiece(board2, pos)
for p in paths:
    print(p)
"""

#board3 = [[-,o,-,o,-,o],
#         [o,-,-,-,o,-],
#         [-,o,-,o,-,o],
#         [-,-,-,-,-,-],
#         [-,o,-,o,-,o],
#         [-,-,-,-,-,-],
#         [-,o,-,o,-,o],
#         [x,-,x,-,x,-],



#QUESTION1
# [x[:] for x in [['|-|']*6]*8]
#    for i in board:
#    for j in i:
#        print(j, end='')
#    print()
# A = [[]]*4
# [[], [], [], []]
# B = [[]*4]
# [[]]
# A[0].append(1) = A[1].append(1) = A[2].append(1).....
# [[1], [1], [1], [1]]


#print ("DONE")
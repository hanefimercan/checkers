

emptyCell= "-"
rowCount = 7  # row count can not be smaller than 8
colCount = 6

def printPaths(paths):
    for path in paths:
        print(path)

def isKing(piece):
    return piece != piece.lower()

def isEmpty(board, row, col):
    return board[row][col] == emptyCell

def isSamePlayerPiece(piece, board, row, col):
    return board[row][col].lower() == piece.lower()

def getNoOfPiecesOnBoard(board):
    xCount = 0
    oCount = 0
    for row in board:
        for cell in row:
            if cell.lower() == 'x':
                xCount += 1
            elif cell.lower() == 'o':
                oCount += 1
    return xCount, oCount
  
def updateBoard(board, path):
    length = len(path)
    firstPos = path[0]
    piece = board[firstPos[0]][firstPos[1]]
    for k in range(length-1):
        row1,col1 = path[k]
        row2,col2 = path[k+1]
        ri = ci = 1
        if row1 > row2:
            ri = -1
        if col1 > col2:
            ci = -1
        length = abs(row1 - row2)
        for i in range(length):  # make current cell empty, too
            rowNext = row1 + (i * ri)
            colNext = col1 + (i * ci)    
            board[rowNext][colNext] = emptyCell
        board[row2][col2] = piece
        if (row2 == rowCount - 1 and piece == 'o') or (row2 == 0 and piece == 'x'):
            board[row2][col2] = board[row2][col2].upper()

def deepCopyBoard(board):
    boardNew = [list(x) for x in board[:]]  # deep copy
    return boardNew






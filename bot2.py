
import random
from common import deepCopyBoard, updateBoard, printPaths

name = 'superior_bot'

def countPiece(board, piece):
    count = 0
    for row in board:
        for p in row:
            if p == piece:
                count += 1
    return count

def calculateGain(board, piece):
    xNormalCount = countPiece(board, 'x')
    oNormalCount = countPiece(board, 'o')
    xKingCount = countPiece(board, 'X')
    oKingCount = countPiece(board, 'O')
    xTotal = xNormalCount + 3 * xKingCount
    oTotal = oNormalCount + 3 * oKingCount
    gain = xTotal - oTotal
    if piece.lower() == 'o':
        gain = -gain
    return gain

def play(board, paths, piece):
    #printPaths(paths)
    gains = {}
    for path in paths:
        boardCopy = deepCopyBoard(board)
        updateBoard(boardCopy, path)
        gains[path] = calculateGain(boardCopy, piece)
    
    maxGain = -10000000
    bestPath = []
    for path in gains:
        gain = gains[path]
        if gain > maxGain:
            maxGain = gain
            bestPath = path

    return bestPath















name = "Hanefi"

def isInteger(x):
    ints = [str(x) for x in range(10)]
    return str(x) in ints

def enterMove():
    length = None
    while not isInteger(length):
        length = input('Enter no of moves (including the piece pos) ')
    length = int(length)
    positions = []
    for i in range(length):
        pos = str(input('Enter position ' + str(i) + ': '))
        pos = tuple([int(x) for x in pos.split(",")])
        positions.append(pos)
    positions = tuple(positions)
    return positions

def play(board, paths, piece):
    path = []
    isValid = False
    while not isValid:
        path = enterMove()
        if path in paths:
            isValid = True
        else:
            print('You can not play this move.')
            print('Either it is not a valid move, or there is a better move.')
            print('')
    return path
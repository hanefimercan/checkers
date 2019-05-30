


from random import choice

# random bot
# chooses a random move and plays it

name = 'random_bot'

def play(board, paths, piece):
    path = choice(paths)
    return path

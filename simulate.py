
import bot1, bot1_copy
import bot2
import realPlayer
import checkers


def printWinner(winner, winCounts, p1, p2, repeat):
    if winner == 'tie':
        winCounts['tie'] += 1 
        print("Repeat-" + str(repeat+1) + " is a tie game.")
    elif winner == 'x':
        winCounts[p1] += 1 
        print("Repeat-" + str(repeat+1) + " winner is " + p1.name + ".") 
    elif winner == 'o':
        winCounts[p2] += 1 
        print("Repeat-" + str(repeat+1) + " winner is " + p1.name+ ".") 
    else:
        raise SystemError('Sth is wrong 4')

def simulate(player1, player2, repeatCount):
    if repeatCount < 1:
        raise SystemError("This can not happen")
    if repeatCount > 1:
        checkers.printInfos = False
    winCounts = {player1: 0, player2: 0, 'tie': 0}
    tieGame = 0
    p1 = player1
    p2 = player2  
    for repeat in range(repeatCount):
        checkers.testBool = True
        winner = checkers.playGame(p1, p2)
        printWinner(winner, winCounts, p1, p2, repeat)
        p1, p2 = p2, p1
        
    
    print("\n")
    print("Win counts:")
    print(player1.name + ": " +str(winCounts[player1])) 
    print(player2.name + ": " +str(winCounts[player2])) 
    print("Tie game: " + str(tieGame)) 
    print("\n\n")



player1 = bot2
player2 = bot1

# if repeat count is more than 1, then print messages will not be displayed
repeatCount = 10


simulate(player1, player2, repeatCount)



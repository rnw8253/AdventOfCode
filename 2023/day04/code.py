import numpy as np
import sys

def CalcCardWins(winningNumbers, scratchNumbers):
    wins = 0
    for winNum in winningNumbers:
        if winNum in scratchNumbers:
            wins += 1
    points = 2**(wins-1)
    return int(wins), int(points)


winningNumbers = np.loadtxt("data.dat", usecols = range(2,12))
scratchNumbers = np.loadtxt("data.dat", usecols = range(13,38))

# Calculate the number of wins and the tickets given for each each win for each ticket
totalPoints = 0
cardWins = []
for cardIndex in range(len(winningNumbers)):
    wins, points = CalcCardWins(winningNumbers[cardIndex],scratchNumbers[cardIndex])
    totalPoints += points
    cardWins.append([cardIndex,wins,np.arange(cardIndex+1,cardIndex+wins+1)])

# Work Backwards and calculate the total number of tickets each ticket gives including all wins each ticket gained from its winning gives
cards = np.zeros(len(winningNumbers),int)
for cardIndex in range(len(winningNumbers)-1,-1,-1):
    for index in cardWins[cardIndex][2]:
        cards[cardIndex] += cards[index] + 1

print(np.sum(cards)+len(cards))


import numpy as np
from collections import Counter


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        
    def cardValue(self, cardIndex):
        if self.cards[cardIndex] == "A":
            return 14
        elif self.cards[cardIndex] == "K":
            return 13
        elif self.cards[cardIndex] == "Q":
            return 12
        elif self.cards[cardIndex] == "J":
            return 1
        elif self.cards[cardIndex] == "T":
            return 10
        else:
            return int(self.cards[cardIndex])

    def handRank(self, wildJs):
        cardDist = Counter(self.cards)
        if wildJs:
            nJs = cardDist['J']
        else:
            nJs = 0
        sortCards = sorted(Counter(self.cards).values())
        if sortCards == [5]:
            return 7
            #print("5 of a kind")
        elif sortCards == [1,4]:
            if nJs > 0:
                return 7
            else:
                return 6
            #print("4 of a kind")
        elif sortCards == [2,3]:
            if nJs > 0:
                return 7
            else:
                return 5
            #print("Fullhouse")
        elif sortCards == [1,1,3]:
            if nJs > 0:
                return 6
            else:
                return 4
            #print("3 of a kind")
        elif sortCards == [1,2,2]:
            if nJs == 1:
                return 5
            elif nJs == 2:
                return 6
            else:
                return 3
            #print("2 pair")
        elif sortCards == [1,1,1,2]:
            if nJs > 0:
                return 4
            else:
                return 2
            #print("Pair")
        elif sortCards == [1,1,1,1,1]:
            if nJs > 0:
                return 2
            else:
                return 1
            #print("High Card")
        else:
            return 0

    def cardRank(self):
        rank = 0
        for i in range(5):
            rank += self.cardValue(i)*10**(2*(4-i))
        return rank

hands = []
for line in open("data.dat").read().splitlines():
    hand, bid = line.split()
    hands.append(Hand(hand,bid))

rankedBids = []
for hand in hands:
    rankedBids.append([hand.handRank(True),hand.cardRank(), hand.bid])

winnings = 0
for index, (hr, cr, bid) in enumerate(sorted(rankedBids)):
    winnings += bid*(index+1)
print(f"Total Winnings: {winnings}")

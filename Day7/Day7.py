
import re
import sys
from collections import Counter

test = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
QQQJJ 123
AAAAA 234
7777A 444
AAT54 923
23456 812'''

class Card():
    def __init__(self, card):
        if card == 'A':
            self.value = 14
        elif card == 'K':
            self.value = 13
        elif card == 'Q':
            self.value = 12
        elif card == 'J':
            self.value = 11
        elif card == 'T':
            self.value = 10
        else:
            self.value = int(card)

        self.lookup = {11:'J', 12:'Q', 13:'K', 14:'A'}

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False

    def __str__(self):
        if self.value <= 10:
            return str(self.value)
        else:
            return self.lookup[self.value]

    def __repr__(self):
        return 'Card:' + self.__str__()

class Hand():
    def __init__(self, card_str):
        self.card_str = card_str
        self.hand = []

        cards, bet = card_str.split()
        self.bet = int(bet)

        for c in cards:
            self.hand.append(Card(c))

        count = Counter(self.hand)

        common = count.most_common()

        self.type = None
        if common[0][1] == 5:
            self.type = 'Five of a Kind'
        elif common[0][1] == 4:
            self.type = 'Four of a Kind'
        elif len(common) == 2 and common[0][1] == 3:
            self.type = 'Full House'
        elif common[0][1] == 3 and len(common) > 2:
            self.type = 'Three of a Kind'
        elif common[0][1] == 2 and common[1][1] == 2:
            self.type = 'Two pair'
        elif common[0][1] == 2 and len(common) == 4:
            self.type = 'One pair'
        else:
            self.type = 'High Card'

        #print(common, self.type)



def main():

    with open('7.input.txt', 'r') as fh:
        data = test.split('\n')

        hands = []
        for d in data:
            new_hand = Hand(d)


if __name__ == '__main__':
    main()

import re
import sys
from collections import Counter
from functools import total_ordering

test = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
QQQJJ 123
AAAAA 234
7777A 444
AAT54 923
23456 812
23152 123
23153 124
23151 251'''

test2 = '''AAA32 123
AAA33 234
AAA56 456
AAA23 123'''

test3 = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''


@total_ordering
class Card():
    def __init__(self, card):
        if card == 'A':
            self.value = 14
        elif card == 'K':
            self.value = 13
        elif card == 'Q':
            self.value = 12
        elif card == 'J':
            self.value = 1
        elif card == 'T':
            self.value = 10
        else:
            self.value = int(card)

        self.lookup = {10:'T', 1:'J', 12:'Q', 13:'K', 14:'A'}

    def __lt__(self, card2):
        #print('LT2', self.value, card2.value)
        if self.value < card2.value:
            return True
        return False

    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        return False

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False

    def __str__(self):
        if self.value < 10 and self.value != 1:
            return str(self.value)
        else:
            return self.lookup[self.value]

    def __repr__(self):
        return 'Card:' + self.__str__()


@total_ordering
class Hand():
    def __init__(self, card_str):
        self.card_str = card_str
        self.hand = []
        self.rank = None

        cards, bet = card_str.split()
        self.bet = int(bet)

        for c in cards:
            self.hand.append(Card(c))

        count = Counter(self.hand)

        self.common = count.most_common()

        self.type = None

        if 'J' not in cards:
            if self.common[0][1] == 5:
                self.type = 'Five of a Kind'
            elif self.common[0][1] == 4:
                self.type = 'Four of a Kind'
            elif len(self.common) == 2 and self.common[0][1] == 3:
                self.type = 'Full House'
            elif self.common[0][1] == 3 and len(self.common) > 2:
                self.type = 'Three of a Kind'
            elif self.common[0][1] == 2 and self.common[1][1] == 2:
                self.type = 'Two pair'
            elif self.common[0][1] == 2 and len(self.common) == 4:
                self.type = 'One pair'
            else:
                self.type = 'High Card'
        else:
            for c in self.common:
                if c[0].value == 1:
                    J_counts = c[1]

            #print(cards)
            #print(count)
            #print(self.common)
            #print(J_counts)

            match J_counts:
                case 5 | 4:
                    self.type = 'Five of a Kind'
                case 3:
                    if self.common[1][1] == 2:
                        self.type = 'Five of a Kind'
                    elif self.common[1][1] == 1:
                        self.type = 'Four of a Kind'
                case 2:
                    if len(self.common) == 4:
                        self.type = 'Three of a Kind'
                    elif len(self.common) == 3:
                        self.type = 'Four of a Kind'
                    elif len(self.common) == 2:
                        self.type = 'Five of a Kind'
                    else:
                        print('ERROR STATE 2 Jacks')
                        sys.exit()

                case 1:
                    if len(self.common) == 5:
                        self.type = 'One pair'
                    elif len(self.common) == 4:
                        self.type = 'Three of a Kind'
                    elif len(self.common) == 3 and self.common[0][1] != 3:
                        self.type = 'Full House'
                    elif len(self.common) == 3 and self.common[0][1] == 3:
                        self.type = 'Four of a Kind'
                    elif len(self.common) == 2:
                        self.type = 'Five of a Kind'

        #print(common, self.type)

    def __eq__(self, hand2):
        for z in range(0,5):
            if self.hand[z] != hand2.hand[z]:
                return False
            return True

    def __lt__(self, hand2):
        #print('LT', self.hand, hand2.hand)
        for z in range(0,5):
            if self.hand[z] < hand2.hand[z]:
                return True
            elif self.hand[z] == hand2.hand[z]:
                continue
            else:
                return False

    def __gt__(self, hand2):
        #print('GT', self.hand, hand2.hand)
        for z in range(0,5):
            if self.hand[z] > hand2.hand[z]:
                return True
            elif self.hand[z] == hand2.hand[z]:
                continue
            else:
                return False

    def __str__(self):
        return ':'.join([str(x) for x in self.hand])

    def __repr__(self):
        return self.__str__()


def main():

    with open('7.input.txt', 'r') as fh:
        data = fh.read().split('\n')
        #data = test3.split('\n')

        hands = []
        for d in data:
            new_hand = Hand(d)
            hands.append(new_hand)

        for z, h in enumerate(hands, start=1):
            print(z, h, h.rank, h.type)

        five = []
        four = []
        full = []
        three = []
        two = []
        one = []
        high = []


        for z in range(0, len(hands)):
            match hands[z].type:
                case 'Five of a Kind':
                    five.append(hands[z])
                case 'Four of a Kind':
                    four.append(hands[z])
                case 'Full House':
                    full.append(hands[z])
                case 'Three of a Kind':
                    three.append(hands[z])
                case 'Two pair':
                    two.append(hands[z])
                case 'One pair':
                    one.append(hands[z])
                case 'High Card':
                    high.append(hands[z])

        five = sorted(five)
        four = sorted(four)
        full = sorted(full)
        three = sorted(three)
        two = sorted(two)
        one = sorted(one)
        high = sorted(high)

        tricks = [high, one, two, three, full, four, five]
        #print(tricks)

        z = 1
        for t in tricks:
            for h in t:
                h.rank = z
                z += 1

        total_sum = 0
        for z, h in enumerate(hands, start=1):
            
            try:
                print(z, h, h.rank, h.bet, h.bet * h.rank)
                total_sum += (h.rank * h.bet)
            except:
                print('Error', h.rank, h.bet)
                sys.exit()

        print(total_sum)
        #print(five)
        #print(four)
        #print(full)
        #print(three)
        #print(two)
        #print(one)
        #print(high)
        #print('')
        #print(sorted(one))

        '''
        a = Hand('AAA23 123')
        b = Hand('AAA35 234')
        c = Hand('AAA34 456')
        d = Hand('AAA88 152')
        e = Hand('AAA11 512')

        print(a)
        print(b)
        print(c)
        print(a == b)
        print(b == c)

        test_sort = [a, b, c, d, e]
        print(test_sort)
        print(sorted(test_sort))
        '''

if __name__ == '__main__':
    main()
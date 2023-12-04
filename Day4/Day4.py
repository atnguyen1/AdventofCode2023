from collections import DefaultDict
import sys


with open('4.test.txt', 'r') as fh:
    data = fh.readlines()

    cards = []
    first_pass = []
    for z, d in enumerate(data, start=1):
        play, win = d.split('|')
        play = play.split(':')[1].rstrip().lstrip()
        win = win.rstrip().lstrip()

        play = sorted([int(x) for x in play.split()])
        win = sorted([int(x) for x in win.split()])

        score = 0
        winning = 0

        for p in play:
            if p in win:
                winning += 1
                if score == 0:
                    score = 1
                else:
                    score = score * 2

        cards.append(score)
        first_pass.append((play, win, winning, score))

    print('Part 1:', sum(cards))

    copy_counter = defaultdict(int)
    copy_counter[1] = 1
    for z, f in enumerate(first_pass, start=1):
        print(f)
        for c in copy_counter[z]:
            for x in range(z, f[2] + 1):



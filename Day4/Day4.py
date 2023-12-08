
import sys

with open('4.input.txt', 'r') as fh:
    data = fh.readlines()

    cards = []
    first_pass = []
    copy_counter = {}

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
        copy_counter[z] = 1

    print('Part 1:', sum(cards))

    for z, f in enumerate(first_pass, start=1):
        #print(f)
        #print(copy_counter[z])
        for repeat in range(0, copy_counter[z]):
            for i in range(1, f[2] + 1):
                copy_counter[z + i] += 1
        #print(copy_counter)

    #print(copy_counter)
    sum_cards = 0
    for k in copy_counter.keys():
        sum_cards += copy_counter[k]

    print('Part 2:', sum_cards)
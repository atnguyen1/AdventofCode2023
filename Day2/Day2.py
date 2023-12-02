import re

init = {'r':12, 'g':13, 'b':14}

def valid(tricks):
    for t in tricks:
        if init[t[1]] < t[0]:
            return False

    return True

def least(game):
    l = {'b': None, 'g': None, 'r': None}
    for g in game:
        for b in g:
            if l[b[1]] is None:
                l[b[1]] = b[0]
            elif b[0] > l[b[1]]:
                l[b[1]] = b[0]

    return l['b'] * l['g'] * l['r']

with open('2.input.txt', 'r') as fh:
    data = fh.read().split('\n')
    game_sum = 0
    game_pwr = 0

    for z, d in enumerate(data, start=1):
        games = d.split(':')[1]
        games = [x.lstrip().rstrip() for x in games.split(';')]
        game_str = []

        for g in games:
            g = g.split(',')
            single_game = []
            for i in g:
                res = re.match(' *?(\d+) (\w+)', i)
                if res:
                    single_game.append((int(res.group(1)), res.group(2)[0]))
            game_str.append(single_game)

        v = [valid(g) for g in game_str]
        p = least(game_str)
        game_pwr += p

        if False not in v:
            game_sum += z

    print('Part1: ', game_sum)
    print('Part2: ', game_pwr)
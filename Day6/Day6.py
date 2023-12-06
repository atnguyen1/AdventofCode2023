import sys
from functools import reduce
import progressbar

part2 = '''Time:        48938595
Distance:   296192812361391'''

def distance(time, max_time):
    return time * (max_time - time)

with open('6.input.txt', 'r') as fh:
    data = fh.read().split('\n')

    t = data[0].split(':')[-1]
    t = [int(x) for x in t.split()]
    d = data[1].split(':')[-1]
    d = [int(x) for x in d.split()]
    all_races = dict(zip(t, d))

    win_vector = []
    for race_time in all_races:
        wins = 0
        for x in range(0, race_time + 1):
            d = distance(x, race_time)
            if d > all_races[race_time]:
                wins += 1
        win_vector.append(wins)

    #print(win_vector)
    print('Part1:', reduce((lambda x, y: x * y), win_vector))

    part2_race = {48938595:296192812361391}

    widgets = [
        ' [', progressbar.Timer(), '] ', progressbar.GranularBar(), ' ', progressbar.ETA()]

    wins2 = 0
    idx = 0
    with progressbar.ProgressBar(max_value=48938596, widgets=widgets) as bar:
        for x in range(0, 48938595 + 1):
            d = distance(x, 48938595)
            if d > 296192812361391:
                wins2 += 1

            idx += 1
            bar.update(idx)

    print(wins2)
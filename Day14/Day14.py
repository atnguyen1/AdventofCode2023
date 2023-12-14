import os
import sys
import re
import numpy as np

test='''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''


def roll_north(platform):
    ymax,xmax = platform.shape
    roll = True
    state = np.copy(platform)
    while roll:
        for y in range(1, ymax):
            for x in range(0, xmax):
                if platform[y, x] == 'O':
                    if platform[y - 1, x] == '.':
                        platform[y - 1, x] = 'O'
                        platform[y, x] = '.'
        if np.array_equal(state, platform):
            # If we rolled and state didnt' change break
            roll = False
        state = np.copy(platform)

    return platform

def calc_load(platform):
    ymax,xmax = platform.shape
    l = 0
    for y in range(0, ymax):
        for x in range(0, xmax):
            if platform[y, x] == 'O':
                l += (ymax - y)
    return l

def spincycle(platform):
    ymax,xmax = platform.shape
    roll = True
    state = np.copy(platform)
    print(platform)

    while roll:
        # North
        #for y in range(1, ymax):
        #    for x in range(0, xmax):
        #        if platform[y, x] == 'O':
        #            if platform[y - 1, x] == '.':
        #                platform[y - 1, x] = 'O'
        #                platform[y, x] = '.'
        # West
        for y in range(0, ymax):
            for x in range(xmax - 2, 0 - 1, -1):
                if platform[y, x] == 'O':
                    if platform[y , x + 1] == '.':
                        platform[y, x + 1] = 'O'
                        platform[y, x] = '.'
        #print(platform)
        #sys.exit()                        

        if np.array_equal(state, platform):
            # If we rolled and state didnt' change break
            roll = False
        state = np.copy(platform)

    print(platform)
    return platform

def main():
    with open('14.input.txt', 'r') as fh:
        #data = fh.read().split('\n')
        data = test.split('\n')

        platform = []
        for d in data:
            platform.append([c for c in d])
        platform = np.array(platform, dtype=str)
        #print(platform)
        end_roll = roll_north(platform)
        #print(end_roll)
        print('Part1:', calc_load(end_roll))
        spincycle(platform)

if __name__ == '__main__':
    main()
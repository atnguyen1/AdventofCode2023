import os
import sys
import re
import numpy as np
from collections import Counter

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
    z = 1
    debug = False

    state_list = []
    state_list_index = []
    init_state_list_size = len(state_list)

    if debug:
        print(platform)

    while True:
        if debug:
            print('Spin:', z)
        roll = True
        state = np.copy(platform)

        # North
        while roll:
            for y in range(1, ymax):
                for x in range(0, xmax):
                    if platform[y, x] == 'O':
                        if platform[y - 1, x] == '.':
                            platform[y - 1, x] = 'O'
                            platform[y, x] = '.'
            if np.array_equal(state, platform):
                roll = False
            state = np.copy(platform)
        # West
        roll = True
        state = np.copy(platform)
        while roll:
            for y in range(0,  ymax):
                for x in range(1, xmax):
                    if platform[y, x] == 'O':
                        if platform[y, x - 1] == '.':
                            platform[y, x - 1] ='O'
                            platform[y, x] = '.'
            if np.array_equal(state, platform):
                roll = False
            state = np.copy(platform)
        # South
        roll = True
        state = np.copy(platform)
        while roll:
            for y in range(ymax - 2, -1, -1):
                for x in range(0, xmax):
                    if platform[y + 1, x] == '.':
                        if platform[y, x] == 'O':
                            platform[y + 1, x] = 'O'
                            platform[y, x] = '.'
            if np.array_equal(state, platform):
                roll = False
            state = np.copy(platform)
        # East
        roll = True
        state = np.copy(platform)
        while roll:
            for y in range(0, ymax):
                for x in range(xmax - 2, -1, -1):
                    if platform[y, x] == 'O':
                        if platform[y , x + 1] == '.':
                            platform[y, x + 1] = 'O'
                            platform[y, x] = '.'
            if np.array_equal(state, platform):
                roll = False
            state = np.copy(platform)        

        z += 1
        if debug:
            print(platform)
        # End state after 1 cycle
        temp = platform.tolist()
        x = []
        for t in temp:
            x.extend(t)
        x = ''.join(x)

        if x not in state_list:
            state_list.append(x)
            state_list_index.append(state_list.index(x))
        else:
            state_list_index.append(state_list.index(x))

        #if len(state_set) == init_state_size:
        #if len(stsate_list_index) == init_state_list_size:
        if len(state_list) == init_state_list_size:
            if debug:
                print('Steps', z)
                print(state_list)
                print(state_list_index)
            break
        else:
            init_state_list_size = len(state_list)

    repeat = state_list_index[-1]
    start_loop = state_list_index[repeat]

    new_loop = state_list[start_loop:-1]
    new_loop_idx = state_list_index[start_loop:-1]
    if debug:
        print(repeat)
        print(start_loop)
        print(new_loop)
        print(new_loop_idx)
    offset = 1000000000 - start_loop

    final_state_idx = (offset % len(new_loop_idx)) - 1
    final_state = new_loop[final_state_idx]

    if debug:
        print(offset)
        print(final_state)

    final_array = []
    row = []
    for z, char in enumerate(final_state):
        row.append(char)

        if len(row) % xmax == 0:
            final_array.append(row)
            row = []
    #for f in final_array:
    #    print(f)
    fa = np.array(final_array, dtype=str)
    #print(fa)
    #print(calc_load(fa))
    return(fa)

def main():
    with open('14.input.txt', 'r') as fh:
        data = fh.read().split('\n')
        #data = test.split('\n')

        platform = []
        for d in data:
            platform.append([c for c in d])
        platform = np.array(platform, dtype=str)
        platform2 = np.copy(platform)
        #print(platform)
        end_roll = roll_north(platform2)
        #print(end_roll)
        print('Part1:', calc_load(end_roll))
        end_roll2 = spincycle(platform)
        print('Part2:', calc_load(end_roll2))

if __name__ == '__main__':
    main()
import re
import sys
import numpy as np
from itertools import combinations


test = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

test_correct = '''....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......'''

def pairs(n):
    return (n*(n-1)) / 2

def manahatten(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    with open('11.input.txt', 'r') as fh:
        data = fh.read().split('\n')
        #data = test.split('\n')
        ymax = len(data)
        xmax = len(data[0])

        empty_x = np.array(['.'] * xmax, dtype=str)
        empty_y = np.array(['.'] * ymax, dtype=str)
        #print(empty_x)
        #print(empty_y)
        galaxy = np.full((len(data), len(data[0])), dtype=str, fill_value='.')

        for y, row in enumerate(data):
            for x, dot in enumerate(row):
                if dot == '#':
                    galaxy[y, x] = '#'

        #print(galaxy)

        yranges = []
        xranges = []
        for y in range(0, len(data)):
            galaxy_row = galaxy[y,:]
            galaxy_col = galaxy[:,y]
            if np.all(galaxy_row == empty_x):
                yranges.append(y)
            if np.all(galaxy_col == empty_y):
                xranges.append(y)
        for insert, y in enumerate(yranges):
            galaxy = np.insert(galaxy, y + insert, empty_y, axis=0)

        # Update shape
        empty_x = ['.'] * len(galaxy[:,0])

        for insert2, x in enumerate(xranges):
            galaxy = np.insert(galaxy, x + insert2, empty_x, axis=1)

        g = np.where(galaxy == '#')
        g_loc = [x for x in zip(g[0], g[1])]
        #print(len(g_loc), pairs(len(g_loc)))

        '''
        # Test cases
        print(galaxy)
        tc = test_correct.split('\n')
        t = np.full((len(galaxy[:,0]), len(galaxy[0,:])), dtype=str, fill_value='.')
        print(t.shape)
        print(galaxy.shape)
        for y, row in enumerate(tc):
            for x, dot in enumerate(row):
                if dot == '#':
                    t[y, x] = '#'

        print(np.all(galaxy==t))
        '''
        dist = list(combinations(g_loc, 2))
        short = []
        for d in dist:
            y1,x1 = d[0]
            y2,x2 = d[1]
            #print(d)
            #print(x1,x2,y1,y2)
            short.append(manahatten(x1,x2,y1,y2))

        print(sum(short))


if __name__ == '__main__':
    main()
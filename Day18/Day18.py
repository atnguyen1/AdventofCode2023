import os
import re
import sys
import numpy as np
from itertools import pairwise

test = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''

def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1

def batched(iterable, batch_size, fill_value=None):
    for batch in batched(iterable, batch_size):
        yield batch + (fill_value,) * (batch_size - len(batch))

def main():
    with open('18.input.txt', 'r') as fh:
        data = fh.read().split('\n')
        #data = test.split('\n')

        instructions = []
        for d in data:
            res = re.match('([LRDU]) (\d) \(#([0-9a-fA-F]+)\)', d)
            if res:
                instructions.append((res.group(1), int(res.group(2)), res.group(3)))

        plane = np.zeros((1000, 1000), dtype=int)
        x = 500
        y = 500
        np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)
        #plane = np.zeros((11,11), dtype=int)
        #x = 1
        #y = 1
        plane[y, x] = 1
        edges = [(500, 500, instructions[0][2])]
        #edges = [(1, 1, instructions[0][2])]

        for i in instructions:
            match i[0]:
                case 'R':
                    for z in range(1, i[1]+1):
                        plane[y, x + z] = 1
                        edges.append((y, x + z, i[2]))
                    x = x + z
                case 'L':
                    for z in range(1, i[1]+1):
                        plane[y, x - z] = 1
                        edges.append((y, x - z, i[2]))
                    x = x - z
                case 'U':
                    for z in range(1, i[1]+1):
                        plane[y - z, x] = 1
                        edges.append((y - z, x, i[2]))
                    y = y - z
                case 'D':
                    for z in range(1, i[1]+1):
                        plane[y + z, x] = 1
                        edges.append((y + z, x, i[2]))
                    y = y + z

        xypairs = list()
        for y, row in enumerate(plane):
            r = row.tolist()
            if 1 in r:
                #xypairs = []
                left_edge = False
                last = None
                for i, element in enumerate(row):
                    if element == 1:
                        if not left_edge:
                            last = i
                            left_edge = True
                    elif element == 0:
                        if left_edge:
                            left_edge = False
                            xypairs.append((y, last, i))
                            last = None

                #print(xypairs)
                #for pairs in xypairs:
                #    for x in range(pairs[0], pairs[1]):
                #        plane[y, x] = 1
                #    print(r, pairs[0], pairs[1])
            else:
                pass
                #print(r)

        #for p in plane:
        #    print(np.array2string(p).replace(' ', ''))
        
        ymax, xmax = plane.shape
        inside = np.zeros((ymax, xmax), dtype = int)

        for y in range(0, ymax):
            row = plane[y,:]
            for x in range(0, xmax):
                row2 = row[x + 1:]
                if plane[y, x] == 0:
                    if sum(plane[y, 0:x]) > 0:
                        inside[y, x] = sum(row2)
        #print(' ')
        #for p2 in inside:
        #    print(np.array2string(p2).replace(' ', ''))

        total = np.zeros((ymax, xmax), dtype=int)

        for y in range(0, ymax):
            for x in range(0, xmax):
                if plane[y, x] == 1 or inside[y, x] > 0:
                    total[y, x] = 1

        print('Part1:', sum(sum(total)))

if __name__ == '__main__':
    main()
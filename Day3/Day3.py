import re
import sys
import numpy as np

symbols = ['*', '/', '@', '+', '-', '#', '&', '=', '%', '$']
dirs = [-1, 0 , 1]


def adjacent(y, x, schematic):
    for d1 in dirs:
        for d2 in dirs:
            if schematic[y + d1, x + d2] in symbols:
                return True

    return False

def adjacent2(y, x, schematic):
    '''
    [1 0 0] [0 1 0]   [1 1 0]  [1 1 1]
    [1 0 0] [1 0 0]   [1 0 0]  [1 0 0]
    [0 0 0] [0 0 0]   [0 0 0]  [0 0 0]            if sum of set(rows) >= 3, then multiple touching

    [1 1 1] [1 0 1]  [0 0 0]   [1 1 1]   [1 0 1]   [1 0 1] 
    [0 0 0] [0 0 0]  [1 0 1]   [0 0 1]   [0 0 0]   [0 0 0]
    [1 1 1] [0 0 0]  [0 0 0]   [0 0 0]   [1 0 0]   [1 0 1]

Valid Orientations:  # Mirrors are valid
 
    [1 1 1] [1 1 0] [1 0 0] [1 1 1] [1 1 0] [1 0 0] [1 1 1] [1 1 0] [1 0 0] [0 1 0] [0 0 0] [1 0 0] [0 0 0]  [0 0 0] [0 0 0] [0 0 0] [0 0 0]  
    [0 0 0] [0 0 0] [0 0 0] [0 0 0] [0 0 0] [0 0 0] [0 0 0] [0 0 0] [0 0 0] [0 0 0] [1 0 1] [0 0 0] [0 0 0]  [1 0 0] [1 0 0] [1 0 0] [1 0 0]
    [1 1 1] [1 1 1] [1 1 1] [1 1 0] [1 1 0] [1 1 0] [1 0 0] [1 0 0] [1 0 0] [0 1 0] [0 0 0] [0 0 1] [1 0 1]  [1 0 0] [0 1 0] [0 0 1] [1 1 1]


    '''
    mask = np.zeros((3,3), dtype=int)
    print(y, x, schematic[y, x])

    for d1 in dirs:
        for d2 in dirs:
            if re.match('\d', schematic[y + d1, x + d2]):
                mask[1 + d1,1 + d2] = 1

    # More than two connections
    print(mask)
    row_sum = 0
    for r in mask:
        q = set(r)
        row_sum += sum(q)

    print(row_sum)
    sys.exit()



with open('3.test.txt', 'r') as fh:
    data = fh.readlines()

    # Make Array and populate, pad with empty string
    schematic = np.full((len(data) + 2, len(data[0]) + 1), dtype=str, fill_value='.')    # Counts new line

    y = 1
    for row in data:
        row = row.rstrip()
        x = 1
        for char in row:
            schematic[y, x] = char
            x += 1
        y += 1

    in_number = False
    num_pos = []
    parts = []
    start = 0

    for y in range(1, len(data) + 1):               # size of y
        for x in range(1, len(data[0])):            # newline counted
            if re.match('\d', schematic[y,x]):               # Found a digit

                if not in_number:
                    in_number = True
                    num_pos.append((schematic[y,x], y, x))
                else:
                    num_pos.append((schematic[y,x], y, x))

            elif in_number and re.match('\D', schematic[y,x]):    # scanning digit and we found a non-digit, process
                for n in num_pos:
                    adj = adjacent(n[1], n[2], schematic)
                    if adj:
                        parts.append(int(''.join([x[0] for x in num_pos])))   # Adjacent
                        break

                in_number = False
                num_pos = []
        if in_number:           # Tail case at edge of map
            for n in num_pos:
                adj = adjacent(n[1], n[2], schematic)
                if adj:
                    parts.append(int(''.join([x[0] for x in num_pos])))   # Adjacent
                    break

            in_number = False
            num_pos = []

    #print(parts)
    print('Part1 :', sum(parts))

    # Part 2

    gears_index = []
    for y in range(1, len(data) + 1):
        for x in range(1, len(data[0])):              # newline counted
            if schematic[y, x] in symbols:
                gears_index.append((y, x))

    for g in gears_index:
        adjacent2(g[0], g[1], schematic)

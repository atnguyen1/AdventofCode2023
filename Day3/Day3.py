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

valids = []

def generate_valids():
    global valids
    a = np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1]], dtype=int)
    valids.append(a)

    b = np.array([[1, 1, 0], [0, 0, 0], [1, 1, 1]], dtype=int)
    b1 = np.flip(b, 1)
    b2 = np.flip(b, 0)
    b3 = np.flip(b)
    valids.append(b)
    valids.append(b1)
    valids.append(b2)
    valids.append(b3)

    c = np.array([[1, 0, 0], [0, 0, 0], [1, 1, 1]], dtype=int)
    c1 = np.flip(c, 1)
    c2 = np.flip(c, 0)
    c3 = np.flip(c)
    valids.append(c)
    valids.append(c1)
    valids.append(c2)
    valids.append(c3)

    d = np.array([[1, 1, 0], [0, 0, 0], [1, 1, 0]], dtype=int)
    d1 = np.flip(d, 1)


    valids.append(d)
    valids.append(d1)

    e = np.array([[1, 0, 0], [0, 0, 0], [1, 1, 0]], dtype=int)
    e1 = np.flip(e, 1)
    e2 = np.flip(e, 0)
    e3 = np.flip(e)

    #print(e)
    #print(e1)
    #print(e2)
    #print(e3)



def adjacent2(y, x, schematic):
    '''
    [1 0 0] [0 1 0]   [1 1 0]  [1 1 1]
    [1 0 0] [1 0 0]   [1 0 0]  [1 0 0]
    [0 0 0] [0 0 0]   [0 0 0]  [0 0 0]            if sum of set(rows) >= 3, then multiple touching

    [1 1 1] [1 0 1]  [0 0 0]   [1 1 1]   [1 0 1]   [1 0 1] 
    [0 0 0] [0 0 0]  [1 0 1]   [0 0 1]   [0 0 0]   [0 0 0]
    [1 1 1] [0 0 0]  [0 0 0]   [0 0 0]   [1 0 0]   [1 0 1]

Valid Orientations:  # Mirrors are valid
       x       x       x      x        x       x
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


    generate_valids()
    #for g in gears_index:
    #    adjacent2(g[0], g[1], schematic)

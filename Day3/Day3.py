import re
import sys
import numpy as np
from collections import defaultdict

symbols = ['*', '/', '@', '+', '-', '#', '&', '=', '%', '$']
dirs = [-1, 0 , 1]


def adjacent(y, x, schematic):
    for d1 in dirs:
        for d2 in dirs:
            if schematic[y + d1, x + d2] in symbols:
                return True

    return False

def get_gear(y, x, schematic):
    for d1 in dirs:
        for d2 in dirs:
            if schematic[y + d1, x + d2] in symbols:
                #return True
                return (y + d1, x + d2)

    return None

with open('3.input.txt', 'r') as fh:
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
    gear_counter = defaultdict(list)

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
                    gear_pos = get_gear(n[1], n[2], schematic)
                    if adj:
                        parts.append(int(''.join([x[0] for x in num_pos])))   # Adjacent
                        gear_counter[gear_pos].append(int(''.join([x[0] for x in num_pos])))
                        break

                in_number = False
                num_pos = []
        if in_number:           # Tail case at edge of map
            for n in num_pos:
                adj = adjacent(n[1], n[2], schematic)
                gear_pos = get_gear(n[1], n[2], schematic)
                if adj:
                    parts.append(int(''.join([x[0] for x in num_pos])))   # Adjacent
                    gear_counter[gear_pos].append(int(''.join([x[0] for x in num_pos])))
                    break

            in_number = False
            num_pos = []

    #print(parts)
    print('Part1 :', sum(parts))

    sum_gear = 0
    for key in gear_counter.keys():
        nums = gear_counter[key]
        if len(nums) == 2:
            val = nums[0] * nums[1]
            print(val)
            sum_gear += val

    print(sum_gear)

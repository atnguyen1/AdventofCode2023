import re
import sys

with open('5.test.txt', 'r') as fh:
    data = fh.read().split('\n\n')

    seeds = [int(x) for x in data[0].split(':')[1].split()]

    maps = []


    for d in data[1:]:
        name, ran = d.split(':\n')
        namem = re.match('\w+-to-(\w+).+', name)
        name = namem.group(1)

        total_ranges = []

        for r in ran.split('\n'):
            r = [int(x) for x in r.split()]
            total_ranges.append(r)


        maps.append((name, total_ranges))

    results = []
    for s in seeds:
        key = s
        res = [('Seed', s)]

        for m in maps:
            ran = m[1]
            new_key = key

            for r in ran:
                if r[1] <= key and key <= r[1] + r[2]:      # correct range
                    new_key = r[0] + (key - r[1])

            res.append((m[0], new_key))
            key = new_key

        results.append(res)

    results = sorted(results, key=lambda x: x[-1][1])

    print('Part1:', results[0][-1][1])

    # Part 2 work backwards
    for m in maps[::-1]:
        for ran in m[1]:
            dest, start, step = ran

            if start > dest:   # mapping to go lower
                small = 

        print(m)
        sys.exit()
import re
import sys

class Ranges():
    def __init__(self, start, stride):
        self.start = start
        self.stride = stride
        self.end = self.start + self.stride

    def overlap(self, mappings):
        pass

    def split(self, mappings):
        # Given a mapping of a -> b
        # determine if the range of chunks overlaps and if so split the ranges

        for r in mappings[1]:
            #if self.start < r[1] and  
            print(r)

    def __str__(self):
        return 'RangeObj-' + str(self.start) + ':' + str(self.stride)



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

    # Part 2
    # Track by range chunks and not ints
 
    seed_start = seeds[0::2]
    seed_steps = seeds[1::2]
    seed2 = [x for x in zip(seed_start, seed_steps)]

    seed_ranges = []
    for s in seed2:
        a = Ranges(s[0], s[1])
        seed_ranges.append(a)

    for m in maps:
        for seed in seed_ranges:
            seed.overlap(m)

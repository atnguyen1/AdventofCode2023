import os
import sys
import re
from collections import deque

test = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''

def ha(s):
    a = 0
    for char in s:
        a += ord(char)
        a = a * 17
        a = a % 256
    return a

class Box:
    def __init__(self, idnum):
        self.id = idnum
        self.lenses = deque()
        self.focus = dict()

    def add(self, lens_label, focal_length):
        if lens_label in self.lenses:
            self.focus[lens_label] = focal_length
        else:
            self.lenses.append(lens_label)
            self.focus[lens_label] = focal_length

    def remove(self, lens_label):
        if lens_label in self.lenses:
            self.lenses.remove(lens_label)
            del self.focus[lens_label]

    def get_power(self):
        res = []
        for z, l in enumerate(self.lenses, start=1):
            p = 1 + int(self.id)
            p = p * z
            p = p * int(self.focus[l])
            res.append((l, p))
        return res

    def __str__(self):
        o = []
        for l in self.lenses:
            p = str(l) + '-' + str(self.focus[l])
            o.append(p)
        q = ':'.join(o)
        return str('Box: ' + str(self.id) + '--' + q)

    def __repr__(self):
        return self.__str__()

def main():
    with open('15.input.txt', 'r') as fh:
        data = fh.read().rstrip().split(',')
        #data = test.rstrip().split(',')

        debug = False
        boxes = []
        for i in range(0, 256):
            boxes.append(Box(i))

        for d in data:
            if debug:
                print(d)
            eqmatch = re.match('(.+)=(\d+)', d)
            if d[-1] == '-':
                # Removal Operation
                lens_label = d[:-1]
                if debug:
                    print('Remove', lens_label, ha(lens_label))
                b = boxes[ha(lens_label)]
                b.remove(lens_label)

            elif eqmatch:
                # Focal lens Add Operation
                lens_label = eqmatch.group(1)
                focal_length = eqmatch.group(2)
                if debug:
                    print('Eq', eqmatch.group(1), eqmatch.group(2), ha(eqmatch.group(1)))

                b = boxes[ha(lens_label)]
                b.add(lens_label, focal_length)

        lens_final = []
        for b in boxes:
            lvals = b.get_power()
            if lvals != []:
                lens_final.extend(lvals)

        if debug:
            print(lens_final)

        part2 = 0
        for l in lens_final:
            part2 += l[1]

        print('Part2:', part2)


if __name__ == '__main__':
    main()
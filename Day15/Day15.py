import os
import sys
import re

test = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''

class HolidayAscii:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_val = 0

    def process(self):
        for char in self.input_string:
            self.current_val += ord(char)
            #print(char)
            #print('ascii add', self.current_val)
            self.current_val = self.current_val * 17
            #print('Mul', self.current_val)
            self.current_val = self.current_val % 256
            #print('Mod', self.current_val)

    def get_val(self):
        return self.current_val


def main():
    with open('15.input.txt', 'r') as fh:
        data = fh.read().rstrip().split(',')
        #data = test.rstrip().split(',')

        #a = HolidayAscii('HASH')
        #a.process()
        #print(a.get_val())

        steps = []

        for d in data:
            ha = HolidayAscii(d)
            ha.process()
            #print(d, ha.get_val())
            steps.append(ha.get_val())

        print('Part1:', sum(steps))


if __name__ == '__main__':
    main()
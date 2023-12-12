import re
import sys
from itertools import product

test = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

base = '''#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1'''


def str_to_ecc(input_string):
    return [len(i) for i in input_string.split('.')  if i != '']

def main():
    with open('12.input.txt', 'r') as fh:
        #data = fh.read().split('\n')
        data = test.split('\n')

        for d in data:
            springs, ecc = d.rstrip().split()
            #print(springs, ecc, str_to_ecc(springs))
            #groups = [s for s in springs.split('.') if s != '']
            #ecc = ecc.split(',')

            questions = re.findall('(\?+)', springs)
            replacements = []
            for q in questions:
                replacements.append(["".join(seq) for seq in product("01", repeat=len(q))])

            unknowns = [s for s in springs.split('.') if s != '']
            print(unknowns)
            print(replacements)


if __name__ == '__main__':
    main()
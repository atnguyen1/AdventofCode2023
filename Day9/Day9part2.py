import re
import sys


test = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

test2 = '''10 13 16 21 30 45'''


def main():
    with open('9.input.txt', 'r') as fh:
        data = [[int(y) for y in x.split()] for x in fh.read().split('\n')]

        processed = []
        for d in data:

            zerop = False
            current_d = d
            depth = [current_d]

            while not zerop:
                diff = [current_d[x + 1] - current_d[x] for x in range(0, len(current_d) -1)]
                current_d = diff

                if diff == [0] * len(diff):
                    zerop = True
                depth.append(current_d)


            processed.append(depth)

        summed = []
        for p in processed:
            #print(p)
            q = p[::-1]
            #print(q)
            q[0].append(0)

            for x in range(1, len(q)):
                q[x] = q[x][::-1]
                q[x].append(q[x][-1] - q[x-1][-1])

            #print(q)
            summed.append(q)
            #sys.exit()

        #print('Q')
        #for q in summed:
        #    print(q)

        new_history = [x[-1][-1] for x in summed]
        print('Part1:', sum(new_history))





if __name__ == '__main__':
    main()
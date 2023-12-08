import sys
import re

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __str__(self):
        return self.label + ':' + self.left + ':' + self.right

    def __repr__(self):
        return self.__str__()


def build_tree(label, lookup):
    n = Node(label)
    left = lookup(label)[0]
    right = lookup(label)[1]

    if left 








def main():
    test = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''


    with open('8.input.txt', 'r') as fh:
        instructions, data = test.split('\n\n')
        instructions = instructions.rstrip().lstrip()

        node_connections = {}
        for d in data.split('\n'):
            res = re.match('(\w{3}) = .(\w{3}), (\w{3}).', d)
            if res:
                print(res.group(1), res.group(2), res.group(3))

                node_connections[res.group(1)] = (res.group(2), res.group(3))

        root = build_tree('AAA', node_connections)






if __name__ == '__main__':
    main()
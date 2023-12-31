import sys
import re

test = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

test2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

test3 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

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
        # left and right are node objects
        return self.label + ':' + self.left.label + ':' + self.right.label

    def __repr__(self):
        return self.__str__()

def main():
    with open('8.input.txt', 'r') as fh:
        instructions, data = fh.read().split('\n\n')
        instructions = instructions.rstrip().lstrip()

        node_connections = {}
        for d in data.split('\n'):
            res = re.match('(\w{3}) = .(\w{3}), (\w{3}).', d)
            if res:
                print(res.group(1), res.group(2), res.group(3))

                node_connections[res.group(1)] = (res.group(2), res.group(3))

        nodes = {}
        for n in node_connections.keys():
            nodes[n] = Node(n)

        for n in node_connections.keys():
            nodes[n].set_left(nodes[node_connections[n][0]])   # Not a node object
            nodes[n].set_right(nodes[node_connections[n][1]])

        current_node = nodes['AAA']
        instruction_start = 0
        steps = 0
        while current_node.label != 'ZZZ':

            if instructions[instruction_start % len(instructions)] == 'L':
                current_node = current_node.left
            elif instructions[instruction_start % len(instructions)] == 'R':
                current_node = current_node.right
            else:
                print("WTF FAIL")
                sys.exit()
            steps += 1
            instruction_start += 1

        print('Part1 Steps:', steps)


if __name__ == '__main__':
    main()
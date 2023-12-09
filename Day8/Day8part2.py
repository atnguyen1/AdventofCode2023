import sys
import re
import numpy as np

# LCM
# https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple

from math import lcm

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

def endp(label):
    if label[-1] == 'Z':
        return True
    return False

def done(node_list):
    doneyet = [endp(x.label) for x in node_list]

def main():
    with open('8.input.txt', 'r') as fh:
        instructions, data = fh.read().split('\n\n')
        instructions = instructions.rstrip().lstrip()

        node_connections = {}
        for d in data.split('\n'):
            res = re.match('(\w{3}) = .(\w{3}), (\w{3}).', d)
            if res:
                #print(res.group(1), res.group(2), res.group(3))

                node_connections[res.group(1)] = (res.group(2), res.group(3))

        nodes = {}
        starts = []
        stops = []
        for n in node_connections.keys():
            new_node = Node(n)
            nodes[n] = new_node
            if n[-1] == 'A':
                starts.append(new_node)
            if n[-1] == 'Z':
                stops.append(new_node)

        for n in node_connections.keys():
            nodes[n].set_left(nodes[node_connections[n][0]])
            nodes[n].set_right(nodes[node_connections[n][1]])

        # Find Starts

        steps = 0
        instruction_start = 0
        current_nodes = starts

        #print(starts)
        #print(stops)
        #print(starts)
        z = 0
        done_steps = []
        all_nodes = []

        found_end = [0] * len(starts)
        while 0 in found_end:
            next_nodes = []

            d = [endp(x.label) for x in current_nodes]
            if True in d:
                en_i = d.index(True)
                # Found an Endpoint
                found_end[en_i] = (current_nodes[en_i], steps)

            for c in current_nodes:
                if instructions[instruction_start % len(instructions)] == 'L':
                    next_nodes.append(c.left)
                elif instructions[instruction_start % len(instructions)] == 'R':
                    next_nodes.append(c.right)
            all_nodes.append([(x) for x in next_nodes])


            #print(instructions[instruction_start % len(instructions)])
            steps += 1
            instruction_start += 1
            current_nodes = next_nodes
            
            #print(current_nodes)
            #if z >=2:
            #    break
            #z += 1
        print(found_end)
        ends = [x[1] for x in found_end]
        print(ends)

        print('Steps is LCM of all steps to get to endpoint:', lcm(*ends))


        #print(all_nodes)
        #print(current_nodes)
        #print('Part 2 Steps', steps)




        '''
        current_node = nodes['AAA']
        instruction_start = 0
        steps = 0
        while current_node.label != 'ZZZ':

            if instructions[instruction_start % len(instructions)] == 'L':                current_node = current_node.left
            elif instructions[instruction_start % len(instructions)] == 'R':
                current_node = current_node.right
            else:
                print("WTF FAIL")
                sys.exit()
            steps += 1
            instruction_start += 1

        print('Part1 Steps:', steps)
        '''

if __name__ == '__main__':
    main()
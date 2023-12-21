import os
import re
import sys
import numpy as np

test = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

ALL_TREE = {}

class Tree:
    def __init__(self, label):
        self.children = []
        self.label = label
        self.edges = []
        self.parent = None
        self.edge_lookup = None

    def associate(self):
    	self.edge_lookup = dict(zip(self.children, self.edges))

    def set_children(self, children):
    	self.children = children

    def children_contains(self, key):
    	if key in self.children:
    		return True

    def __contains__(self, key):
    	return key in self.label

    def __str__(self):
    	return self.label

    def __repr__(self):
    	return self.__str__()


def dfs(root, target, path=(), set_paths=[]):
	path = path + (root,)

	if root.label == target:
		return path

	for child in root.children:
		path_found = dfs(ALL_TREE[child], target, path)

		if path_found is not None:
			return path_found

	return None

def exhaust(root):
	"""Exhaustive search"""
	if not root.children:
		return [[root.label]]
	paths = []
	for child in root.children:
		for path in exhaust(ALL_TREE[child]):
			paths.append([root.label] + path)

	return paths

'''
def paths(self):
    if not self.children:
        return [[self.value]]  # one path: only contains self.value
    paths = []
    for child in self.children:
        for path in child.paths():
            paths.append([self.value] + path)
    return paths
'''

def get_assignment(part, iq, loc):
		#print(loc, iq[loc])
		for z, i in enumerate(iq[loc]):
			#print(z, i)
			if ':' in i:
				test, dest = i.split(':')
			else:
				dest = i
				test = ''
			passed_test = False

			if '<' in test:
				var, test_val = test.split('<')
				if part[var] < int(test_val):
					passed_test = True
			elif '>' in test:
				var, test_val = test.split('>')
				if part[var] > int(test_val):
					passed_test = True				
			elif '=' in test:
				var, test_val = test.split('=')
				if part[var] == int(test_val):
					passed_test = True

			if dest == 'R' and passed_test:
				return 'R'
			elif dest == 'A' and passed_test:
				return 'A'

			if z == len(iq[loc]) - 1:
				if dest == 'R':
					return 'R'
				elif dest == 'A':
					return 'A'
				return get_assignment(part, iq, dest)

			if passed_test is False:
				continue

			return get_assignment(part, iq, dest)
	
def main():
	with open("19.input.txt", 'r') as fh:
		#instructions, parts = fh.read().split('\n\n')
		instructions, parts = test.split('\n\n')

		instruction_queue = {}

		for i in instructions.split('\n'):
			regex = re.match('([a-z]+)\{(.+)\}', i)
			if regex:
				priority = regex.group(2).split(',')
				instruction_queue[regex.group(1)] = priority

		#for i in instruction_queue:
		#	print(i, instruction_queue[i])

		parts_queue = []
		for p in parts.split('\n'):
			regex2 = re.match('\{(.+)\}', p)
			if regex2:
				parts_queue.append(regex2.group(1).split(','))

		processed_parts = []
		for p in parts_queue:
			data_vals = {'x': 0, 'm':0, 'a':0, 's':0}
			for pa in p:
				var, val = pa.split('=')
				data_vals[var] = int(val)
			processed_parts.append(data_vals)

		s = 0
		for z, p in enumerate(processed_parts):
			label = get_assignment(p, instruction_queue, 'in')
			part_sum = 0
			if label == 'A':
				part_sum = p['x'] + p['m'] + p['a'] + p['s']
			#print(z, p, label, part_sum)
			s += part_sum

		print('Part1:', s)

		# Part 2
		#root = bigtree.Node.from_dict({'Name': 'in', })


		global ALL_TREE

		for i in instruction_queue:
			#print(i, instruction_queue[i])
			edges = []
			children = []
			state = None
			label = None
			for inst in instruction_queue[i]:
				if ':' in inst:
					state, label = inst.split(':')
				else:
					#state = ['not ' + e for e in edges.copy()]
					state = edges.copy()
					label = inst
				edges.append(state)
				children.append(label)

			#print(edges)
			#print(children)
			a = Tree(i)
			a.edges = edges
			a.children = children
			a.associate()
			ALL_TREE[i] = a

		accept = Tree('A')
		reject = Tree('R')
		ALL_TREE['A'] = accept
		ALL_TREE['R'] = reject

		#for a in all_tree:
		#p = dfs(ALL_TREE['in'], 'A')
		#print(p)
		p = exhaust(ALL_TREE['in'])

		valid_paths = []
		for q in p:
			if q[-1] == 'A':
				if q not in valid_paths:
					valid_paths.append(q)

		walks = []
		nodes_traveled = []
		for v in valid_paths:
			nodes = [ALL_TREE[rule] for rule in v]
			labels = [ALL_TREE[rule].label for rule in v]
			edges =	[nodes[z].edge_lookup[labels[z + 1]] for z in range(0, len(labels)-1)]
			walks.append(edges)
			nodes_traveled.append(nodes)

			#values = []
			#print(v)
			#print(edges)
			'''
			continue
			for e in edges:
				print(e)
				if '<' in e:
					var, val = e.split('<')
					values.append(int(val))
				elif '>' in e:
					var, val = e.split('>')
					values.append(4000 - int(val))
				elif '=' in e:
					var, val = e.split('=')
					values.append(1)

			print(values)
			'''
		# Flatten and standardize the number ranges per success
		for w in walks:
			print('W', w)
			#print([type(entry) == list for entry in w])
			filt = []
			for i in w:
				if type(i) != list:
					filt.append(i)
				else:
					for i2 in i:
						if '>' in i2:
							filt.append(i2.replace('>', '<'))
						elif '<' in i2:
							filt.append(i2.replace('<', '>'))
						elif '=' in i2:
							print('Should not see this', file=sys.stderr)
							pass
			
			print('F', filt)
		from operator import mul
		from functools import reduce
		#a = reduce(mul, [1350, 2005, 1415, 4000])
		#b = reduce(mul, [1350, 2005, 1337, 4000]) 
		#c = reduce(mul, [1350, 1909, 4000, 4000]) 
		#d = reduce(mul, [814, 1994, 2090, 2440])
		#e = reduce(mul, [552, 4000, 4000, 4000])
		#f = reduce(mul, [678, 1547, 4000, 4000])
		#g = reduce(mul, [2649, 963, 4000, 4000])
		#h = reduce(mul, [2649, 838, 1716, 4000])
		#print(sum([a, b, c, d, e ,f, g, h]))
		#167409079868000






if __name__ == '__main__':
	main()
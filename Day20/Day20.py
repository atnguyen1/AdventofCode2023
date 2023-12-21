import sys
import re
from collections import deque

test = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

class FlipFlop:
	def __init__(self, label, inputs=[]):
		self.label = label
		self.state = False
		self.children = []
		self.inputs = inputs

	def pulse(self, inputs, signal):
		if not signal:   # False
			self.state = not self.state

			if self.state:    # On
				# Send High Pulse to Children
				return (self.children, True)
			else:
				# Send Low Pulse to Children
				return (self.children, False)

	def __str__(self):
		return 'F_' + str(self.label) + '-' + ':'.join(self.children)

	def __repr__(self):
		return self.__str__()

class Conj:
	def __init__(self, label, inputs=[]):
		self.label = label
		self.inputs = inputs
		self.memory = [0] * len(inputs)
		self.children = []
		self.data = dict(zip(self.inputs, self.memory))


	def pulse(self, inputs, signal):
		idx = self.inputs.index(inputs)
		self.memory[idx] = signal
		if sum(self.memory) == len(self.memory):
			return (self.children, False)
		else:
			return (self.children, True)

	def __str__(self):
		return 'C_' + str(self.label) + '-' + ':'.join(self.children)

	def __repr__(self):
		return self.__str__()		

class Broadcaster:
	def __init__(self, label='broadcaster', inputs=[]):
		self.label = label
		self.children = []

	def pulse(self, inputs, signal):
		return (self.children, signal)

	def __str__(self):
		return str(self.label) + '-' + ':'.join(self.children)

	def __repr__(self):
		return self.__str__()


class State:
	def __init__(self, node_list):
		self.queue = deque()


def main():
	with open('20.input.txt', 'r') as fh:
		#data = fh.read().split('\n')
		data = test.split('\n')

		pulse_chain = []
		nodes = {}

		for d in data:
			node, target = d.split(' -> ')
			#print(node, target)
			if node[0] == '%':
				label = node[1:]
				if ',' in target:
					target = target.split(',')
				else:
					target = [target]
				a = FlipFlop(label)
				a.children = target
				nodes[label] = a
			elif node[0] == '&':
				label = node[1:]
				if ',' in target:
					target = target.split(',')
				else:
					target = [target]
				b = Conj(label)
				b.children = target
				nodes[label] = b				
			elif node == 'broadcaster':
				c = Broadcaster()
				if ',' in target:
					target = target.split(',')
				else:
					target = [target]
				c.children = target
				nodes['broadcaster'] = c	

		s = State(nodes)
		#for n in nodes:
	 	#	print(n, nodes[n])

if __name__ == '__main__':
	main()
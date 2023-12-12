import re
import sys
import numpy as np

pipe_lookup = {'|':[[0, 1, 0], [0, 0, 0], [0, 1, 0]],
			   '-':[[0, 0, 0], [1, 0, 1], [0, 0, 0]],
			   'L':[[0, 1, 0], [0, 0, 1], [0, 0, 0]],
			   'J':[[0, 1, 0], [1, 0, 0], [0, 0, 0]],
			   '7':[[0, 0, 0], [1, 0, 0], [0, 1, 0]],
			   'F':[[0, 0, 0], [0, 0, 1], [0, 1, 0]]}

pipe_lookup2 = {'|':[(-1, 0), (1, 0)],
			    '-':[(0, -1), (0, 1)],
			    'L':[(-1, 0), (0, 1)],
			    'J':[(-1, 0), (0, -1)],
			    '7':[(0, -1), (1, 0)],
			    'F':[(0, 1), (1, 0)],
			    '.':[(0, 0), (0, 0)]}

test = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF'''

test2 = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''

def find_connector(y, x, m, directions, visited):
	# Return list of connecting pipes
	connecting_pipes = []
	for d in directions:
		dy = y + d[0]
		dx = x + d[1]
		new_pipe = m[dy, dx]
		if (dy, dx) in visited:
			continue
		for d2 in pipe_lookup2[new_pipe]:
			ddy = dy + d2[0]
			ddx = dx + d2[1]

			if ddy == y and ddx == x:

				# pipe connects to current segment
				connecting_pipes.append((dy, dx))
				break

	#print(connecting_pipes)
	#for c in connecting_pipes:
	#	print(c, m[c])
	return connecting_pipes


def main():
	with open('10.input.txt', 'r') as fh:
		data = test.split('\n')
		#data = fh.read().split('\n')

		m = np.full((len(data) + 2, len(data[0]) + 2), dtype=str, fill_value='.')

		y = 1
		for row in data:
			row = row.rstrip()
			x = 1
			for char in row:
				m[y, x] = char
				x += 1
			y += 1

		starty, startx = np.where(m == 'S')
		#print(start, m[start])
		#print(m)
		#print(m.shape)

		# Find connecting pipes
		start_connectors = find_connector(starty[0], startx[0], m, [(-1, 0), (0, -1), (0, 1), (1, 0)], [(starty, startx)])
		pipe_loop = [(starty[0], startx[0])] + start_connectors

		connector_list = start_connectors

		#print(m)

		while connector_list != []:
			filt_connections = []
			for c in connector_list:
				new_connectors = find_connector(c[0], c[1], m, pipe_lookup2[m[c]], pipe_loop)
				for n in new_connectors:
					if n not in pipe_loop:
						filt_connections.append(n)
						pipe_loop.append(n)
			connector_list = filt_connections

		m_sparse = np.full((len(data) + 2, len(data[0]) + 2), dtype=str, fill_value='.')
		for p in pipe_loop:
			m_sparse[p] = m[p]

		#print(m_sparse)
		print('Part1:', len(pipe_loop), len(pipe_loop) / 2)

		print(m_sparse)
		in_out = np.full((len(data) + 2, len(data[0]) + 2), dtype=str, fill_value = '.')

		

		for y in range(1, len(data) + 1):
			v = [1 if (y, x) in pipe_loop else 0 for x in range(1, len(data) + 1)]

			for x in range(1, len(data[0]) + 1):

				
				

if __name__ == '__main__':
	main()
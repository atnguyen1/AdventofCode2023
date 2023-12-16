import re
import sys
import numpy as np

test = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.'''


def main():
	with open('13.input.txt', 'r') as fh:
		#data = fh.read().split('\n\n')
		data = test.split('\n')
		data = [data]

		processed = []
		for d in data:
			d2 = []
			for row in d:
				d2.append(['#' if c == '#' else '.' for c in row])
			d2 = np.array(d2, dtype=str)
			processed.append(d2)
			#print(d2)

		for p in processed:
			ydim, xdim = p.shape

			# Horizontal Scanning
			for y in range(0, ydim):
				v = p[y,:]
				new_p = np.vstack((p[:y,:], p[y+1:,:]))
				
				v2 = v.tolist()
				new_p2 = new_p.tolist()
				
				#print(v)
				#print(new_p.tolist())
				
				if v2 in new_p2:
					print(True)

					mirrored = new_p2.index(v2) + 1    
					border = [y + 1, mirrored + 1]     # Fix 0/1 start

					print(y, new_p2.index(v2), mirrored)

					while (border[0] < mirrored) and (border[0] + 1 != mirrored):
						border[0] = border[0] + 1
						border[1] = border[1] - 1
					print('Border', border)
				else:
					print(False)
				print(y)
				print(p)
				print(new_p)




if __name__ == '__main__':
	main()
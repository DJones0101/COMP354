# Darius Jones
# Floyd-Warshall Algorithm
# 11/27/2018
# Python3


import sys
import numpy as np
infinity = sys.maxsize

graph = {
	'a':[('c',3),],
	'b':[('a',2),],
	'c':[('b',7),('d',1),],
	'd':[('a',6)],
}

def floyd(graph):

	size = len(graph)
	row,column = size,size
	values = graph.values()
	grid = np.full(shape=(row,column),fill_value=0,dtype=int)

	for r in range(row):
		for c in range(column):

			node, weight = values[c][0][0],values[c][1][1]

			print(f" node : {node}, weight : {weight}")
			#grid[r,c] = 
	return


def main():
	floyd(graph)

if __name__ == '__main__':
	main()

# Darius Jones
# Floyd-Warshall Algorithm
# 11/27/2018
# Python3


import sys
import numpy as np
import pandas as pd
import math


graph = {
	'a':[('c',3),],
	'b':[('a',2),],
	'c':[('b',7),('d',1),],
	'd':[('a',6)],
}

# graph1 = {
# 	'a':[],
# 	'b':[('a',2),],
# 	'c':[('b',7),('d',1),],
# 	'd':[('a',6)],
# }

def floyd(graph):

	# Make a dict to matrix function!
	size = len(graph)
	row,column = size,size
	inf = np.inf
	nodes = list(graph)
	C = []
	B = np.full(shape=(row,column),fill_value=inf,dtype=float)
	hasSelfLoop = False

	for frm, values in graph.items():
		for to, weight in values:
			#print(f"frm : {frm}, to :{to}, weight :{weight}")
			C.append((weight,frm,to))
			if frm == to:
				hasSelfLoop = True

	# Note: inf means no edge connecting the nodes. 0 means no selfloop

	#The algorithm
	for weight, frm, to in C:
		r,c = nodes.index(frm),nodes.index(to)
		B[r,c] = weight

	if hasSelfLoop == False:
		np.fill_diagonal(B, 0)

	for k in range(size):
		for r in range(row):
			for c in range(column):
				B[r,c] = min(B[r,c], B[r,k] + B[k,c])

	return B


def display(graph):
	display = pd.DataFrame(graph)
	print(display)


def main():
	result = floyd(graph)
	display(result)

if __name__ == '__main__':
	main()

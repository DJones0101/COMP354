#!/usr/bin/env python3

# Darius Jones
# 10/31/2018
# COMP 354
# Python 3.6


import numpy as np
import pandas as pd


def isShuffle(u,v,w):

	row = len(u) + 1
	column = len(v) + 1

	assert (row-1) + (column-1) == len(w)

	grid = np.full(shape=(row,column),fill_value=False,dtype=bool)

	for i in range(row):
		if u[:i] == w[:i]:
			grid[i,0]=True

	for j in range(column):
		if v[:j] == w[:j]:
			grid[0,j] = True

	for i in range(row):
		for j in range(column):
			if grid[i-1,j] == True and w[:i+j-1] + u[i-1] == w[:i+j]:
				grid[i,j] = True
			elif grid[i,j-1] == True and w[:i+j-1] + v[j-1] == w[:i+j]:
				grid[i,j] = True


	print(pd.DataFrame(grid))

	if False in grid.diagonal():
		return False

	return True


def main():

	u = "01101110"
	v = "10101000"
	w = "0110110011101000"
	result = isShuffle(u,v,w)

	print(f"Is w a Shuffle ? {result}")


if __name__ == '__main__':
	main()
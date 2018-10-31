#!/usr/bin/env python3

# Darius Jones
# 10/31/2018
# COMP 354
# Python 3.6

# Dynamic programming computes a data structure of partial soluions.
# We need to create a grid, which represents these partial solutions.
# So, I'm guessing the highlighted equation on page 86 explains much of the algorithm.
# I just don't know how to translate that into code at the moment.

import numpy as np
import pandas as pd


def isShuffle(u,v,w):

	row = len(u) + 1
	column = len(v) + 1
	grid = np.zeros(shape=(row,column))

def showGrid(grid):
	print(pd.DataFrame(grid))

	


def main():
	u = "000"
	v = "111"
	w = "010101"
	isShuffle(u,v,w)


if __name__ == '__main__':
	main()
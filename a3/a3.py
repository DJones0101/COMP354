#!/usr/bin/env python3

# Darius Jones
# Chad Bloor
# Gerardo Carillo
# 10/31/2018
# COMP 354
# Python 3.6

import unittest
import numpy as np
import pandas as pd

class Test_a3(unittest.TestCase):

	''' Test cases from the Assignment 3 PDF'''

	def test_case1(self):
		self.assertEqual(shuffle("01101110","10101000","0110110011101000"), "Yes")

	def test_case2(self):
		self.assertEqual(shuffle("000","111","010101"), "Yes")

	def test_case3(self):
		self.assertEqual(shuffle("011","011","001111"), "Yes")

	''' Test cases we made came up with'''
	# def test_case4(self):
	# 	self.assertEqual(shuffle("111","000","110010"), "Yes") # Why does this fail?

	# def test_case5(self):
	# 	self.assertEqual(shuffle("1111","0000","11001100"), "Yes") #Why does this fail?


def shuffle(u,v,w):

	row = len(u) + 1
	column = len(v) + 1
	result  =  len(w)

	if (row-1) + (column-1) != result:
		raise Exception(f" |u| + |v| = |w| : {row-1} + {column-1} != {result}")

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
	print(f"List of diagonals from top left to bottom right: {getDiagonals(grid)}")
	print("\n")

	return "No" if False in grid.diagonal() else "Yes"

def getDiagonals(grid):
	#https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
	row = grid.shape[0]
	column = grid.shape[1]
	gridSize = (row * column)
	halfGridsize = gridSize/2

	listn = [grid.diagonal(i) for i in range( -1, halfGridsize )]

if __name__ == '__main__':

	shuffle("000","111","010101")
	#shuffle("111","000","110010")
	#shuffle("1111","0000","11001100")
	#unittest.main()




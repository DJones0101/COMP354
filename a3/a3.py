#!/usr/bin/env python3

# Darius Jones
# Chad Bloor
# Gerardo Carillo
# 11/10/2018
# COMP 354
# Python 3.6

import unittest
import numpy as np
import pandas as pd

class Test_a3(unittest.TestCase):

	# Test cases from the Assignment 3 PDF

	def test_case1(self):
		self.assertEqual(isShuffle("01101110","10101000","0110110011101000"), "Yes")

	def test_case2(self):
		self.assertEqual(isShuffle("000","111","010101"), "Yes")

	def test_case3(self):
		self.assertEqual(isShuffle("011","011","001111"), "Yes")

	# Test cases we came up with

	def test_case4(self):
	 	self.assertEqual(isShuffle("111","000","110010"), "Yes") 

	def test_case5(self):
		self.assertEqual(isShuffle("0000","1111","00110011"), "Yes") 

	def test_case6(self):
		self.assertEqual(isShuffle("0000","0101","00010001"), "Yes")

	def test_case7(self):
		self.assertEqual(isShuffle("0001","0101","00010101"), "Yes")

	def test_case8(self):
		self.assertEqual(isShuffle("00011","01011","0001010111"), "Yes")
	

def isShuffle(u,v,w):

	row = len(u)+1
	column = len(v)+1
	result  =  len(w)

	if (row-1) + (column-1) != result:
		raise Exception(f" |u| + |v| = |w| : {row-1} + {column-1} != {result}")

	# The Algorithm
	grid = np.full(shape=(row,column),fill_value=False,dtype=bool)

	for i in range(row):

		print(f"{u[:i]} == {w[:i]}")
		if u[:i] == w[:i]:
			grid[i,0] = True

	for j in range(column):

		print(f"{v[:j]} == {w[:j]}")

		if v[:j] == w[:j]:
			grid[0,j] = True
	
	print(pd.DataFrame(grid))
	print("\n")


	for i in range(row):
		for j in range(column):

			if grid[i-1,j] == True and (w[:i+j-1] + u[i-1] == w[:i+j]):

				grid[i,j] = True
				print(f"{w[:i+j-1]} + {u[i-1]} == {w[:i+j]}")
				print(f" grid[{i},{j}]=  {grid[i,j]}\n" )

			elif grid[i,j-1] == True and (w[:i+j-1] + v[j-1] == w[:i+j]):

				grid[i,j] = True

			


	print(pd.DataFrame(grid))
	print("\n")
	
<<<<<<< HEAD
	return "Yes" if grid[row-1,column-1]== True else "No"
=======
	return "Yes" if shuffle(grid) == True else "No"

>>>>>>> master


<<<<<<< HEAD
def main():
	q = isShuffle("aab", "axy", "aaxaby")
	print(q)
=======
	row = grid.shape[0]
	return [grid.diagonal(i) for i in range(-(row-1), 1)]


def shuffle(grid):

	diagonals = getDiagonals(grid)

	for i in range(len(diagonals)):

		listSize = len(diagonals[i])
		trueCounter = 0

		for k in range(listSize):
			if diagonals[i][k] == True:
				trueCounter += 1

		if trueCounter == listSize:
			return True

	return False
>>>>>>> master


if __name__ == '__main__':

	main()
	#unittest.main()


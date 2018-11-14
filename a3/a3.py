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

	# # Test cases from the Assignment 3 PDF

	# def test_case1(self):
	# 	self.assertEqual(isShuffle("01101110","10101000","0110110011101000"), "Yes")

	# def test_case2(self):
	# 	self.assertEqual(isShuffle("000","111","010101"), "Yes")

	# def test_case3(self):
	# 	self.assertEqual(isShuffle("011","011","001111"), "Yes")

	# # Test cases we came up with

	# def test_case4(self):
	#  	self.assertEqual(isShuffle("111","000","110010"), "Yes") 

	# def test_case5(self):
	# 	self.assertEqual(isShuffle("0000","1111","00110011"), "Yes") 

	# def test_case6(self):
	# 	self.assertEqual(isShuffle("0000","0101","00010001"), "Yes")

	# def test_case7(self):
	# 	self.assertEqual(isShuffle("0001","0101","00010101"), "Yes")

	# def test_case8(self):
	# 	self.assertEqual(isShuffle("00011","01011","0001010111"), "Yes")
	
	def test_case8(self):
	 	self.assertEqual(isShuffle("11","00","1100"), "Yes")

def isShuffle(u,v,w):

	row = len(u)+1
	column = len(v)+1
	result  =  len(w)

	if (row-1) + (column-1) != result:
		raise Exception(f" |u| + |v| = |w| : {row-1} + {column-1} != {result}")

	# The Algorithm
	grid = np.full(shape=(row,column),fill_value=False,dtype=bool)

	for i in range(row):


		if v[:i] == w[:i]:
			grid[0,i] = True
	
	for j in range(column):

		if u[:j] == w[:j]:
			grid[j,0] = True


	for i in range(row):
		for j in range(column):

			if grid[i-1,j] == True and (w[:i+j-1] + u[i-1] == w[:i+j]):

				grid[i,j] = True

			elif grid[i,j-1] == True and (w[:i+j-1] + v[j-1] == w[:i+j]):

				grid[i,j] = True

	display(grid,u,v)

	return "Yes" if grid[row-1,column-1]== True else "No"

def display(grid,u,v):
	#https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
	grid = np.rot90(grid)


	


if __name__ == '__main__':

	unittest.main()


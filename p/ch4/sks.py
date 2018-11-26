# Algorithm 4.3 Simple Knapsack
#

import numpy as np
import pandas as pd
import unittest

def ks(numOfObjects, weightsList):

	row = numOfObjects + 1
	column = len(weightsList) + 1 # also the capacity
	S = [True] + [False for i in len(1, weightsList)]

	grid = np.full(shape=(row,column),fill_value=False,dtype=bool)

	for i in range(1, row):
		for j in range(column,-1,-1):
			if j >= weightsList[i] = True and S(j - weightsList[i]) == True:
				S[j] = True

	print(pd.DataFrame(data=grid))

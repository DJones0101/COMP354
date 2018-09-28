#!/usr/bin/env python3

# Darius Jones
# 9/20/2018
# COMP 354
# Python 3.6.4


import math, sys, random
from matplotlib import pyplot as plt


def xgcd(b, a):

	if (b <= 0 or a <= 0) or (b != int(b) or a != int(a)):
		raise ValueError("Invalid inputs   " + str(a) + " " + str(b))

	x = 1  # runs 1 time for each assignment, so 4 times in total
	y = 0
	last_x = 0
	last_y = 1

	steps = 4

	while a > 0:  #runs n times, everything in the loop also runs n times so, 8n in total

		q, b, a = (b // a), a, (b % a)
		x, last_x = last_x, x - q * last_x
		y, last_y = last_y, y - q * last_y
		#print("a = " + str(a) +" b = " + str(b) + " x = " + str(x) + " last_x = " + str(last_x) + " y = " + str(y) + " last_y = " + str(last_y))
		steps += 8

	return b, x, y, steps


def test_algo(b, a):

	# a(s) + b(t) = gcd(a,b)

	gcd, s, t = xgcd(a, b)

	if ((a * s) + (b * t) == gcd):

		return True
	else:
		return False
		

def getBitsList(lenght):

	list1 = []

	for i in range(1, (2 ** 10)):
		x = "{0:b}".format(i)
		if (len(x) == lenght) and (x != 0):
			list1.append(i)
	return list1

def calculateAverage(bitslist):


	# We should modify this method to return list of averages for the length of bits.
	# This will be used to used to populate the y-axis of the graph

	steps = 0
	b =  0x7FFFFFFF # 31 bits, we will keep this value constant. becaue the value of (a) is doing the work in the algorithm.
	total = 0
	print(bitslist)
	for i in range(len(bitslist)):

		#b =  blist[i]#random.randint(1, 100)
		a = bitslist[i]
		print("A = %d" %(a))
		gcd, s, t, steps = xgcd(b, a) # the calculation of the steps will be used to  populate the x-axis of the graph.

		total += steps


	average = total / len(bitslist)

	return average


def main():

	# we will get rid of this 

	# turn into an array or arrays . we need to go up to N bits meaning 100 or 200 bits.
	# becasue the ways you can represent a value n is 2^n, we need to  make a cut off of numbers 
	# that wil be in the list. say at bits of len 15 we limit the array to len  2^14.


	# this will be changed to a method that generates the numbers with len n from (1 to say 100)
	# and returns a list of those numbers

	x = []
	y = []
	bitList = []

	for i in range(1,100):
		x.append(i)
	
	index = 0
	index1 = 0
	count = 1

	for i in range(1, 100):
		bitList.append(getBitsList(count))
		count += 1


	for i in range(1, 100):
		 y.append(calculateAverage(bitList[index1]))
		 index1 += 1
	

	plt.scatter(x,y)
	plt.title("Relationship between number of bits and number of steps")
	plt.ylabel("Number of steps ")
	plt.xlabel("Number of bits")
	plt.show()


if __name__ == "__main__":
	main()

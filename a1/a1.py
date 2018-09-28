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
		
	

def calculate(bits, bitslist):


	# We should modify this method to return list of averages for the length of bits.
	# This will be used to used to populate the y-axis of the graph
	if not bitslist:
		print("list is empty")
		return

	total = 0

	print("-------------- %d bits ----------------------" %(bits))

	print(bitslist)

	steps = 0
	b =  0x7FFFFFFF # 31 bits, we will keep this value constant. becaue the value of (a) is doing the work in the algorithm.

	for i in range(len(bitslist)):

		#b =  blist[i]#random.randint(1, 100)
		a = bitslist[i]
		gcd, s, t, steps = xgcd(b, a) # the calculation of the steps will be used to  populate the x-axis of the graph.

		total += steps
		print("b = %d, a = %d " % (b, a))
		print("steps =  %d\n" % (steps))

	average = total / len(bitslist)

	print("Average steps = %d" %(average))
	return average

def main():

	# we will get rid of this 
	twobits = []
	threebits = []
	fourbits = []
	fivebits = []
	sixbits = []
	sevenbits = []
	eightbits = []
	ninebits = []
	tenbits = []



	# turn into an array or arrays . we need to go up to N bits meaning 100 or 200 bits.
	# becasue the ways you can represent a value n is 2^n, we need to  make a cut off of numbers 
	# that wil be in the list. say at bits of len 15 we limit the array to len  2^14.


	# this will be changed to a method that generates the numbers with len n from (1 to say 100)
	# and returns a list of those numbers
	for i in range(0, 0xFFF):
		x = "{0:b}".format(i)
		if len(x) == 2:
			twobits.append(i)
		elif len(x) == 3:
			threebits.append(i)
		elif len(x) == 4:
			fourbits.append(i)
		elif len(x) == 5:
			fivebits.append(i)
		elif len(x) == 6:
			sixbits.append(i)
		elif len(x) == 7:
			sevenbits.append(i)
		elif len(x) == 8:
			eightbits.append(i)
		elif len(x) == 9:
			ninebits.append(i)
		elif len(x) == 10:
			tenbits.append(i)
		elif len(x) == 11
			elevenbits.append(i)
		elif len(x) == 12
			twelvebits.append(i)


	x = [2,3,4,5,6,7,8,9,10]



	y = [calculate(2, twobits),
		calculate(3, threebits),
		calculate(4, fourbits),
		calculate(5, fivebits),
		calculate(6, sixbits),
		calculate(7, sevenbits),
		calculate(8, eightbits),
		calculate(9, ninebits),
		calculate(10, tenbits)
		]

	plt.scatter(x,y)
	plt.title("Relationship between number of bits and number of steps")
	plt.ylabel("Number of steps ")
	plt.xlabel("Number of bits")
	plt.show()


if __name__ == "__main__":
	main()

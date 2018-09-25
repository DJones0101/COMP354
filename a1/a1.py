#!/usr/bin/env python

# Darius Jones
# 9/20/2018
# COMP 354
# Python 3.6.4

# The runtime of euclid's extended algorithm depends binary encoding of a, since the while loop conditions depends on a. The
# runtime polynomial is 8n + 4, where n = 2^log2(a binary length). To run the experiment we run the runtime method
# on a group of numbers and draw a conculsion that the runtime is dependant on a's binary string lenght. For example every
# integer with a binary string of lenght 10 the runtime is 85 and  for 9 the runtime is 77 and so on.

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
		
	

def calculate( bits, bitslist):

	if not bitslist:
		print("list is empty")
		return

	total = 0

	print("-------------- %d bits ----------------------" %(bits))

	print(bitslist)

	steps = 0
	blist = bitslist[::-1]

	for i in range(len(bitslist)):

		b =  blist[i]#random.randint(1, 100)
		a = bitslist[i]
		gcd, s, t, steps = xgcd(b, a)

		total += steps
		print("b = %d, a = %d " % (b, a))
		print("steps =  %d\n" % (steps))

	average = total / len(bitslist)

	print("Average steps = %d" %(average))
	return average

def main():

	twobits = []
	threebits = []
	fourbits = []
	fivebits = []
	sixbits = []
	sevenbits = []
	eightbits = []


	for i in range(0, 200000):
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

	x = [2,3,4,5,6,7,8]



	y = [calculate(2, twobits),
		calculate(3, threebits),
		calculate(4, fourbits),
		calculate(5, fivebits),
		calculate(6, sixbits),
		calculate(7, sevenbits),
		calculate(8, eightbits)]

	plt.plot(x,y)
	plt.title("Relationship between number of bits and number of steps")
	plt.ylabel("Number of steps ")
	plt.xlabel("Number of bits")
	plt.show()


#print ("total = " + str(twobits_total))

if __name__ == "__main__":
	main()

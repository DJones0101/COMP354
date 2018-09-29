#!/usr/bin/env python3

# Darius Jones
# Chad Bloor
# Gerardo Carillo
# 9/28/2018
# COMP 354
# Python 3.6.4


import math, random
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

	return steps
	

def calculateAverage(length):

	print("-------------- %d length ----------------------" %(length))

	b =  generate_string(200)
	a = generate_string(length)
	total = 0 
	steps = 0
	runs = 0

	for i in range(0, 10):

		steps = xgcd(int(b,2), int(a,2)) # the calculation of the steps will be used to  populate the x-axis of the graph.

		total += steps
		print("a = %d, b = %d" %(int(a,2), int(b,2)))
		print("steps =  %d\n" % (steps))
		a = replace_random(a)
		runs += 1

	average = total / runs

	print("Average steps = %d" %(average))
	return average


def replace_random(seq):
	seq = list(seq)
	toReplace = random.randint(1,len(seq)-1)
	seq[toReplace] = "0"
	return "".join(seq)

def generate_string(length):
	listn = ""
	for i in range(0, length):
		listn += "1"
	return listn

def main():

	x = []
	y = []
	for i in range(2, 100):
		r = calculateAverage(i)
		x.append(i)
		y.append(r)


	plt.scatter(x,y)
	plt.title("Relationship between number of bits and number of steps")
	plt.ylabel("Number of steps")
	plt.xlabel("Binary length")
	plt.show()


if __name__ == "__main__":
	main()

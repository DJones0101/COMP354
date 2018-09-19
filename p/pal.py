# Darius Jones
# 9/9/2018
# COMP 354
# 1.3
import math, sys


def pal(string):

	
	i = 0
	n = len(string)

	#check precoditions
	assert n >= 1 and isinstance(string, str), "Invalid Input"

	while i < math.floor(n/2) :

		if string[i] != string[n - i -1]:
			return False

		i = i+1

	return True


def pal_1(string): #problem 1.12
	#reverse the string with slicing , check for equality
	#[start:stop:step] omitted means start/stop
	return str(string) == string[::-1]


word = "tumor"

print("is " + word + " a palindrome? "+ str(pal_1(word)))


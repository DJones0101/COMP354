# Darius Jones
# 9/2/2018
# Division 1.1 from the book

import sys

def div(x,y):

	#check precondtions
	if x<=0 and y<0 and x != int(x) and y != int(y):
		raise ValueError("Invalid inputs for Division.")

	#algorithm
	quotient = 0
	remainder = x

	while y<= remainder:
		remainder = remainder - y
		quotient = quotient + 1

		print("remainder = " +str(remainder) + " quotient = "+ str(quotient))
		
	return quotient, remainder

# As per the book the (post condition/ loop invariant) is x = (quotient * y) + remainder and the remainder >= 0
# The (post condition/ loop invariant) is used to check for correctness


print( " x = 25 and y = 3 " + "then quotient and remainder are respectively "+str(div(25,3)))
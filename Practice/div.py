# Darius Jones
# 9/2/2018
# Division 

import sys

def div(x,y):

	#check precondtions
	if x<=0 and y<0 and x != int(x) and y != int(y):
		raise ValueError("Invalid inputs for Division.")

	#algorithm
	quotient = 0
	remainder = x

	while y<= remainder:
		remainder -= y
		quotient += 1
		
return quotient, remainder


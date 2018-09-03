# Darius Jones
# 9/2/2018
# Division 1.1 from the book

import sys

def div(x,y):

	#check precondtions
	if x<=0 and y<0 and x != int(x) and y != int(y):
		raise ValueError("Invalid inputs for Division.")

	#algorithm
	quotient = 0  #--- 1
	remainder = x #---1

	while y<=remainder: #--- n
		remainder = remainder - y #---n
		quotient = quotient + 1 #---n

		print("remainder = " +str(remainder) + " quotient = "+ str(quotient)) #---n
		
	return quotient, remainder #---1

	#runtime is f(n) = 4n+3, O(n)

# As per the book the (post condition/ loop invariant) is x = (quotient * y) + remainder and the remainder >= 0
# The (post condition/ loop invariant) is used to check for correctness


# We need to prove this by induction  x = (quotient * y) + remainder and the remainder >= 0
# Base case: (before the loop starts) quotient = 0, remainder = x, so we have 
# x = (0 * y) + r which is true.
# Inductive step we one more iteration x = [(qoutient + 1) * y] + remainder - y, which holds true.  
# So far we have proved partial correctness, we must show termination to show full correctness.
# By LNP (Least Number Principle) the remainder is being reducded by y every iteration, therfore the loop
# condition y<=remainder will eventually not hold. Full correctness has been shown.


print( " x = 25 and y = 3 " + "then quotient and remainder are respectively "+str(div(25,3)))
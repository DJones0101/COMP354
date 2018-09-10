# Darius Jones
# 9/2/2018
# Division 1.1 from the book


def div(x,y):

	#check precondtions
	if (x<0 and y<=0) and (x != int(x) and y != int(y)):
		raise ValueError("Invalid inputs for Division.")

	#algorithm
	q = 0  #--- 1
	r = x #---1

	while y<=r: #--- n
		r = r - y #---n
		q = q + 1 #---n

		print("r = " +str(r) + " q = "+ str(q)) #---n problem 1.5
		
	return q, r #---1


def div_1(x,y): #problem 1.5

	q, r = 0, 0

	if x < 0 or y < 0:

		q, r = div(abs(x), abs(y))
		return -q, -r 

	return div(x,y)






# As per the book the (post condition/ loop invariant) is x = (quotient * y) + remainder and the remainder >= 0
# The (post condition/ loop invariant) is used to check for correctness


# We need to prove this by induction  x = (quotient * y) + remainder and the remainder >= 0
# Base case: (before the loop starts) quotient = 0, remainder = x, so we have 
# x = (0 * y) + r which is true.
# Inductive step we one more iteration x = [(qoutient + 1) * y] + remainder - y, which holds true.  
# So far we have proved partial correctness, we must show termination to show full correctness.
# By LNP (Least Number Principle) the remainder is being reducded by y every iteration, therfore the loop
# condition y<=remainder will eventually not hold. Full correctness has been shown.

# problem 1.3 runtime is f(n) = 3n+3, O(n), as is from the book

# problem 1.4 changing the preconditons to x >= 0 and y >0 and x,y are contained in integers positive and negative isn't correct. The
# algorithm doen't work on negative numbers and in the case when x is positive and y is negative the algorithm doesn't terminate. The
# same is true for y >= 0 and x, y are contained in integers positive and negative.

# problem 1.5 see div_1




x = -200
y =  10
print( " x = "+ str(x) +" and y = "+ str(y) + " then quotient and remainder are respectively "+str(div_1(x,y)))
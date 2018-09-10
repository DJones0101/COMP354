
# Darius Jones
<<<<<<< HEAD
# 9/9/2018
# COMP 354
# 1.2



def gcd(a, b):

	#check preconditons
	if a < 0 and b < 0 and a != int(a) and b != int(b):
		print("Invalid input")
		return

	m = a
	n = b
	r = m % n
	 	
	while r > 0:
		m = n
		n = r
		r = m % n
		
	return n
=======
# 8/29/2018
# COMP 354


def xgcd(a, b):

	#check precondtions
	if a<=0 and b<=0 or a != int(a) or b != int(b):
		raise ValueError("Invalid inputs")

	m = int(a)
	n = int(b)
	r = m % n 

	while r > 0:
		q = m/n
		m = n
		n = r
		r = m % n

		
	return n

gcd = xgcd(56,15)

print( " GCD of 56 and 15 is " + str(gcd))
>>>>>>> master

a = 56
b = 15

print("a = " + str(a) +" b = " + str(b) + " gcd = " + str(gcd(a,b)))





# Darius Jones
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






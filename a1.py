'''
Darsius Jones
8/29/2018
COMP 354

'''

def gcd(m, n):

	while n > 0:
		(m, n) = (n, m % n)
	return m


def xgcd(m, n):

	if gcd(m, n) > 0:
		



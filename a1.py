'''
Darius Jones
8/29/2018
COMP 354

'''

def xgcd(m, n):

	while n > 0:
		(m, n) = (n, m % n)
	return m









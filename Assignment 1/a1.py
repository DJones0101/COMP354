
# Darius Jones
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

a = 56
b = 15

print("a = " + str(a) +" b = " + str(b) + " gcd = " + str(gcd(a,b)))




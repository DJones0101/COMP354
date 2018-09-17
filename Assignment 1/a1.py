
# Darius Jones
# 9/9/2018
# COMP 354
# Python 3.6.5


import math, sys

def xgcd(b, a):


    x = 1 
    y = 0
    last_x = 0
    last_y = 1


    while a != 0:

        q, b, a = math.floor(b/a), a, (b % a)
        x, last_x = last_x, x - q * last_x
        y, last_y = last_y, y - q * last_y
        

        print("a = " + str(a) +" b = " + str(b) + " x = " + str(x) + " last_x = " + str(last_x) + " y = " + str(y) + " last_y = " + str(last_y))
       
    return  b, x, y

a = 56
b = 15

print("a = " + str(a) +" b = " + str(b) + " gcd = " + str(xgcd(a,b)))




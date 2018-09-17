
# Darius Jones
# 9/9/2018
# COMP 354
# Python 3.6.5


# The runtime depends binary encoding of a. the runtime polynomial is 8n + 4, where n = 2^log2(|a| binary len). To run the expiriment
# We run the algo on a group of numbers, calculate the runtime using the polynomial and draw a conclusion based on the length of the 
# their binary strings.


import math, sys

def xgcd(b, a):


    x = 1 
    y = 0
    last_x = 0
    last_y = 1
    


    while a > 0:

        q, b, a = math.floor(b/a), a, (b % a)
        x, last_x = last_x, x - q * last_x
        y, last_y = last_y, y - q * last_y
       
         

        #print("a = " + str(a) +" b = " + str(b) + " x = " + str(x) + " last_x = " + str(last_x) + " y = " + str(y) + " last_y = " + str(last_y))
    run = run + 1
    print("runtime = " + str(run))
    return  b, x, y

a = 56
b = 15

print("a = " + str(a) +" b = " + str(b) + " gcd = " + str(xgcd(a,b)))




#!/usr/bin/env python3

# Darius Jones
# 9/19/2018
# COMP 354
# Python 3.6.4


# The runtime of euclid's extended algorithm depends binary encoding of min(a,b). The runtime polynomial is 8n + 4, where n = 2^log2(min(a,b) binary len). To run the expiriment
# We run the runtime method on a group of number and draw a conculsion that the runtime is dependant on the lenght of the smaller number's binary string. For example every integer
# with a binary string of lenght 10 has a runtime of 85, and 9 the runtime is 77 ans so on.

import math, sys, random

def xgcd(b, a):


    x = 1  # runs 1 time for each assignment, so 4 times in total
    y = 0
    last_x = 0
    last_y = 1
    
    while a > 0:   #runs n times, everything in the loop also runs n times so, 8n in total

        q, b, a = (b//a), a, (b % a)
        x, last_x = last_x, x - q * last_x
        y, last_y = last_y, y - q * last_y   
        #print("a = " + str(a) +" b = " + str(b) + " x = " + str(x) + " last_x = " + str(last_x) + " y = " + str(y) + " last_y = " + str(last_y))
    
    return  b, x, y


def test_algo(a,b):

    # a(s) + b(t) = gcd(a,b)

    gcd, s, t = xgcd (a,b)

    if( (a * s) + (b * t) == gcd ):

        print("Testing " + str(a) +"*"+ str(s) + " + "+ str(b) +"*"+ str(t) +"="+ str(gcd) + " PASS!!")
    else :
        print("Testing " + str(a) +"*"+ str(s) + " + "+ str(b) +"*"+ str(t) +"="+ str(gcd) + " FAIL!!")
    pass



def runtime(a,b):

    # run time polynomial 8(n) + 4
    # where n = 2^log2(x), where x is the len of the min(a,b) binary string 

    m = a
    x = "{0:b}".format(m)
    n = 2 ** math.log(len(x),2)
    runtime = (8 * n) + 4
    
    print("Min of " + " ("+str(a)+","+str(b) +") "+ str(m))
    print("Binary lenght of " + str(m)+" = " + str(len(x)))
    print("Runtime = " + str(math.ceil(runtime)))
    pass


def main():

    for i in range(0,100):

        a = random.randint(0, 1000)
        b = random.randint(0, 1000)

        #test_algo(a,b)
        runtime(a,b)
        print("\n")
    pass


if __name__ == "__main__":
    main()







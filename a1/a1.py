#!/usr/bin/env python3

# Darius Jones
# 9/20/2018
# COMP 354
# Python 3.6.4


# The runtime of euclid's extended algorithm depends binary encoding of a, since the while loop conditions depends on a. The 
# runtime polynomial is 8n + 4, where n = 2^log2(a binary length). To run the experiment we run the runtime method 
# on a group of numbers and draw a conculsion that the runtime is dependant on a's binary string lenght. For example every 
# integer with a binary string of lenght 10 the runtime is 85 and  for 9 the runtime is 77 and so on.

import math, sys, random

def xgcd(b, a):


    if (b<=0 or a<=0) or (b!=int(b) or a!=int(a)):
        raise ValueError("Invalid inputs   " + str(a) +" "+ str(b))


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


def test_algo(b,a):

    # a(s) + b(t) = gcd(a,b)

    gcd, s, t = xgcd (a,b)

    if( (a * s) + (b * t) == gcd ):

        print("Testing " + str(a) +"*"+ str(s) + " + "+ str(b) +"*"+ str(t) +"= "+ str(gcd) + " PASS!!")
    else :
        print("Testing " + str(a) +"*"+ str(s) + " + "+ str(b) +"*"+ str(t) +"= "+ str(gcd) + " FAIL!!")
    pass



def runtime(b,a):

    # run time polynomial 8(n) + 4
    # where n = 2^log2(x), where x is the len of the min(a,b) binary string

    m = a
    x = "{0:b}".format(m)
    n = 2 ** math.log(len(x),2)
    runtime = (8 * n) + 4
    print("Binary lenght of " + str(m)+" = " + str(len(x)))
    print("Runtime = " + str(math.ceil(runtime)))
    test_algo(b,a)
    print("\n")
    pass


def main():

    for i in range(0,1000):

        a = random.randint(1, 1000)
        b = random.randint(1, 1000)

        #test_algo(a,b)
        runtime(b,a)        

    pass


if __name__ == "__main__":
    main()







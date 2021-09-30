#!/usr/bin/env python

import numpy as np
import sys
from timeit import default_timer

'''
Purely python based version of the primes script. Applies the same method as the other scripts by checking each number 
and voiding each number divisible with it starting at the square. 
'''

n =100 #int(sys.argv[1])


def primes_python(n):
    prob_primes = np.zeros(n)
    for i in range(n):
        prob_primes[i] = 1

    prob_primes[0] = 0
    prob_primes[1] = 0
    for i in range(len(prob_primes)):
        if prob_primes[i] != 0:
            print(i, end=" ")
            j = i*i
            while j < n:
                prob_primes[j] = 0
                j += i


t_start = default_timer()

if __name__ == "__main__":
    primes_python(n)

t_end = default_timer()
print("Execution time is:", t_end-t_start)

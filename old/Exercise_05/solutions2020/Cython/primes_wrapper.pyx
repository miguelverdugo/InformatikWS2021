
from cpython.pycapsule cimport *

cdef extern from "primeslib.h":
    void primes_c(long n)

def primes(n):
    return primes_c(n)
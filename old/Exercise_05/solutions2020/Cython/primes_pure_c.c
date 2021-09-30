//
// Created by gerald on 13.08.19.
//

/*
Pure C-version of the Primes-script, that is used for the cython implementation in combination with the header file
primeslib.h. Note that this script only prints the prime numbers instead of creating an array containing them in order
to keep things beginner friendly. If Roland talks about pointers and arrays in C, I can edit a defined output. If that's
not the case, then I'll still add some form of output since it won't do much good if people learn how to write C
extensions without learning how to return values from their functions.
*/


#include <stdbool.h>
#include <stdio.h>
#include "primeslib.h"

void primes_c(long n) {
    bool possible_prime[n];

    for(long i = 0; i<n; i++){
        possible_prime[i] = 1;
    }
    possible_prime[0] = 0;
    possible_prime[1] = 0;

    for(long i = 0; i<n; i++){
        if(possible_prime[i] != false) {
            printf("%li \n", i);
            for(long j = i*i; j<n; j = j + i) {
                possible_prime[j] = false;
            }
        }
    }
    return;
};


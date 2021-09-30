import numpy as np
import timeit


N = 10**3
# Time from here
start_time = timeit.default_timer()
daten=[]
for i in range(0,N) :
    daten.append(i**0.5)

time_2 = timeit.default_timer() - start_time

print(time_2)
# to here
# and from here


start_time = timeit.default_timer()
daten = np.sqrt(np.arange(0,N))
# to here
time_2 = timeit.default_timer() - start_time
print(time_2)


# With N=10**3 the times are similar

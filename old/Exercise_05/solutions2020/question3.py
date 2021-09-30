import numpy as np

"""
important difference is numpy arrays can only contain one type of data

Shape is an important aspect, e.g. all rows must have same length

they contain by default many mathematical methods for matrix operations, etc
"""

# Creation of arrays

array1 = np.array([1,2,3])

array2 = np.arange(0,10, 1)

array3 = np.linspace(0, 10, 5)

array4 = np.ones(20).reshape(4,5)


print(np.sqrt(array1))


print(np.log10(array2))

# simple just a line!

# Broadcasting are rules for operations between arrays of disimilar shapes


# simple example

print(array5 = 5*array1)

# more complex

print(array4 *array3)


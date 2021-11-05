# Informatics for Astronomers - WS2021

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Andreas Schanz**

# Exercise sheet 3 - Python functions and numpy

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Write a simple python script that takes a distance in lightyears and returns
   that distance in both parsec and kilometers. In the case of parsec, the script
   should return the proper SI notation (e.g. Gpc, Mpc, kpc depending on the distance).
   The distance in kilometers shall be written in proper scientific notation. Make use of
   functions in each case

2. Write a Python function that calculates the entropy of a string. That function
   should be placed within a script that reads the input from the command-line.

3. The following snippet creates a list of 100 random numbers between 0 and 100.

    ```python

       import random

       random_list = [random.choices(range(100))[0] for i in range(100)]
    ```

      write three functions that return 1) maximum value 2) the minimum  and 3)
      which values are repeated and how many times each.

4. Do the same but using the `numpy` library build-in functions, including the
   creation of the array (that is, do not use the snippet above).

5. Create a 2D `numpy` array of $100 \times 100$ elements filled with zeros.
   Replace inner of $50 \times 50$ elements with ones.
   Calculate the mean and the median of this new array. Display it with `matplotlib`

6. Create a simple function that evaluates a `numpy` array (between `(0,10)` with
   a spacing of `0.1`). That function should be able to take as parameter any (simple)
   mathematical function available in the `numpy` library (e.g. `sqrt`, `sin`, `log`, etc).
   Return and plot the resulting array with `matplotlib`.

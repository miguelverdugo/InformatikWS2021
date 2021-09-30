  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 7 - Python lists, functions and C

---

> _Your preparation of exercises should include two aspects:_
>
> _(1) Try to present exercises in a way that everyone can follow (even if that
> person didn’t do the exercise at all), so please explain all the (vital) parts of
> your solution in a slow and comprehensive way._
>
> _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._
>
---

1. In Exercise 5, question 4, you created a simple calculator that adds numbers from the command line.
   Make use of ``try``, ``except``  and ``finally`` statements to check the inputs and always produce
   a result even if some invalid values (e.g. ``str``) were passed to the script.  

2. In Exercise 6, question 4, you were asked to calculate the distance between these two points (vectors)
   ```python
   point_1 = [2.8, -4.7, 0.4]
   point_2 = [-8.1, 3.0, -10.6]
   ```
   - Transform that script into a function
   - Create functions that also calculate the dot ($\bullet$) and cross ($\times$) products of vectors.

   (Do not use ``numpy`` here)

3. ``Python`` provides a standard module (``timeit``)  for timing the execution of scripts and
    pieces of code. Please time the execution of these two equivalents blocks

    ````python
    N = 10**8
    # Time from here
    daten=[]
    for i in range(0,N) :
        daten.append(i**0.5)
    # to here

    # and from here
    daten = np.sqrt(np.arange(0,N))
    # to here
    ````
    - Which one is faster?
    - For what values of ``N`` the effect is really noticeable. Please try a few wildly different
    values to have an idea.

4. Write a ``Python`` script that asks for a integer and then prints every prime number up to that value.
   Check the execution time with the module ``timeit``. What can be said about the complexity of the algorithm you use (how many iterations does it need to process a dataset of n entires)? Look at different approaches to this problem and their complexity.

5. Now write the same script in ``C``. Please also check the execution time using the ``clock()`` function.

   [//]: # (As comment for now: BONUS: Here you can also try to create an array containing all the primes.
   Note that you will need the malloc and realloc functions in order to create an array without
   any empty entries)

# Informatics for Astronomers - WS2020

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Gerald Mösenlechner**

# Exercise sheet 5 - Python loops and C

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---


1. In Exercise 4, question 5, you were asked to calculate the distance between these two points (vectors)
   ```python
   point_1 = [2.8, -4.7, 0.4]
   point_2 = [-8.1, 3.0, -10.6]
   ```
   - Transform that script into a function
   - Create functions that also calculate the dot ($\bullet$) and cross ($\times$) products of vectors.

   (Do not use ``numpy`` here)

 2. ``Python`` provides a standard module (``timeit``)  for timing the execution of scripts and
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

 3. ``numpy`` is likely the most important library in ``python``. 

   - How do ``numpy`` arrays differ from ``python`` lists?
   - Show the creation of ``numpy`` arrays with different properties (e.g. converting from a ``list``, different step size and dimensions)
   - Apply some mathematical functions to arrays and comment the differences with using ``lists``
   - What is ``array`` broadcasting?

 4. Write a ``Python`` script that asks for a integer and then prints every prime number up to that value.
    Check the execution time with the module ``timeit``. What can be said about the complexity of the algorithm you use (how many iterations does it need to process a dataset of n entires)? Look at different approaches to this problem and their complexity.

 5. Now write the same script in ``C``. Please also check the execution time using the ``clock()`` function.



  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 10 - Title

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
> _Please strive for that in all exercises to come. From now on this will also be part of the assessment._

---

1. In the latest lecture, the python library ``numba`` was introduced. Please use this
   library in your `primes.py` code from Exercise 7.4 and discuss the speed-up improvements.
   What is this library doing under the hood? Under which conditions can be applied?
   How does it compare to the `C` code?

   Bonus: Using `matplotlib`, plot the speed-up improvements for different input values.

2. Write a simple `python` function that finds all files in a directory and determines their types.
   You may want to use the modules `glob` and `mimetypes` (or `python-magic`)

3. Using a ``python`` function find all environmental variables and write them to a text file.

4. Take some mathematical function of your choice and plot it using ``Matplotlib``. Note that the
   plot should at least contain a label for each axis and a title. Save the plot to a file.

5. Consider the data table ``rotcurve.txt`` provided with this exercise. It contains data
   for a rotation curve for a galaxy with columns _r_ for radius, _vel_ for velocity
   and error in _vel_. Please read the file and plot that information (including the errors)
   with ``matplotlib``.

   Bonus: Plot a function that best describe the data.  

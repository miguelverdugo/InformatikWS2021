# Informatics for Astronomers - WS2021

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Andreas Schanz**

# Exercise sheet 8 -

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Write a simple `python` function that finds all files in a directory and determines their types.
   You may want to use the modules like `glob` and `mimetypes` (or `python-magic`)

2. Using a ``python`` function find all environmental variables in your Linux/Unix environment and write them
    to a text file.

3. Take some mathematical function of your choice and plot it using ``Matplotlib``. Note that the
   plot should at least contain a label for each axis and a title. Save the plot to a file.

4. Consider the data table ``rotcurve.txt`` provided with this exercise. It contains data
   for a rotation curve for a galaxy with columns _r_ for radius, _vel_ for velocity
   and error in _vel_. Please read the file and plot that information (including the errors)
   with ``matplotlib``.

5. Take the data from the file (``dataset.txt``) and create a normalized histogram using
      ``matplotlib``. Play with the different plotting options like bin width,
      colors, line widths, etc. Calculate the mean and standard deviation using the
      ``numpy.mean`` and ``numpy.std`` functions.

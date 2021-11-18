# Informatics for Astronomers - WS2021

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Andreas Schanz**

# Exercise sheet 5 - Python and C

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Write a ``Python`` function that takes an integer and returns a list or array of all prime numbers
   up to that value. Write the function in a `.py` file and import it from the `ipython` shell.

2. The previous function takes an integer as parameter. Make sure that the function checks
   that it is the case and raise an exception otherwise clearly informing the user where the problem is.

    * Explain the concept "ask for forgiveness, not for permission" in `python`.   

3. Consider the following `numpy` array: ``x = np.arange(0, 100, 1)``.
   Find the list of attributes, properties and methods associated to that instance.
   Demonstrate the usage of few of them.

4. Take the ASCII file ``Photometry_example.txt`` from moodle. The file contains data of an $200\times 200$ pixels image of a star. Load the image using ``numpy.genfromtxt()``.

    - Use ``matplotlib.pyplot.imshow()`` to properly plot the image. Save it as `jpg` image.
    - Write a function that takes the array and find the position of the star returning 1) the peak flux 2) the
      `(x, y)` coordinates of the maximum.

5. Write the previous example as a `C` function. The function shall read the file using the ``fopen()`` and ``fscanf()`` function and write the content to an array (you can use either a 1D or 2D array). You can allocate the memory of the array directly (e.g. ``int array[200][200]`` or ``int array[200*200]``) or with a pointer and the `malloc` function. Note that you only need to print the result not the plotting.

6. Write a simple C function that takes three integer numbers and returns the largest number.

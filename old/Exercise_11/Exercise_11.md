  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 11 - Plotting, scipy and astropy

---

> _Your preparation of exercises should include two aspects:_
>
> _(1) Try to present exercises in a way that everyone can follow (even if that
> person didn’t do the exercise at all), so please explain all the (vital) parts of
> your solution in a slow and comprehensive way._
>
> _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Take the data from the file (``dataset.txt``) and create a normalized histogram using
   ``matplotlib``. Play with the different plotting options like bin width,
   colors, line widths, etc. Calculate the mean and standard deviation using the
   ``numpy.mean`` and ``numpy.std`` functions.

2. Take the dataset from the previous example and fit a gaussian distribution using ``curvefit``
   from ``scipy.optimize`` (Look at the documentation for examples).
   Plot the result over the the histogram of the dataset and check the
   resulting values for the mean and standard deviation calculated above. Also print the error of the fit.

3. The ``matplotlib`` library can also be used to create 2D images from arrays.
   This is very useful for plotting FITS (Flexible Image Transport System) files.
   FITS is a data format with widespread use in astronomy.

   Try and convert the provided image `SN2012aw.fits` into an array using the ``io.fits``
   package from ``astropy``.

   You can then plot the image using the ``imshow()`` function from ``matplotlib.pyplot``.
   Please experiment with the color and the normalization of the image.

   Note that FITS files contain more information than just the image. What is this information?

4. Similar as above: load the image `SN2012aw.fits` with ``astropy.io.fits`` and make a
   few statistics of the image using ``numpy`` statistical functions
   (e.g. mean, median, standard deviation, minimum and maximum value)

   - What is the size of the image?
   - Extract a small region around the SN (The size should be somewhere around 200x200 pixels) to a new array.
     Plot this array (don't forget a colorbar, tilte and labels for the axis) and save the array to a text-file.

5. Create a histogram of the image pixel values as in question 1 and try to fit a gaussian as
   in question 2. Discuss the results.

6. If you are using the ``anaconda`` environment you may have ``ginga`` installed
   (otherwise just type ``pip install ginga``). ``Ginga`` is a graphical application
   written in python to display FITS images. Please show some of its capabilities and discuss the differences with the above procedures.
   When do you think is better to use one or the other?

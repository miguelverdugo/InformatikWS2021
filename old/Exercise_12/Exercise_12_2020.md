#  Informatics for Astronomers - WS2020

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Marina Dütsch**

# Exercise sheet 12 -  Astronomical Data Analysis

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
>
---

1. Smooth the image `MACSJ0416_HAWKI.fits` from the previous exercise with ``scipy.ndimage.gaussian_filter``
   using a kernel size of your preference (please explore!). Subtract the smoothed image from the original one.  Save the smoothed _and_ subtracted images in ``fits`` format (using `astropy`) and display them with with e.g. ``ginga``
  (or ``ds9``).

2. In Exercise 9, question 5 you were asked to go to the SDSS SkyServer at
   [http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx](http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx)
   and search for objects around a position on the sky, setting the search radius to 30 arcmin. Download the data, setting the number to output rows to "max" (=0) so all objects are returned.

   Load the data with ``astropy.table.Table`` (`XML`, `CSV`, `VOTable` and `FITS` formats should be
   supported) and create the following plots.

     - an histogram of the object magnitudes (in 0.5 mag bins). Try setting the y-axis to linear and then switch to logarithmic.

     - a plot of the magnitude (any of them) vs their errors.

   What can we say about the survey characteristics from these plots?

3. Fit Gaussians profiles to the H$\alpha$ ($\lambda$=`6562.8 A`) and to the
   ``[OIII]`` ($\lambda$=`5007 A`) lines in the spectrum `SDSS_spec_galaxy.csv` and overplot the fits.
   You might need to subtract the spectral continuum to make the fitting to work.

    - What is the flux of these lines?

    - What is the `sigma` in `Angstrom` of these lines?

    - Transform these `sigma` to the velocity dispersion in `km/s`.

4. In the last exercise, you were able to find the pixel with maximum value in the
   image `MACSJ0416_HAWKI.fits`. Now, store the coordinates and pixel value in a list, array or table.
   Replace all pixels in a box of 20\times 20 pixels around that pixel with the median value
   of the image. Find the next pixel with the maximum value and repeat the process iteratively (let's say a 100 times).
   Save the results in an ``astropy.table.Table``.

   What are we doing here? Draw circles on the original image around these positions

5. The file ``Lightcurve.txt`` contains the lightcurve of an ACV-Type variable star.
   The first column contains the time in days while the second column shows the relative brightness change.
   Plot the lightcurve using ``matplotlib``.

   Now determine and plot the discrete Fourier Transform of the lightcurve using the functions ``fft`` and ``fftfreq``
   from ``scipy.fft``.

   Assume that the sample spacing of the time is constant. Then find the main frequency of the star by
   determining the frequency of the maximum magnitude in the transformed lightcurve.
   If you have issues you can look at the example for plotting the FFT of two sines in the ``1D discrete Fourier Transform`` section of [https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html#id10](https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html#id10) .  

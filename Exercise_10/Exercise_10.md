# Informatics for Astronomers - WS2021

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Andreas Schanz**

## Exercise sheet 10 - Astropy & GTK

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---
1. Smooth the image `MACSJ0416_HAWKI.fits`, ``scipy.ndimage.gaussian_filter``
   using a kernel size of your preference (please explore!). Subtract the smoothed image from the original one.  
   Save the smoothed _and_ subtracted images in ``fits`` format (using `astropy`) and display them with with
   e.g. ``ginga`` (or ``ds9``).

2.  Take the image `MACSJ0416_HAWKI.fits`. Now, store the coordinates and pixel value in a list, array or table.
    Replace all pixels in a box of $20\times 20$ pixels around that pixel with the median value
    of the image. Find the next pixel with the maximum value and repeat the process iteratively (let's say a 100 times).
    Save the results in an ``astropy.table.Table``.

    What are we doing here? Draw circles on the original image around these positions

3. In Exercise 9, question 5 you were asked to go to the SDSS SkyServer at
   [http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx](http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx)
   and search for objects around a position on the sky, setting the search radius to 30 arcmin. Download the data, setting the number to output rows to "max" (=0) so all objects are returned.

    Load the data with ``astropy.table.Table`` (`XML`, `CSV`, `VOTable` and `FITS` formats should be
    supported) and create the following plots.

      - an histogram of the object magnitudes (in 0.5 mag bins). Try setting the y-axis to linear and then switch to logarithmic.

      - a plot of the magnitude (any of them) vs their errors.

    What can we say about the survey characteristics from these plots?

4. The file `SDSS_spec_galaxy.csv` contains the spectrum of a star forming galaxy taken as
   part of the Sloan Digital Sky Survey. Load the spectrum with ``astropy`` and make a plot
   with ``matplotlib``.

     Knowing that the H$\alpha$ line at $\lambda=6562.8$ Angstrom (restframe) is the most intense
     line in this spectrum, please determine the redshift of this galaxy.

5. Fit Gaussians profiles to the H$\alpha$ ($\lambda$=`6562.8 A`) and to the
   ``[OIII]`` ($\lambda$=`5007 A`) lines in the spectrum `SDSS_spec_galaxy.csv` and overplot the fits.
   You might need to subtract the spectral continuum to make the fitting to work.

    - What is the flux of these lines?

    - What is the `sigma` in `Angstrom` of these lines?

    - Transform these `sigma` to the velocity dispersion in `km/s`.


6.  Design a simple calculator with `python GTK` (instructions for installing GTK are
    below). The calculator should have an entry field and buttons for the numbers
    0-9 and the operations add, subtract, multiply, and divide, as well as a result
    button. Use the `GtkEntry` and `GtkGrid` (or `GtkTable`) widgets for the entry field
    and buttons, respectively. The calculator does not need to work yet.


    GTK can be installed with conda using the following commands:

    ```
    conda install pycairo=1.18.2
    conda install -c conda-forge pygobject
    conda install -c conda-forge gtk3
    ```
    To avoid conflicts, you can first create a new conda environment:

    ```
    conda create --name=myenv python=3.8
    conda activate myenv
    ```

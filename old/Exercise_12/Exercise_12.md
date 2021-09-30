  Informatics for Astronomers - WS2019

**Miguel Verdugo, Gerald Mosenlechner, Roland Ottensamer, Leopold Haimberger**

# Exercise sheet 12 -  Image processing, astropy,

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

Solve this exercise in a ``Jupyter Notebook`` session.  Please include appropriate titles and
explanations for the different steps, as well as formulas, images and links if applicable.   


1. The fits file `MACSJ0416_HAWKI.fits` contains a near infrared (_Ks_-band) image of the center
   of the cluster of galaxies `MACS J0416.1-2403` at $z=0.4$. It was taken with the HAWK-I instrument at the VLT as part
   of the ESO contribution to the FrontierFields program (see
   [http://gbrammer.github.io/HAWKI-FF/](http://gbrammer.github.io/HAWKI-FF/)).

   Load the image with ``astropy`` and find the pixel with the maximum value.  Using ``matplotlib``
   draw a circle around it.  

2. Smooth the image with ``scipy.ndimage.gaussian_filter`` using a kernel size of your preference
   (please explore!). Subtract the smoothed image from the original one.

   Save the smoothed _and_ subtracted images in ``fits`` format and display them with with e.g. ``ginga``
   (or ``ds9``)

3. In Exercise 9, question 5 you were asked to go to the SDSS SkyServer
   [http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx](http://skyserver.sdss.org/dr15/en/tools/search/radial.aspx)
   and search for objects around a position on the sky.

   Now, please download the data. Do not forget to set the number to output rows to "max" (=0)
   so all objects are returned.

   Load the data with ``astropy.table.Table`` (XML, CSV, VOTable and FITS formats should be
   supported) and print the table on the notebook.

   Make a ``matplotlib`` plot of the positions of the objects (ra and dec columns) with points
   proportional to their magnitudes (any of them: u, g, r, i and z columns). Remember
   that brighter objects have smaller magnitudes.

4. Now set the search radius to 30 arcmin. Load the table and create the following plots.

    - an histogram of the object magnitudes (in 0.5 mag bins). Try setting the y-axis to
    linear and then switch to logarithmic.

    - a plot of the magnitude vs their errors.    

   What can we say about the survey characteristics from these plots?

5. The file `SDSS_spec_galaxy.csv` contains the spectrum of a star forming galaxy taken as
   part of the Sloan Digital Sky Survey. Load the spectrum with ``astropy`` and make a plot
   with ``matplotlib``.

   Knowing that the H$\alpha$ line at $\lambda=6562.8$ Angstrom (restframe) is the most intense
   line in this spectrum, please determine the redshift of this galaxy.


---

**Extra question**: It won't be evaluated but your are welcome to try.

Do Question 1 again with the following variation:

Find the pixel with maximum value. Store the coordinates and pixel value in e.g. a list
Now replace all pixels in a box of 20\times 20 pixels around that pixel with the median value
of the image. Find the next pixel with the maximum value and repeat the process. Do the same
iteratively (let's say a 100 times). Save the results in an ``astropy.table.Table``.
What are we doing here? Draw circles on the original image around these positions

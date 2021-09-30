# Informatics for Astronomers - WS2020

**Roland Ottensamer, Marina Dütsch, Miguel Verdugo, Gerald Mösenlechner**

# Exercise sheet 11 - Astronomical Data Analysis

---

>  _The following will be also part of the assessment:_
>
>  _(1) Try to present exercises in a way that everyone can understand (even those who didn’t do the exercises), so please explain the vital parts of
> your solution in a clear way._
>
>  _(2) Try to also include some background information where applicable, and/or
> explain the possible context/motivation for the given exercise._

---

1. Describe the `astropy` project (origin, purpose, etc) as well as its most important components.

2. The `FITS` file `MACSJ0416_HAWKI.fits` contains a near infrared (_Ks_-band) image of the center
   of the cluster of galaxies `MACS J0416.1-2403` at $z=0.4$. It was taken with the HAWK-I instrument at
   the VLT as part of the ESO contribution to the [FrontierFields program](http://gbrammer.github.io/HAWKI-FF/)).  

   - Using the `astropy` library, load that file in python and show us the most important parameters,
     like image size and headers.

   -  Display the previous image with `matplotlib` in a way that the objects can be distinguished by
     eye (by adjusting the contrast). Find the pixel with the maximum value and draw a circle around it.
     Finally save the image as a PDF file.

3. Do some statistics (mean, median and standard deviation) of the previous image using `numpy` statistical functions.
   Create an histogram of the pixel values and plot it with `matplotlib`.

   Now, using ``curvefit`` from ``scipy.optimize`` fit a Gaussian to the histogram values and determine
   the center (mean) and the sigma (standard deviation) from the fit. Discuss the differences with values
   derived by `numpy`.

4. Consider the data table `rotcurve.txt` provided with this exercise. It contains data for a rotation curve
   for a galaxy with columns `r` for radius, `vel` for velocity and the error in `vel`. Please read the file
   (with `astropy`) and plot that information (including the errors) with `matplotlib`.

   What is the maximum rotation velocity of this galaxy? Try to determine it by fitting the following
   function to the data (but other ideas are also welcome)

   $V(r) = \frac{2}{\pi} V_{max} \arctan(r/r_d)$,

   where $r_d$ is the disk scale length, $\sim 5$ in this case, but can also be left as a free parameter.

5. The file `SDSS_spec_galaxy.csv` contains the spectrum of a star forming galaxy observed as
   part of the Sloan Digital Sky Survey. Load the spectra with ``astropy`` and make a plot with ``matplotlib``.

   Knowing that the H$\alpha$ line at $\lambda=6562.8$ `Angstrom` (restframe) is the most intense line in this spectrum,
   determine the redshift of this galaxy.

   Overplot now the redshift corrected spectrum.

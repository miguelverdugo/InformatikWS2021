from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdu = fits.open('./SN2012aw.fits')[0]
for i in hdu.header[:]:
    print(i, hdu.header[str(i)])

print(hdu.header["DATE"])

import numpy as np
from astropy.io import fits

hdu=fits.open('dapall-v2_4_3-2.2.1.fits')
tab=hdu[1].data


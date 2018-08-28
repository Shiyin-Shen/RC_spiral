import numpy as np

from astropy.io import fits


hdu=fits.open('dapall-v2_4_3-2.2.1.fits')

dapall=hdu[1].data

MANGAID=dapall['MANGAID']
Ra=dapall['OBJRA']
Dec=dapall['OBJDEC']
Ser_N=dapall['NSA_SERSIC_N']
btoa=dapall['NSA_SERSIC_BA']
Phi=dapall['NSA_SERSIC_PHI']
redshift=dapall['NSA_Z']
IFUDESIGN=dapall['IFUDESIGN']
R50=dapall[]

#%%
sel=np.where((Ser_N < 2) & (btoa > 0.3) & (btoa < 0.7) & (IFUDESIGN > 12700)) 


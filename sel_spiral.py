import numpy as np

from astropy.io import fits


hdu=fits.open('dapall-v2_4_3-2.2.1.fits')

dapall=hdu[1].data

MANGAID=dapall['MANGAID']
Plate=dapall['PLATE']
Ra=dapall['OBJRA']
Dec=dapall['OBJDEC']
Ser_N=dapall['NSA_SERSIC_N']
btoa=dapall['NSA_SERSIC_BA']
Phi=dapall['NSA_SERSIC_PHI']
redshift=dapall['NSA_Z']
IFUDESIGN=dapall['IFUDESIGN']
R50=dapall['NSA_SERSIC_TH50']
type=dapall['DAPTYPE']

#select non-face/edge on spirals with 127 fibers
sel=np.where((Ser_N < 2) & (btoa > 0.3) & (btoa < 0.7) & (IFUDESIGN > 12700) & \
             (type == 'HYB10-GAU-MILESHC') )

ID=MANGAID[sel]

dapdir='/DATA_MANGA/MANGA/DAP/MPL-7/HYB10-GAU-MILESHC/'
#for i,MID in enumerate(ID):
      
Isel=sel[0][i]
mapfilename='manga-'+str(Plate[Isel])+'-'+str(IFUDESIGN[Isel])+'-MAPS-HYB10-GAU-MILESHC.fits.gz'
cubefilename='manga-'+str(Plate[Isel])+'-'+str(IFUDESIGN[Isel])+'-LOGCUBE-HYB10-GAU-MILESHC.fits.gz'
mapfile=dapdir+str(Plate[Isel])+'/'+str(IFUDESIGN[Isel])+'/'+mapfilename
cubefile=dapdir+str(Plate[Isel])+'/'+str(IFUDESIGN[Isel])+'/'+cubefilename
 
maps=fits.open(mapfile)
cube=fits.open(cubefile)


StellarV=maps[15].data
StellarV_Ivar=maps[16].data
sigma=maps[17].data
sigma_Ivar=maps[18].data
sigma_corr=maps[19].data

EmV=maps[36].data
EmVerr=maps[37].data



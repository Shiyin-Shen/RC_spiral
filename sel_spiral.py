import numpy as np
import os

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
UID=list(set(MANGAID[sel]))

#dapdir='/DATA_MANGA/MANGA/DAP/MPL-7/HYB10-GAU-MILESHC/'
dapdir='/DATA_MANGA/newton/mpl7/dap/HYB10-GAU-MILESHC/'

outdir='veldata/'
j=0

outpar=open('spiral_RC.par','w')
outpar.write('#MaNGAID,ellp,Phi\n')
for i,MID in enumerate(UID):
      
      sel=np.where(UID[i] == MANGAID)
      Isel=sel[0][0]
         
      mapfilename='manga-'+str(Plate[Isel])+'-'+str(IFUDESIGN[Isel])+'-MAPS-HYB10-GAU-MILESHC.fits.gz'
      #cubefilename='manga-'+str(Plate[Isel])+'-'+str(IFUDESIGN[Isel])+'-LOGCUBE-HYB10-GAU-MILESHC.fits.gz'
      mapfile=dapdir+str(Plate[Isel])+'/'+str(IFUDESIGN[Isel])+'/'+mapfilename
      #cubefile=dapdir+str(Plate[Isel])+'/'+str(IFUDESIGN[Isel])+'/'+cubefilename
      if not os.path.isfile(mapfile):
            continue
      
      outpar.write('%8s,%4.2f,%6.2f\n' %(UID[i],1-btoa[Isel],Phi[Isel]))
      
      maps=fits.open(mapfile)
      #cube=fits.open(cubefile)

      StellarV=maps[15].data
      StellarV_Ivar=maps[16].data
      #sigma=maps[17].data
      #sigma_Ivar=maps[18].data
      #sigma_corr=maps[19].data
      EmV=maps[36].data
      EmV_Ivar=maps[37].data[0,:,:]

      hdu1 = fits.PrimaryHDU(EmV[0,:,:])
      sel=np.where(EmV_Ivar ==0)
      EmV_Ivar[sel]=1.e-6
      EmV_err=1/np.sqrt(EmV_Ivar)
      hdu2 = fits.PrimaryHDU(EmV_err)
      hdu3 = fits.PrimaryHDU(StellarV)
      sel=np.where(StellarV_Ivar == 0)
      StellarV_Ivar[sel]=1.e-6
      StellarV_err=1./np.sqrt(StellarV_Ivar)

      #sel=where()
      
      hdu4 = fits.PrimaryHDU(StellarV_err)

      #hdu1.writeto(outdir+'EmV'+MANGAID[Isel]+'.fits',overwrite=True)
      #hdu2.writeto(outdir+'EmVerr'+MANGAID[Isel]+'.fits',overwrite=True)
      #hdu3.writeto(outdir+'StV'+MANGAID[Isel]+'.fits',overwrite=True)
      #hdu4.writeto(outdir+'StVerr'+MANGAID[Isel]+'.fits',overwrite=True)
      
      j=j+1
      
print(j,'galaxies velocity maps read')
outpar.close()


















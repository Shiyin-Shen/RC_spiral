#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:52:33 2018

@author: shen
"""

import numpy as np
import glob
import os
from astropy.io import fits
import pandas as pd


outdir='veldata/'
veldata=glob.glob(os.path.join(outdir,'EmV1*fits'))
par=pd.read_csv('spiral_RC.par')

#velerrdata=glob.glob(os.path.join(outdir,'EmVerr*fits'))

Ngal=len(veldata)


for i,datafile in enumerate(veldata):
      
      hdu=fits.open(datafile)
      ima=hdu[0].data
      xim,yim=ima.shape
      
      dataname=datafile.split('/')[-1]
      MaNGAID=dataname[3:10]
      
      Phi=par['Phi'][i]
      ellp=par['ellp'][i]
      ID=par['MaNGAID][i]
      
   
      errfile=outdir+'EmVerr'+MaNGAID+'.fits'
  
      
      #get the position angle, b/a paramters
      
      
      #output DiskFit parameter file
      filename=outdir+'velpar'+MaNGAID+'.ini'
         
      outpar=open(filename,'w')
      outpar.write("Disk rotation curve fit, axsymetric\n")
      outpar.write("vels\n")
      outpar.write("T    F\n")
      outpar.write('\''+datafile+'\'\n')
      outpar.write('\''+errfile+'\'\n')
      print('1   1  ',xim,yim,file=outpar)
      regrad=np.min(xim,yim)*np.sqrt(3)*0.5
      print(regrad,)
      


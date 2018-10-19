#!/usr/bin/python

# This script is to change unit of omega(from Hatree to cm^-1) and sum contributions of each 4 atoms.
# read output file of ABINIT anaddb utility, then plot phonon density of states.

import numpy as np
import math
import scipy



f1=open('pb_5.out_PHDOS_by_atom','r')
f2=open('phonon_dos.dat','w')

ff1=f1.readlines()
f1.close()

# to find line number
f1=open('pb_5.out_PHDOS_by_atom','r')
line_num=-1
for line in f1:
 line_num+=1
f1.close()

for iline in range(line_num):
  if (iline>=8) :
    aa=ff1[iline].split()
    omega=float(aa[0])*219474.627888
    for i in range(17):
      if '-1' in aa[i+1]:
        aa[i+1]='0'
      if '-2' in aa[i+1]:
        aa[i+1]='0'
 
    tot=float(aa[1])
    cd=float(aa[2])+float(aa[3])+float(aa[4])+float(aa[5])
    iv=float(aa[6])+float(aa[7])+float(aa[8])+float(aa[9])
    n1=float(aa[10])+float(aa[11])+float(aa[12])+float(aa[13])
    n2=float(aa[14])+float(aa[15])+float(aa[16])+float(aa[17])
    tot=tot/10000
    cd=cd/10000
    iv=iv/10000
    n1=n1/10000
    n2=n2/10000
    tt=str(omega)+' '+str(tot)+' '+str(cd)+' '+str(iv)+' '+str(n1)+' '+str(n2)
    f2.write(tt+' \n')

f2.close()

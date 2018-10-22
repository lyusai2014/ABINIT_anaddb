#!/usr/bin/python

# This python script is to calculate unclamped EO tensor in II-IV-N2 compounds.
# p_ijuv=d epsilon/ d eta

f1=open('dielectric.dat','r')
ff1=f1.readlines()
f1.close()
# define empty lists
epsilon_00=[] # no strain perturbation

epsilon_11=[] # xx 
epsilon_22=[]
epsilon_33=[]
epsilon_12=[]
epsilon_13=[]
epsilon_23=[]

for i in range(28):
  if (1<=i<=3) :
    for j in range(3):
     epsilon_00.append(ff1[i].split()[j])

  if (5<=i<=7) :
    for j in range(3):
     epsilon_11.append(ff1[i].split()[j])
  if (9<=i<=11) :
    for j in range(3):
     epsilon_22.append(ff1[i].split()[j])
  if (13<=i<=15) :
    for j in range(3):
     epsilon_33.append(ff1[i].split()[j])
  if (17<=i<=19) :
    for j in range(3):
     epsilon_12.append(ff1[i].split()[j])
  if (21<=i<=23) :
    for j in range(3):
     epsilon_13.append(ff1[i].split()[j])
  if (25<=i<=27) :
    for j in range(3):
     epsilon_23.append(ff1[i].split()[j])


#======================




eta_11=0.001
eta_22=0.001
eta_33=0.001
eta_12=0.001/2 # since the summing is over 6 terms instead of 9 terms.
eta_13=0.001/2
eta_23=0.001/2 

# 
p_11=[] # p_ij11
p_22=[]
p_33=[]
p_12=[]
p_13=[]
p_23=[]


for i in range(9):
  aa=(float(epsilon_11[i])-float(epsilon_00[i]))/eta_11
  p_11.append(aa)
for i in range(9):
  aa=(float(epsilon_22[i])-float(epsilon_00[i]))/eta_22
  p_22.append(aa)
for i in range(9):
  aa=(float(epsilon_33[i])-float(epsilon_00[i]))/eta_33
  p_33.append(aa)
for i in range(9):
  aa=(float(epsilon_12[i])-float(epsilon_00[i]))/eta_12
  p_12.append(aa)
for i in range(9):
  aa=(float(epsilon_13[i])-float(epsilon_00[i]))/eta_13
  p_13.append(aa)
for i in range(9):
  aa=(float(epsilon_23[i])-float(epsilon_00[i]))/eta_23
  p_23.append(aa)




#########
f2=open('piezo.dat','r')
ff2=f2.readlines()
f2.close()
dtensor=[]
for k in range(6) :
 cc=ff2[k].split()
 dtensor.append(cc) 

print dtensor


# rcc, the EO tensor correction, difference between clamped and unclamped
# rcc_ijy=sum_uv p_ijuv*d_yuv
# p_ijuv*d_yuv,  sum over u and v
# Voigt notation, 1=xx, 4=yz, 5=zx, 6=xy
# p_uv[ij], dtensor[uv][y]
rcc_15= float(p_11[4])*float(dtensor[0][0])+float(p_22[4])*float(dtensor[1][0]) \
       +float(p_33[4])*float(dtensor[2][0])+float(p_23[4])*float(dtensor[3][0]) \
       +float(p_13[4])*float(dtensor[4][0])+float(p_12[4])*float(dtensor[5][0])


print 'rcc_15',rcc_15


# rcc_15, so 5-1=4, p_11[4], p_22[4] an so on, 1-1=0, dtensor[][0]  

rcc_24= float(p_11[3])*float(dtensor[0][1])+float(p_22[3])*float(dtensor[1][1]) \
       +float(p_33[3])*float(dtensor[2][1])+float(p_23[3])*float(dtensor[3][1]) \
       +float(p_13[3])*float(dtensor[4][1])+float(p_12[3])*float(dtensor[5][1])


print 'rcc_24',rcc_24


rcc_31= float(p_11[0])*float(dtensor[0][2])+float(p_22[0])*float(dtensor[1][2]) \
       +float(p_33[0])*float(dtensor[2][2])+float(p_23[0])*float(dtensor[3][2]) \
       +float(p_13[0])*float(dtensor[4][2])+float(p_12[0])*float(dtensor[5][2])


print 'rcc_31',rcc_31

rcc_32= float(p_11[1])*float(dtensor[0][2])+float(p_22[1])*float(dtensor[1][2]) \
       +float(p_33[1])*float(dtensor[2][2])+float(p_23[1])*float(dtensor[3][2]) \
       +float(p_13[1])*float(dtensor[4][2])+float(p_12[1])*float(dtensor[5][2])


print 'rcc_32',rcc_32

rcc_33= float(p_11[2])*float(dtensor[0][2])+float(p_22[2])*float(dtensor[1][2]) \
       +float(p_33[2])*float(dtensor[2][2])+float(p_23[2])*float(dtensor[3][2]) \
       +float(p_13[2])*float(dtensor[4][2])+float(p_12[2])*float(dtensor[5][2])


print 'rcc_33',rcc_33


#========================================
f3=open('eotensor.dat','r')
ff3=f3.readlines()
f3.close()
reo=[]
for k in range(6) :
  dd=ff3[k].split()
  reo.append(dd)

print 'unclamped EO tensor'
r15=rcc_15+float(reo[4][0]) # rcc_ij+reo_j-1,i-1
r24=rcc_24+float(reo[3][1])
r31=rcc_31+float(reo[0][2])
r32=rcc_32+float(reo[1][2])
r33=rcc_33+float(reo[2][2])

print 'r15', r15
print 'r24', r24
print 'r31', r31
print 'r32', r32
print 'r33', r33


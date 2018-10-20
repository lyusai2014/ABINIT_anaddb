#!/usr/bin/python

# This script is to collect the data of Phonons from ABINIT output
# and then sort out the phonon modes by their corresponding irreducible representations
# for II-IV-N_2 semiconductors.



import numpy as np
import math
import scipy



f=open('tnlo_5.out','r')
g=open('phonon_data.txt','w')
range_number=11


i_index=0
lines=f.readlines() 
# readlines() method splilt the file into an array of words. 
# array=lines[index].splilt()
f.close() 
# AFTER READING, CLOSE THE FILE. IF NOT, THE NEXT READING WILL START FORM WHERE LAST READING END.


#First part, record the line index containing 'Phonon frequencies'
f=open('tnlo_5.out','r')
phonon_index_list=[] # specify an empty list
for line in f :
  if 'Phonon frequencies' in line  :
   phonon_index_list.append(i_index) #list.append() method
  i_index=i_index+1

print phonon_index_list
f.close()

# Second part, write out the lines with phonon index.

for j_index in range(4) :
  for k_index in range(range_number) : # write the lines containig "Phonon frequencies" and the following 10 lines.
    aa=lines[phonon_index_list[j_index]+k_index]
    g.write(aa)  



g.close()

del lines
del aa  # CLEAR THE VARIABLE

# Third part, to store the frequencies into 4 lists. each list contains 48 elements.  
p=open('phonon_data.txt','r')
q=open('list_phonon.txt','w')
list_1=[]
list_2=[]
list_3=[]
list_4=[]

lines2=p.readlines()

for line_index in range(50) :
  if (line_index >=1 and line_index <=9) :
    aa=lines2[line_index].split()
    for m_index in range(6):
       list_1.append(aa[m_index])
    list_1.remove('-') # list.remove() method

  if (line_index ==10) :
    aa=lines2[line_index].split()
    for m_index in range(4):
       list_1.append(aa[m_index])
    list_1.remove('-') # list.remove() method
  
  if (line_index >=12 and line_index <=20) :
    aa=lines2[line_index].split()
    for m_index in range(6):
       list_2.append(aa[m_index])
    list_2.remove('-') # list.remove() method

  if (line_index ==21) :
    aa=lines2[line_index].split()
    for m_index in range(4):
       list_2.append(aa[m_index])
    list_2.remove('-') # list.remove() method
  if (line_index >=23 and line_index <=31) :
    aa=lines2[line_index].split()
    for m_index in range(6):
       list_3.append(aa[m_index])
    list_3.remove('-') # list.remove() method

  if (line_index ==32) :
    aa=lines2[line_index].split()
    for m_index in range(4):
       list_3.append(aa[m_index])
    list_3.remove('-') # list.remove() method

  if (line_index >=34 and line_index <=42) :
    aa=lines2[line_index].split()
    for m_index in range(6):
       list_4.append(aa[m_index])
    list_4.remove('-') # list.remove() method

  if (line_index ==43) :
    aa=lines2[line_index].split()
    for m_index in range(4):
       list_4.append(aa[m_index])
    list_4.remove('-') # list.remove() method

  line_index=line_index+1

 

print list_1
print list_2
print list_3
print list_4


p.close()
q.close()


# Fourth part, print out every mode under specified symmetry.

v=open('phonon_data.txt','r')
u=open('phonon_table.dat','w') # WRITE THE OUTPUT IN .DAT FILE


for h_index in range(48) :
       if list_1[h_index] in list_2 :
         if list_1[h_index] in list_3 :
            if list_1[h_index] in list_4 :
               cc=round(float(list_1[h_index]),1)
               if cc != -0.0:
                 u.write('a2 mode '+str(cc)+'\n')                   
for h_index in range(48) :  
   if list_2.count(list_1[h_index])==0 :
               cc=round(float(list_1[h_index]),1)
               if cc != -0.0:
                 u.write('b1_T mode '+str(cc)+'\n')


for h_index in range(48) :
   if list_1.count(list_2[h_index])==0 :
               cc=round(float(list_2[h_index]),1)
               if cc != -0.0:
                  u.write('b1_L mode '+str(cc)+'\n')


for h_index in range(48) :
   if list_3.count(list_1[h_index])==0 :
               cc=round(float(list_1[h_index]),1)
               if cc != -0.0: 
                  u.write('b2_T mode '+str(cc)+'\n')


for h_index in range(48) :
   if list_1.count(list_3[h_index])==0 :
               cc=round(float(list_3[h_index]),1)
               if cc != -0.0:
                 u.write('b2_L mode '+str(cc)+'\n')





for h_index in range(48) :

   if list_4.count(list_1[h_index])==0 :
               cc=round(float(list_1[h_index]),1)
               if cc != -0.0: 
                 u.write('a1_T mode '+str(cc)+'\n')
for h_index in range(48) :

   if list_1.count(list_4[h_index])==0 :
               cc=round(float(list_4[h_index]),1)
               if cc != -0.0:
                     u.write('a1_L mode '+str(cc)+'\n')                               

u.close()
v.close()

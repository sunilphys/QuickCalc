# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:30:16 2020

@author: sunil
"""
import os.path
import time
import numpy as np
import matplotlib.pyplot as plt
Path = "D:\OneDrive\IISERTirupati\Astrobiolab\My Research\Simulations\iFunnelQ\SimData\\"
Filename ="if-f5-a27-cl1-0.dat"
File = Path + Filename

with open(File) as fl:
    head = [next(fl) for x in range(14)]
    for i, line in enumerate(head):
        if i == 1:
            p = float(line[line.index(": ") + 1:line.rindex(" ")])
        if i == 2:
            Vrf = float(line[line.index(": ") + 1:line.rindex(" ")])
        if i == 3:
            Frf = float(line[line.index(": ") + 1:line.rindex(" ")])
        if i == 4:
            Vcap = float(line[line.index(": ") + 1:line.rindex(" ")])
        if i == 5:
            Vrf1 = float(line[line.index(": ") + 1:line.rindex(" ")])
        if i == 6:
            Vrf24 = float(line[line.index(": ") + 1:line.rindex(" ")])
        if i == 7:
            Vcl = float(line[line.index(": ") + 1:line.rindex(" ")])
        if i == 11:
            if 'Separately' in line:
                fly = 'Ind'
            else:
                fly = 'Grp'
            tq = int(line[line.index("(") + 1:line.rindex(")")])
        if i == 12:
            ni = int(line[line.index("= ") + 1:line.rindex("\"")])

datatab = np.genfromtxt(File,delimiter='\t',skip_header=19,skip_footer=1,
                        usecols=(0,1,2,3,5,6,7,8,12))


print("The working file is %s"%Filename)
print("It was created on: %s and last modified on: %s " 
      %(time.ctime(os.path.getctime(File)),time.ctime(os.path.getmtime(File))))

xposxy = []
yposxy = []
yposyz = []
zposyz = []
ike = []
oke = []
ionin = 0
ionout = 0
nbin2d = 20
amu = 1.660539e-27  # Atomic mass unit
kB = 1.3806488e-23		# Boltzmann constant in m²kgs⁻²K⁻¹
mi = 215    # Mass of the ion
# for line in datatab:
#     if line[3]>=172:
#         ypos.append(line[4])
#         zpos.append(line[5])

for line in datatab:
    if line[1] == 1:
        ionin+=1
        ike.append(line[7])
    if line[1] == 1024:
    #if line[1] !=1024 and line[3] >= 145.0:
        ionout+=1
        oke.append(line[7]*1000)
        yposyz.append(line[5])
        zposyz.append(line[6])
print("Number of ions generated: %d" %(ionin))
print("Transmission efficiency = %3.0f %%." % (ionout*100/ionin))

plt.hist(ike,bins=100)
plt.xlabel("Initial Kinetic Energy (eV)")
plt.ylabel("Counts")
plt.show()

plt.hist(oke,bins=100)
plt.xlabel("Final Kinetic Energy (meV)")
plt.ylabel("Counts")
plt.xlim(0,4000)
plt.show()

fig, ax = plt.subplots(1,1)

ax.set(xlabel='y (mm)')
ax.set(ylabel='z (mm)')
ax.hist2d(yposyz,zposyz,bins=nbin2d)
#ax.axis("scaled")
ax.set_xlim(min(yposyz)-0.01,max(yposyz)+0.01)
ax.set_ylim(min(zposyz)-0.01,max(zposyz)+0.01)

#print("Efficiency = %3.2f" %float(ionout*100/ionin))
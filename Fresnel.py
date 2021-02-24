# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:32:15 2018

@author: Sunil
"""

import numpy as np
import matplotlib.pyplot as plt
n1=1.00
n2=1.50
n=n2/n1
AngB=180/np.pi*np.arctan(n)
if n<=1:
  AngC=180/np.pi*np.arcsin(n)
deg2rad=np.pi/180
AngXrad=deg2rad*0.0
x=np.linspace(0,90,360,endpoint=True)
xrad=x*deg2rad
Ifrac=np.sqrt(n**2-np.sin(xrad)**2)/np.cos(xrad)
IfracX=np.sqrt(n**2-np.sin(AngXrad)**2)/np.cos(AngXrad)
re=(np.cos(xrad)-np.sqrt(n**2-(np.sin(xrad)**2)))/(np.cos(xrad)+np.sqrt(n**2-np.sin(xrad)**2))
reX=(np.cos(AngXrad)-np.sqrt(n**2-(np.sin(AngXrad)**2)))/(np.cos(AngXrad)+np.sqrt(n**2-np.sin(AngXrad)**2))
rm=(np.sqrt(n**2-(np.sin(xrad)**2))-n**2*np.cos(xrad))/(np.sqrt(n**2-np.sin(xrad)**2)+n**2*np.cos(xrad))
rmX=(np.sqrt(n**2-(np.sin(AngXrad)**2))-n**2*np.cos(AngXrad))/(np.sqrt(n**2-np.sin(AngXrad)**2)+n**2*np.cos(AngXrad))
te=(2*np.cos(xrad))/(np.cos(xrad)+np.sqrt(n**2-np.sin(xrad)**2))
teX=(2*np.cos(AngXrad))/(np.cos(AngXrad)+np.sqrt(n**2-np.sin(AngXrad)**2))
tm=(2*n*np.cos(xrad))/(np.sqrt(n**2-np.sin(xrad)**2)+n**2*np.cos(xrad))
tmX=(2*n*np.cos(AngXrad))/(np.sqrt(n**2-np.sin(AngXrad)**2)+n**2*np.cos(AngXrad))
Re=re*re
ReX=reX*reX
Rm=rm*rm
RmX=rmX*rmX
Te=Ifrac*te*te
TeX=IfracX*teX*teX
Tm=Ifrac*tm*tm
TmX=IfracX*tmX*tmX
f1=plt.figure()
#plt.plot(x,re,label="Refl. Coeff. TE")
#plt.plot(x,te,label="Trans. Coeff. TE")
plt.plot(x,rm,label="Refl. Coeff. TM")
plt.plot(x,tm,label="Trans. Coeff. TM")
plt.title("Reflection and transmission coefficients for n=%3.2f/%3.2f" %(n2,n1))
plt.xlabel("Angle of incidence in degrees")
plt.ylabel("Coefficients of reflection/transmission")
plt.xlim(0,90)
#plt.ylim(-1,1)
plt.axvline(AngB,color='grey', linestyle='--',linewidth=1)
if n<=1:
  plt.axvline(AngC,color='grey', linestyle='--',linewidth=1)
plt.axhline(0,color='grey', linestyle='--',linewidth=1)
plt.axhline(1,color='grey', linestyle='--',linewidth=1)
#plt.axvline(41.81,color='g', linestyle='--')
#plt.axvline(33.69,color='b', linestyle='--')
plt.legend()
plt.savefig("RTCn0.7.pdf")
plt.show()
f2=plt.figure()
plt.plot(x,Re,label="Reflectance: TE")
plt.plot(x,Te,label="Transmittance: TE")
#plt.plot(x,Rm,label="Reflectance: TM")
#plt.plot(x,Tm,label="Transmittance: TM")
#plt.plot(x,Re+Te,label="Total: RTE+TTE")
#plt.plot(x,Rm+Tm,label="Total: RTM+TTM")
plt.title("Reflectance and transmittance for n=%3.2f/%3.2f" %(n2,n1))
plt.xlabel("Angle of incidence in degrees")
plt.ylabel("Reflectance/Transmittance")
plt.xlim(0,90)
#plt.ylim(0,1)
plt.axvline(AngB,color='grey', linestyle='--',linewidth=1)
if n<=1:
  plt.axvline(AngC,color='grey', linestyle='--',linewidth=1)
plt.axhline(0,color='grey', linestyle='--',linewidth=1)
plt.axhline(1,color='grey', linestyle='--',linewidth=1)
#plt.axvline(41.81,color='g', linestyle='--')
#plt.axvline(33.69,color='b', linestyle='--')
plt.legend()
plt.savefig("RTn0.7.pdf")
plt.show()
print("The Brewster angle is: %3.2f" %(AngB))
if n<=1:
  print("The critical angle is: %3.2f" %(AngC))
print("Reflectance for external TE reflection = %3.3f" % ReX)
print("Reflectance for external TM reflection = %3.3f" % RmX)
print("Transmittance for external TE reflection = %3.3f" % TeX)
print("Transmittance for external TM reflection = %3.3f" % TmX)

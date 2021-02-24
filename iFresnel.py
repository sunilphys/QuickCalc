# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:32:15 2018

@author: Sunil
"""

import numpy as np
import cmath
import matplotlib.pyplot as plt
n1=1.50
n2=1.00
n=n2/n1
deg2rad=np.pi/180
AngB=180/np.pi*np.arctan(n)
if n<=1:
  AngC=180/np.pi*np.arcsin(n)
AngX=deg2rad*0
x=np.linspace(0,90,360,endpoint=True)
xrad=x*deg2rad
#xradar=np.asarray(xrad)
Ifrac=[(cmath.sqrt(n**2-np.sin(i)**2)/np.cos(i)).real for i in xrad]
IfracX=(cmath.sqrt(n**2-np.sin(AngX)**2)/np.cos(AngX)).real
Ifrac=np.asarray(Ifrac)
re=[abs((cmath.cos(i)-cmath.sqrt(n**2-(cmath.sin(i)**2)))/(cmath.cos(i)+cmath.sqrt(n**2-cmath.sin(i)**2))) for i in xrad]
reX=abs((cmath.cos(AngX)-cmath.sqrt(n**2-(cmath.sin(AngX)**2)))/(cmath.cos(AngX)+cmath.sqrt(n**2-cmath.sin(AngX)**2)))
re=np.asarray(re)
rm=[abs((cmath.sqrt(n**2-(cmath.sin(i)**2))-n**2*cmath.cos(i))/(cmath.sqrt(n**2-cmath.sin(i)**2)+n**2*cmath.cos(i))) for i in xrad]
rmX=abs((cmath.sqrt(n**2-(cmath.sin(AngX)**2))-n**2*cmath.cos(AngX))/(cmath.sqrt(n**2-cmath.sin(AngX)**2)+n**2*cmath.cos(AngX)))
rm=np.asarray(rm)
te=[abs((2*cmath.cos(i))/(cmath.cos(i)+cmath.sqrt(n**2-cmath.sin(i)**2))) for i in xrad]
teX=abs((2*cmath.cos(AngX))/(cmath.cos(AngX)+cmath.sqrt(n**2-cmath.sin(AngX)**2)))
te=np.asarray(te)
tm=[abs((2*n*cmath.cos(i))/(cmath.sqrt(n**2-cmath.sin(i)**2)+n**2*cmath.cos(i))) for i in xrad]
tmX=abs((2*n*cmath.cos(AngX))/(cmath.sqrt(n**2-cmath.sin(AngX)**2)+n**2*cmath.cos(AngX)))
tm=np.asarray(tm)
Re=re*re
ReX=reX*reX
Rm=rm*rm
RmX=rmX*rmX
Te=Ifrac*te*te
TeX=IfracX*teX*teX
Tm=Ifrac*tm*tm
TmX=IfracX*tmX*tmX
f1=plt.figure()
plt.plot(x,re,label="Refl. Coeff. TE")
plt.plot(x,te,label="Trans. Coeff. TE")
plt.plot(x,rm,label="Refl. Coeff. TM",linestyle='dashed')
plt.plot(x,tm,label="Trans. Coeff. TM",linestyle='dashed')
plt.title("Reflection and transmission coefficients for n=%3.2f/%3.2f" %(n2,n1))
plt.xlabel("Angle of incidence in degrees")
plt.ylabel("Coefficients of reflection/transmission")
plt.xlim(0,90)
#plt.ylim(0,1.0)
#plt.axvline(56.31,color='grey', linestyle='--')
plt.axhline(0,color='grey', linestyle='--',linewidth=1)
plt.axhline(1,color='grey', linestyle='--',linewidth=1)
plt.axvline(AngB,color='grey', linestyle='--',linewidth=1)
if n<=1:
  plt.axvline(AngC,color='grey', linestyle='--',linewidth=1)
plt.legend()
plt.savefig("RTiCn1.5.pdf")
plt.show()
f2=plt.figure()
plt.plot(x,Re,label="Reflectance: TE")
plt.plot(x,Te,label="Transmittance: TE")
plt.plot(x,Rm,label="Reflectance: TM",linestyle='dashed')
plt.plot(x,Tm,label="Transmittance: TM",linestyle='dashed')
#plt.plot(x,Re+Te,label="Total: RTE+TTE")
#plt.plot(x,Rm+Tm,label="Total: RTM+TTM")
plt.title("Reflectance and transmittance for n=%3.2f/%3.2f" %(n2,n1))
plt.xlabel("Angle of incidence in degrees")
plt.ylabel("Reflectance/Transmittance")
plt.xlim(0,90)
#plt.ylim(0,1.0)
#plt.axvline(56.31,color='grey', linestyle='--')
plt.axhline(0,color='grey', linestyle='--',linewidth=1)
plt.axhline(1,color='grey', linestyle='--',linewidth=1)
plt.axvline(AngB,color='grey', linestyle='--',linewidth=1)
if n<=1:
  plt.axvline(AngC,color='grey', linestyle='--',linewidth=1)
plt.legend()
plt.savefig("RTin1.5.pdf")
plt.show()
print("The Brewster angle is: %3.2f" %(AngB))
if n<=1:
  print("The critical angle is: %3.2f" %(AngC))
print("Reflectance for internal TE reflection = %3.3f" % ReX)
print("Reflectance for internal TM reflection = %3.3f" % RmX)
print("Transmittance for internal TE reflection = %3.3f" % TeX)
print("Transmittance for internal TM reflection = %3.3f" % TmX)

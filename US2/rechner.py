import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Generelle Abmessungen

oben, unten =np.genfromtxt("data/abmessungen.csv",delimiter=",",unpack=True)
dicke = 80.45-(oben+unten)
dreal=dicke
nummer = np.arange(1,12)
np.savetxt("data/abmessungentab.csv",np.column_stack([nummer,oben,unten,dicke]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f"])

#A-Scan

oben, unten = np.genfromtxt("data/ascan.csv",delimiter=",",unpack=True)
oben = oben-0.43
unten = unten-0.43
komplett = 60.55-0.43
c = 2730*0.001 #mm/μs


obenm = 1/2*c*oben
untenm = 1/2*c*unten
komplettm = 1/2*c*komplett
schutzschicht=komplettm-80.45
komplettm=komplettm-schutzschicht
obenm=obenm-schutzschicht
untenm= untenm-schutzschicht
print('komplettm= ', komplettm)
dicke = komplettm-(obenm+untenm)
dascan=dicke
np.savetxt("data/ascantab.csv",np.column_stack([nummer,oben,obenm,unten,untenm,dicke]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f","%3.2f","%3.2f"])

#Auflösung

oben = np.array([15.12-0.43, 13.74-0.43])
unten = np.array([44.34-0.43, 45.60-0.43])
obenm = (1/2)*c*oben
untenm = (1/2)*c*unten
obenm=obenm-schutzschicht
untenm= untenm-schutzschicht
dicke = komplettm-(obenm+untenm)
nummer2 = np.delete(nummer,[2,3,4,5,6,7,8,9,10,11])
#frequenz = np.array([1,2])
np.savetxt("data/auflosungtab.csv",np.column_stack([nummer2,oben,obenm,unten,untenm,dicke]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f","%3.2f","%3.2f"])

#B-Scan

oben, unten = np.genfromtxt("data/bscan.csv",delimiter=",",unpack=True)
oben = np.delete(oben,[9])
unten = np.delete(unten,[9])
#oben = oben-2.58
#unten = unten-2.58
obenm = (1/2)*c*oben
untenm = (1/2)*c*unten
dicke = komplettm-(obenm+untenm)
dbscan=dicke
nummer3 = np.delete(nummer,[9])
np.savetxt("data/bscantab.csv",np.column_stack([nummer3,oben,obenm,unten,untenm,dicke]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f","%3.2f","%3.2f"])

#Abweichungen und vergleiche
deltaascan=((dascan/dreal)-1)*100
deltaascan=np.absolute(deltaascan)
np.savetxt("data/ascanvgl.csv",np.column_stack([nummer,dreal,dascan,deltaascan]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f"])
dreal=np.delete(dreal,[9])
deltabscan=((dbscan/dreal)-1)*100
deltabscan=np.absolute(deltabscan)
np.savetxt("data/bscanvgl.csv",np.column_stack([nummer3,dreal,dbscan,deltabscan]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f"])


#Herz A-Scan
ruhe=66.96-0.53
maxpump=29.11-0.53
ht=ruhe-maxpump
c=1485*0.001 #mm/µs #dest. Wasser
a=57.65/2
h=(1/2)*c*ht
Vmax=(h*np.pi*(3*a**2+h**2))/6
Vmax=Vmax*10**(-3)
print("Höhe in mm",h)
print("maximales Schlagvolumen (A-Scan) in ml",Vmax)


#HZV
peaks=np.genfromtxt("data/herzscan.csv",delimiter=",",unpack=True)
oberkante=4.4
grundniveau=62.52
peaks=peaks-oberkante
grundniveau=grundniveau-oberkante
ht=grundniveau-peaks

h=(1/2)*c*ht

Vherz=(h*np.pi*(3*a**2+h**2))/6
Vherz=Vherz*10**(-3)
Vherzm=ufloat(np.mean(Vherz),sem(Vherz))
print("mittleres Herzvolumen in ml=",Vherzm)
HZV=Vherzm*84
HZV=HZV*10**(-3)
np.savetxt("data/herztab.csv",np.column_stack([peaks,ht,h,Vherz]),delimiter=",",fmt=["%3.2f","%3.2f","%3.2f","%3.2f"])
print("HZV in l/min=",HZV)

import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
import scipy.constants as const
from scipy.stats import sem
#Faktoren!!!
dUDy = np.array([1.2e-3,1.3e-3,1.3e-3])
dUNd = np.array([0.05e-3,0.1e-3,0.05e-3])
dUGd = np.array([0.2e-3,0.25e-3,0.3e-3])
F=8.66e-5
#dy nd gd
qreal= np.array([0.15e-4,0.08e-4,0.11e-4])

chiudy = F/qreal[0]*dUDy
chiudym = ufloat(np.mean(chiudy), sem(chiudy))
print("Chi(Dy), durch U berechnet:", chiudy, chiudym)

chiund = F/qreal[1]*dUNd
chiundm = ufloat(np.mean(chiund), sem(chiund))
print("Chi(Nd), durch U berechnet:", chiund, chiundm)

chiugd = F/qreal[2]*dUGd
chiugdm = ufloat(np.mean(chiugd), sem(chiugd))
print("Chi(Gd), durch U berechnet:", chiugd, chiugdm)

R3 = 998
dRDy = np.array([1255e-3,1410e-3,1700e-3])
dRNd = np.array([450e-3,410e-3,365e-3])
dRGd = np.array([770e-3,745e-3,870e-3])

chirdy = 2*F/qreal[0]*dRDy/R3
chirdym = ufloat(np.mean(chirdy),sem(chirdy))
print("Chi(Dy), durch R berechnet:",chirdy, chirdym)

chirnd = F/qreal[1]*dRNd/R3
chirndm = ufloat(np.mean(chirnd),sem(chirnd))
print("Chi(Nd), durch R berechnet:",chirnd, chirndm)

chirgd = F/qreal[2]*dRGd/R3
chirgdm = ufloat(np.mean(chirgd),sem(chirgd))
print("Chi(Gd), durch R berechnet:",chirgd, chirgdm)

chigesdy = (chiudym+chirdym)/2
chigesnd = (chiundm+chirndm)/2
chigesgd = (chiugdm+chirgdm)/2

print("Komplett gemittelte Chi(Dy,Nd,Gd)",chigesdy,chigesnd,chigesgd)

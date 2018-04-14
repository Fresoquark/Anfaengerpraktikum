import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

phir = np.array([79.0   , 209.3, 198.4, 201.4, 180.1, 223.2, 216.3])
phil = np.array([199.0  , 329.5, 318.5, 321.4, 300.2, 343.3, 336.3])
phi = 1/2*(phil-phir)
phim = np.mean(phi)
phimf=np.std(phi, ddof=1) / np.sqrt(len(phi))

omegar = np.array([237.1, 236.7, 236.4, 235.8, 235.3, 235.1, 234.3, 233.3])
omegal = np.array([119.8, 120.2, 120.6, 121.1, 121.6, 121.9, 122.7, 123.7])
eta = 180 - (omegar - omegal)

#degree to radians
phirad=np.deg2rad(phi)
phimr=np.mean(phirad)
phimfr=np.std(phirad, ddof=1) / np.sqrt(len(phirad))

phiu = unp.uarray(phimr, phimfr)

n = unp.sin((np.deg2rad(eta) + phiu)/2)/(unp.sin(phiu/2))

print('phi= ', phi)
print('phim= ', phim)
print('phimf= ', phimf)
print('eta= ', eta)
print('phiu= ', phiu)
print('n= ', n)

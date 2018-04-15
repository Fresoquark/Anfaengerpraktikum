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

n2 = np.array([3.08, 3.10, 3.12, 3.15, 3.18, 3.20, 3.24, 3.29])
lamda = np.array([643.85, 576.96, 546.07, 508.58, 479.99, 467.82, 404.65, 365.02])

def f(lamda, a, b):
    return a - b * lamda**2

params, covariance_matrix = curve_fit(f, lamda, n2, p0=(0.5,0.5))

errors = np.sqrt(np.diag(covariance_matrix))

As0 = params[0]
As2 = params[1]

print('As0 =', params[0], '+-', errors[0])
print('As2 =', params[1], '+-', errors[1])

sn2ssum = (n2 - As0 + As2 * lamda**2)**2
sn2s = 1/6 * np.sum(sn2ssum)

print('sn2ssum= ', sn2ssum)
print('sn2s= ', sn2s)

def g(lamda, a, b):
    return a + b / lamda**2

params, covariance_matrix = curve_fit(g, lamda, n2, p0=(0.5,0.5))

errors = np.sqrt(np.diag(covariance_matrix))

A0 = params[0]
A2 = params[1]

print('A0 =', params[0], '+-', errors[0])
print('A2 =', params[1], '+-', errors[1])

sn2sum = (n2 - A0 - A2 * lamda**2)**2
sn2 = 1/6 * np.sum(sn2sum)

print('sn2sum= ', sn2sum)
print('sn2= ', sn2)

#Abbesche Anzahl

nD = np.sqrt(A0 + A2 / 589**2)
nF = np.sqrt(A0 + A2 / 486**2)
nC = np.sqrt(A0 + A2 / 656**2)
nu = (nD - 1) / (nF - nC)

print('nC= ', nC)
print('nD= ', nD)
print('nF= ', nF)
print('nu= ', nu)

fraunhofer = np.array([656, 589, 486])
auflosung = 3e+7 * A2 / (fraunhofer**3 * np.sqrt(A0 + A2 / (fraunhofer**2) ))

print('Auflösungsvermögen= ', auflosung)

print('phi= ', phi)
print('phim= ', phim)
print('phimf= ', phimf)
print('eta= ', eta)
print('phiu= ', phiu)
print('n= ', n)
print('n= ', n**2)

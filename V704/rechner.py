import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Für Zink:

t, cts, d = np.genfromtxt("data/zink.csv", delimiter=",", unpack=True)
ctserr = np.sqrt(cts)
print('d: ', d)
print('t: ', t)
print('cts: ', cts, '+-', ctserr)
cts = cts/t
null=950/900
akt=cts-null
akterr = (ctserr-np.sqrt(950))/t
print('akt: ', akt, '+-', akterr )

r=2.82e-15
epsilon= 2.45
z = 30
Molvol = 9.16e-6
sigma = 2 * np.pi * r**2 * ((1+epsilon) / (epsilon**2) * ((2 * (1+epsilon)) / (1+2 * epsilon) - 1/(epsilon) * np.log(1+epsilon)) + 1/(2 * epsilon) * np.log(1 + 2 * epsilon) - (1+3 * epsilon)/ ((1+2 * epsilon)**2))
n = (z * 6.02214085774e23)/(Molvol)
mu = sigma * n

print('sigma: ', sigma)
print('n: ', n)
print('mu: ', mu)
#Für Blei:

print('----------------------------------------------')
tb, ctsb, db = np.genfromtxt("data/blei.csv", delimiter=",", unpack=True)
ctsberr = np.sqrt(ctsb)
print('db: ', db)
print('tb: ', tb)
print('ctsb: ', ctsb, '+-', ctsberr)
ctsb = ctsb/tb
nullb=950/900
aktb=ctsb-nullb
aktberr = (ctsberr-np.sqrt(950))/tb
print('aktb: ', aktb, '+-', aktberr )

zb = 82
Molvolb = 18.26e-6
nb = (zb * 6.02214085774e23)/(Molvolb)
mub = sigma * nb

print('sigma: ', sigma)
print('nb: ', nb)
print('mub: ', mub)

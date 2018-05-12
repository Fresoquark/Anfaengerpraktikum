import numpy as np
from uncertainties import ufloat
from scipy.stats import sem

spos, lpos1, lpos2 = np.genfromtxt("data/bessel1.csv", delimiter = ",", unpack = True)

e =  spos - 20
g1 = lpos1 - 20
b1 = e - g1
g2 = lpos2 - 20
b2 = e - g2

print("g1=", g1)
print("b1=", b1)
print("g2=", g2)
print("b2=", b2)

d1 = g1 - b1
f1 = (e**2 - d1**2)/(4*e)
f1mitt = ufloat(np.mean(f1), sem(f1))
print ("Die durch g1 und b1 ermittelten Brennweiten:",f1)
print ("Die durch g1 und b1 ermittelte mittlere Brennweite:",f1mitt)

d2 = g2 - b2
f2 = (e**2 - d2**2)/(4*e)
f2mitt = ufloat(np.mean(f2), sem(f2))
print ("Die durch g2 und b2 ermittelten Brennweiten:",f2)
print ("Die durch g2 und b2 ermittelte mittlere Brennweite:",f2mitt)

f = np.hstack([f1,f2])
fmitt = ufloat(np.mean(f), sem(f))

print ("Die durch g und b ermittelten Brennweiten:",f)
print ("Die durch g und b ermittelte mittlere Brennweite:",fmitt)

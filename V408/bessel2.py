import numpy as np
from uncertainties import ufloat
from scipy.stats import sem

spos, lpos1r, lpos2r, lpos1l, lpos2l = np.genfromtxt("data/bessel2.csv", delimiter = ",", unpack = True)

e =  spos - 20
g1r = lpos1r - 20
b1r = e - g1r
g2r = lpos2r - 20
b2r = e - g2r

print("g1r=", g1r)
print("b1r=", b1r)
print("g2r=", g2r)
print("b2r=", b2r)

d1r = g1r - b1r
f1r = (e**2 - d1r**2)/(4*e)
f1rmitt = ufloat(np.mean(f1r), sem(f1r))
print ("Die durch g1r und b1r ermittelten Brennweiten:",f1r)
print ("Die durch g1r und b1r ermittelte mittlere Brennweite:",f1rmitt)

d2r = g2r - b2r
f2r = (e**2 - d2r**2)/(4*e)
f2rmitt = ufloat(np.mean(f2r), sem(f2r))
print ("Die durch g2r und b2r ermittelten Brennweiten:",f2r)
print ("Die durch g2r und b2r ermittelte mittlere Brennweite:",f2rmitt)

fr = np.hstack([f1r,f2r])
frmitt = ufloat(np.mean(fr), sem(fr))

print ("Die durch g und b ermittelten Brennweiten rot:",fr)
print ("Die durch g und b ermittelte mittlere Brennweite rot:",frmitt)

g1l = lpos1l - 20
b1l = e - g1l
g2l = lpos2l - 20
b2l = e - g2l

print("g1l=", g1l)
print("b1l=", b1l)
print("g2l=", g2l)
print("b2l=", b2l)

d1l = g1l - b1l
f1l = (e**2 - d1l**2)/(4*e)
f1lmitt = ufloat(np.mean(f1l), sem(f1l))
print ("Die durch g1l und b1l ermittelten Brennweiten:",f1l)
print ("Die durch g1l und b1l ermittelte mittlere Brennweite:",f1lmitt)

d2l = g2l - b2l
f2l = (e**2 - d2l**2)/(4*e)
f2lmitt = ufloat(np.mean(f2l), sem(f2l))
print ("Die durch g2l und b2l ermittelten Brennweiten:",f2l)
print ("Die durch g2l und b2l ermittelte mittlere Brennweite:",f2lmitt)

fl = np.hstack([f1l,f2l])
flmitt = ufloat(np.mean(fl), sem(fl))

print ("Die durch g und b ermittelten Brennweiten blau:",fl)
print ("Die durch g und b ermittelte mittlere Brennweite blau:",flmitt)

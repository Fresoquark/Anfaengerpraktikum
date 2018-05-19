import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

line, I = np.genfromtxt("data/250Vmag.csv",delimiter=",",unpack=True)
d=(line-1)*6

B= 4* np.pi * 10e-7 *(8/np.sqrt(125)) * 20 * (I/0.282)
B=B* 10e3
print("Magnetfeldstärke:", B)
L=175 #Weg in mm

y= d/(L**2+d**2)
y=y*10e3

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, B, y)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
e= (a * np.sqrt(8*250))**2
print("e0/m0 = ",e)

plt.figure(figsize=(4.76, 2.94))
plt.plot(B, y, 'k.', label="Daten", ms=2.5)
plt.plot(B, f(B, *params), 'r-', label='Fit')
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"B / $\si{\milli\tesla}$")
plt.ylabel(r'$\frac{D}{L^2 + D^2}$ / $\si{\per\micro\metre}$')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/250Vmag.pdf')

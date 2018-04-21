import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

druck,kanal,counts= np.genfromtxt("data/5mm.txt")

energie = kanal / 1150 * 4
xeff = 5 * druck / 1013


def f(x, a, b):
    return a*x +b

params, covariance_matrix = curve_fit(f, xeff, energie)

errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
print('energie= ', energie)

plt.plot(xeff, energie, 'k.', label="Daten", ms=2.5)
plt.plot(xeff, f(xeff, *params), 'r-', label='Fit')


plt.xlabel(r'Effektive Länge / mm ')
plt.ylabel(r'Energie / MeV ')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/5mmenergie.pdf')

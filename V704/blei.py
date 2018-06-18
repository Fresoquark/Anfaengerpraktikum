import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, cts, d = np.genfromtxt("data/blei.csv", delimiter=",", unpack=True)
cts = cts/t
d=d*1e-4
null=950/900
cts=cts-null
errY = np.array([0.0, 0.0, 0.1, 0.1, 0.2, 0.3, 0.4, 0.6, 0.6, 0.8, 0.9, 1.0, 0.9])

ctsfit=np.delete(cts,[0]) #Der letzte wird weggelassen, da dieser wert dank der hintergrundstrahlung negativ ist
dfit=np.delete(d,[0])

def f(x, a, b):
    return np.exp(a*x)*b

params, covariance_matrix = curve_fit(f,dfit,ctsfit)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
b=ufloat(params[1],errors[1])

plt.yscale('log')
plt.errorbar(d, cts, yerr=errY, fmt='.k', label='Messdaten')
plt.plot(dfit, f(dfit, *params), 'r-', label='Linearer Fit')
#plt.plot(d, cts, 'k.', label="Messdaten", ms=2.5)
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"D / $\si{\metre}$")
plt.ylabel(r'$A_\text{total}$') #Achsenbeschriftung zu lang und ln() immer ohne Einheit
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/blei.pdf')

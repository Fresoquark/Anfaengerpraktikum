import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

afit=np.array([1.71926364226, 1.52086195034, 1.22806009196, 1.02422232825, 0.967994025908]) #Zuvor berechnete a
Ub=np.array([180, 200, 250, 280, 300])

xfit= 1 / Ub


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, xfit, afit)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])


plt.figure(figsize=(4.76, 2.94))
plt.plot(xfit, afit, 'k.', label="Daten", ms=2.5)
plt.plot(xfit, f(xfit, *params), 'r-', label='Fit')
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"$\frac{1}{U_B}$ / $\si{\per\volt}$")
plt.ylabel(r'$\frac{D}{U_d}$ / $\si{\milli\metre\per\volt}$')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/UB.pdf')

import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

B, A = np.genfromtxt("data/abbe.csv",delimiter=",",unpack=True)
V=B/3
gs=A-20
bs=55-A


x1= 1 + V

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, x1, bs)

errors = np.sqrt(np.diag(covariance_matrix))

print('f=', params[0], '+-', errors[0])
print('h=', params[1], '+-', errors[1])


plt.figure(figsize=(4.76, 2.94))
plt.plot(x1, bs, 'k.', label="Daten", ms=2.5)
plt.plot(x1, f(x1, *params), 'r-', label='Fit')
plt.legend(loc="best")
plt.grid()
plt.xlabel(r'$1 + V$')
plt.ylabel(r" $b'$ / cm")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/abbe2.pdf')

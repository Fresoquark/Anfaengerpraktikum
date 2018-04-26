import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x,I = np.genfromtxt("data/es.csv",delimiter = ",", unpack=True)

"""
def f(x, a, b):
    return a*x +b

params, covariance_matrix = curve_fit(f, xeff, energie)

errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])

"""
plt.plot(x, I, 'k.', label="Daten", ms=2.5)
#plt.plot(xeff, f(xeff, *params), 'r-', label='Fit')


plt.xlabel(r'Position / mm ')
plt.ylabel(r'Photostrom')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/es.pdf')

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x,I = np.genfromtxt("data/es.csv",delimiter = ",", unpack=True)
x = x-24
xbla= np.linspace(-15,15, 1000)
lada = 635 * 10**(-6)
L = 99.5 * 10

def f(x, a, b, c):
    #return a**2 * b**2 * (lada /( np.pi * b * np.sin(x/(L) + c )))**2 * np.sin(np.pi * b * np.sin(x /(L) + c ) / (lada))
    return a ** 2 * b**2 * np.sinc(np.pi * b * np.sin(x/L+c)/(lada))**2

params, covariance_matrix = curve_fit(f, x, I, p0=(1.4, 0.075, 0))

errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
print('c=', params[2], '+-', errors[2])


plt.plot(x, I, 'k.', label="Daten", ms=2.5)
plt.plot(xbla, f(xbla, *params), 'r-', label='Fit')


plt.xlabel(r'Position / mm ')
plt.ylabel(r'Photostrom')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/es.pdf')

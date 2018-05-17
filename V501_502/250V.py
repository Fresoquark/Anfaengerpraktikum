import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

line, ud = np.genfromtxt("data/250V.csv",delimiter=",",unpack=True)

d=(line-1)*6 #Ablenkung in mm

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, ud, d)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])


plt.figure(figsize=(4.76, 2.94))
plt.plot(ud, d, 'k.', label="Daten", ms=2.5)
plt.plot(ud, f(ud, *params), 'r-', label='Fit')
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"$U_d$ / V")
plt.ylabel(r'D / mm')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/250V.pdf')

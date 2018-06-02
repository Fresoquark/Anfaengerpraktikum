import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


z = np.array([30,35,38,40])
Ek = np.array([9.57,13.09,15.57,17.21])
Ek=Ek*1000
y=np.sqrt(Ek)

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, z, y)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
m=ufloat(params[0],errors[0])
eryd=m**2
print("Rydbergkonstante=",eryd)

plt.figure(figsize=(4.76, 2.94))
plt.plot(z, f(z, *params), 'r-', label='Fit')
plt.plot(z, y, 'k.', label="Daten", ms=2.5)
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"Z")
plt.ylabel(r'$\sqrt{E_K}$ / $\sqrt{\si{\electronvolt}}$')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/moseley.pdf')

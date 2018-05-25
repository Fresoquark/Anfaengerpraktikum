import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

def f(x, a, b):
    return a*x+b

plt.grid()
plt.xlabel(r"$\nu$ / $\si{\tera\hertz}$")
plt.ylabel(r'$U_g$ / $\si{\volt}$')

nu = np.array([467.69, 518.67, 549.07, 740.23, 819.11])
Ug = np.array([1.07, 0.61, 0.70, 1.22, 1.38])
nufit = np. delete(nu,[0])
Ugfit = np. delete(Ug,[0])
params, covariance_matrix = curve_fit(f, nufit, Ugfit)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])

plt.plot(nu,Ug, 'rx', label="$U_g$")
plt.plot(nufit, f(nufit, *params), 'b-', label='Fit')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/he0.pdf')

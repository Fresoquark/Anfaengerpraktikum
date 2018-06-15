import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, cts, d = np.genfromtxt("data/zink.csv", delimiter=",", unpack=True)
cts = cts/t
d=d*1e-4
null=950/900
cts=cts-null
cts=np.log(cts)

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f,d,cts)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
b=ufloat(params[1],errors[1])

plt.plot(d, f(d, *params), 'r-', label='Linearer Fit')
plt.plot(d, cts, 'k.', label="Datenpunkte", ms=2.5)
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"D / $\si{\metre}$")
plt.ylabel(r'ln(Counts - Hintergrundstrahlungscounts) / $\si{\per\second}$ ')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zink.pdf')

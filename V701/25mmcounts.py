import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

druck,kanal,counts= np.genfromtxt("data/25mm.txt")

xeff = 25 * druck / 1013


cfit = np.delete(counts,[0,1,2,3,4,5,6,7,8,9])
xfit = np.delete(xeff,[0,1,2,3,4,5,6,7,8,9])
def f(x, a, b):
    return a*x +b

params, covariance_matrix = curve_fit(f, xfit, cfit)

errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])

m=ufloat(params[0],errors[0])
c=ufloat(params[1],errors[1])

cmax=counts[0]
rm= ((cmax/2)-c)/m
ea=(rm/3.1)**(2/3)
print(ea)

print (rm)

plt.plot(xeff ,counts, 'k.', label="Daten", ms=2.5)
plt.plot(xfit, f(xfit, *params), 'r-', label='Fit')

plt.xlabel(r'Effektive Länge / mm')
plt.ylabel(r'Counts pro 120 Sekunden ')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/25mmcounts.pdf')

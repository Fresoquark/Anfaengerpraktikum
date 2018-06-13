import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, cts, d = np.genfromtxt("data/aluminium.csv", delimiter=",", unpack=True)
cts=cts/t
null=568/900
cts=cts-null
ctsfit1=np.delete(cts,[0,1,2,3,4,5,6,7,8])
dfit1=np.delete(d,[0,1,2,3,4,5,6,7,8])
ctsfit2=np.delete(cts,[8,9,10,11])
dfit2=np.delete(d,[8,9,10,11])


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f,dfit1,ctsfit1)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a1=ufloat(params[0],errors[0])
b1=ufloat(params[1],errors[1])
plt.plot(dfit1, f(dfit1, *params), 'r-', label='Fit 1')

params, covariance_matrix = curve_fit(f,dfit2,ctsfit2)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a2=ufloat(params[0],errors[0])
b2=ufloat(params[1],errors[1])
schnittfit=np.linspace(0,500)
plt.plot(schnittfit, f(schnittfit, *params), 'b-', label='Fit 2')

rmax=(b2-b1)/(a1-a2)
print("Rmax=",rmax)


plt.plot(d, cts, 'k.', label="Daten", ms=2.5)
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"D / $\si{\micro\metre}$")
plt.ylabel(r'Counts / $\si{\per\second}$')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/aluminium.pdf')

import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

l,r = np.genfromtxt("data/data2.txt")

eta = 180-l+r

ll,rr = np.genfromtxt("data/data1.txt")

Phi=(rr-ll)*0.5
phi0 = ufloat(np.mean(Phi),sem(Phi))
phi = np.mean(Phi)

eta = (np.pi)/180*eta
phi = (np.pi)/180*phi

n=(np.sin((eta+phi)/2))/(np.sin(phi/2))

n=n**2
lamda = np.genfromtxt("data/data3.txt")


def f(lamda, a, b):
    return a + b / lamda**2

params, covariance_matrix = curve_fit(f, lamda, n, p0=(0.5,0.5))

errors = np.sqrt(np.diag(covariance_matrix))

print('A0 =', params[0], '+-', errors[0])
print('A2 =', params[1], '+-', errors[1])

d= f(lamda, *params)
print (d)
d= np.sqrt(d)

plt.figure(figsize=(4.76, 2.94))
plt.plot(lamda, d, 'r-', label='Dispersionskurve')
plt.legend(loc="best")
plt.grid()
plt.xlabel(r'$ \lambda $ in $\mathrm{nm}$')
plt.ylabel(r'$n$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot4.pdf')

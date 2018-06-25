import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

omega,U = np.genfromtxt("data/verstaerker.csv",delimiter=",",unpack=True)
U = U/10
#12,13
#16,17
xlunten=omega[13]
ylunten=U[13]
xloben=omega[14]
yloben=U[14]
xroben=omega[17]
yroben=U[17]
xrunten=omega[18]
yrunten=U[18]

xfitl=np.array([xlunten,xloben])
yfitl=np.array([ylunten,yloben])
xfitr=np.array([xroben,xrunten])
yfitr=np.array([yroben,yrunten])
plt.axhline(0.6435,ls="--",lw=0.8,c="k")

def f(x,a,b):
    return a*x+b

params, covariance_matrix = curve_fit(f, xfitl, yfitl)
errors = np.sqrt(np.diag(covariance_matrix))
a=params[0]
b=params[1]
plt.plot(xfitl, f(xfitl, *params), 'b-',lw=0.8)
minus=(0.6435-b)/a
print("minus=",minus)
params, covariance_matrix = curve_fit(f, xfitr, yfitr)
errors = np.sqrt(np.diag(covariance_matrix))

a=params[0]
b=params[1]
plt.plot(xfitr, f(xfitr, *params), 'r-',lw=0.8)
plus=(0.6435-b)/a
print("plus=",plus)
max=(1/0.91)*0.6435



plt.grid()
plt.plot(omega, U,"k.",ms=2, label='Daten')
plt.plot(minus,0.6435,"kx",ms=3)
plt.plot(plus,0.6435,"kx",ms=3)
plt.xlabel(r'$\omega \:/\:\si{\kilo\hertz}$')
plt.ylabel(r'$\frac{U_A}{U_E} \:/\:\si{\volt}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/verstaerker.pdf')

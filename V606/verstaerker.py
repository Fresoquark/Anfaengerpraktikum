import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

omega,U = np.genfromtxt("data/verstaerker.csv",delimiter=",",unpack=True)
U = U/10
#12,13
#16,17
xlunten=omega[12]
ylunten=U[12]
xloben=omega[13]
yloben=U[13]
xroben=omega[16]
yroben=U[16]
xrunten=omega[17]
yrunten=U[17]

xfitl=np.array([xlunten,xloben])
yfitl=np.array([ylunten,yloben])
xfitr=np.array([xroben,xrunten])
yfitr=np.array([yroben,yrunten])

def f(x,a,b):
    return a*x+b

params, covariance_matrix = curve_fit(f, xfitl, yfitl)
errors = np.sqrt(np.diag(covariance_matrix))

a=params[0]
b=params[1]
minus=(0.6435-b)/a
print("minus=",minus)
#minus=35.01
params, covariance_matrix = curve_fit(f, xfitr, yfitr)
errors = np.sqrt(np.diag(covariance_matrix))

a=params[0]
b=params[1]
plus=(0.6435-b)/a
print("plus=",plus)
#plus=35.34
max=(1/0.91)*0.6435



plt.grid()
plt.plot(omega, U,"k.",ms=2, label='Daten')
plt.axvline(35.01,ymin=0,ymax=max,c="b",ls="--")
plt.axvline(35.34,ymin=0,ymax=max,c="r",ls="--")
plt.xlabel(r'$\omega \:/\:\si{\kilo\hertz}$')
plt.ylabel(r'$\frac{U_A}{U_E} \:/\:\si{\volt}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/verstaerker.pdf')

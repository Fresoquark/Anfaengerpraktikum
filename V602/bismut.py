import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

theta, counts = np.genfromtxt("data/bismut.csv",delimiter=",",unpack=True)

theta=0.5*theta
l2 = theta[6]
l3= theta[27]
print("L2 bei ",l2)
print("L3 bei ",l3)

plt.figure(figsize=(4.76, 2.94))
plt.axvline(l2,color="r",label="Position der L2-Kante")
plt.axvline(l3,color="b",label="Position der L3-Kante")
plt.plot(theta, counts, 'k.', label="Daten", ms=2.5)
plt.legend(loc="best")
plt.grid()
plt.xlabel(r'$\theta$ / $\si{\degree}$')
plt.ylabel(r'Rate / $\si{\per\second}$')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/bismut.pdf')

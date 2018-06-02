import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

theta, counts = np.genfromtxt("data/zink.csv",delimiter=",",unpack=True)

theta=0.5*theta


plt.figure(figsize=(4.76, 2.94))
plt.plot(theta, counts, 'k.', label="Daten", ms=2.5)
plt.legend(loc="best")
plt.grid()
plt.xlabel(r'$\theta$ / $\si{\degree}$')
plt.ylabel(r'Rate / $\si{\per\second}$')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zink.pdf')

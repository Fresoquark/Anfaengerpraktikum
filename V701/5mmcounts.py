import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

druck,kanal,counts= np.genfromtxt("data/5mm.txt")

xeff = 5 * druck / 1013

plt.plot(xeff ,counts)

plt.xlabel(r'Effektive Länge / mm')
plt.ylabel(r'Counts pro 120 Sekunden ')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/5mmcounts.pdf')

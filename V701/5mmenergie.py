import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

druck,kanal,counts= np.genfromtxt("data/5mm.txt")

energie = kanal / 1150 * 4
xeff = 5 * druck / 1013

plt.plot(xeff ,energie)

plt.xlabel(r'Effektive Länge / mm ')
plt.ylabel(r'Energie / MeV ')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/5mmenergie.pdf')

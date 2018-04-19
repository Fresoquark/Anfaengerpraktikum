import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

druck,kanal,counts= np.genfromtxt("data/25mm.txt")

energie = kanal / 1199 * 4

plt.plot(druck,energie)

#plt.xlabel(r'Counts pro $10 \si{\seconds}$')
#plt.ylabel(r'Absolute Häufigkeit')
#plt.legend(loc='best')
# in matplotlibrc leider (noch) nicht möglich
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('build/histo.pdf')
plt.show()

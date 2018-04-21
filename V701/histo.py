import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x=np.genfromtxt("data/histo.txt")
plt.hist(x,bins=10)
plt.xlabel(r'Counts pro 10 Sekunden')
plt.ylabel(r'Absolute Häufigkeit')
plt.legend(loc='best')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/histo.pdf')

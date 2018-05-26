import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

U,I=np.genfromtxt("data/messreihe2.csv",delimiter=",",unpack=True)



plt.grid()
plt.xlabel(r"$U$ / $\si{\volt}$")
plt.ylabel(r'$I$ / $\SI{100}{\pico\ampere}$')
plt.plot(U,I, 'k.', label="$Daten$")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/messreihe2.pdf')

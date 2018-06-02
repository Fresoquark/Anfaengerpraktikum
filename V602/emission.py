import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import uncertainties.unumpy as unp

theta, counts = np.genfromtxt("data/emissionsspektrum.csv",delimiter=",",unpack=True)

theta=0.5*theta


plt.figure(figsize=(4.76, 2.94))
plt.plot((20.2,20.2), (0, 5050), 'r-')
plt.text(18, 4000, r'$K_\beta$', color='red')
plt.plot((22.5,22.5), (0, 5050), 'b-')
plt.text(23.5, 4000, r'$K_\alpha$', color='blue')
plt.text(10, 1000, r'Bremsberg', color='black')
plt.plot(theta, counts, 'k.', label="Daten", ms=2.5)
plt.legend(loc="best")
plt.grid()
plt.xlabel(r'$\theta$ / $\si{\degree}$')
plt.ylabel(r'Rate / $\si{\per\second}$')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/emission.pdf')

E  = [0.404,0.421]
Em = np.mean(E)
Ef =np.std(E, ddof=1) / np.sqrt(len(E))

print('Em= ', Em)
print('Ef= ', Ef)

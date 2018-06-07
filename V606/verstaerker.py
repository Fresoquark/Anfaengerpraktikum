import matplotlib.pyplot as plt
import numpy as np

omega,U = np.genfromtxt("data/verstaerker.csv",delimiter=",",unpack=True)

plt.grid()
plt.plot(omega, U,"k.",ms=2, label='Daten')
plt.xlabel(r'$\omega \:/\:\si{\kilo\hertz}$')
plt.ylabel(r'$U \:/\:\si{\volt}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/verstaerker.pdf')

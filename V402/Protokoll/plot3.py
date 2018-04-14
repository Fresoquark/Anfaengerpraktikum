import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

y = np.array([3.08, 3.10, 3.12, 3.15, 3.18, 3.20, 3.24, 3.29])
x = np.array([643.85, 576.96, 546.07, 508.58, 479.99, 467.82, 404.65, 365.02])


plt.plot(x, y, 'k.', label='Messwerte')
plt.xlabel(r'$\lambda \:/\: nm$')
plt.ylabel(r'$\text{n}^2$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.grid()
plt.savefig('build/plot3.pdf')

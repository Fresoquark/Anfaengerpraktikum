import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

phir = np.array([79.0   , 209.3, 198.4, 201.4, 180.1, 223.2, 216.3])
phil = np.array([199.0  , 329.5, 318.5, 321.4, 300.2, 343.3, 336.3])
phi = 1/2*(phil-phir)
phim = np.mean(phi)
phimf=np.std(phi, ddof=1) / np.sqrt(len(phi))

print('phi= ', phi)
print('phim= ', phim)
print('phimf= ', phimf)

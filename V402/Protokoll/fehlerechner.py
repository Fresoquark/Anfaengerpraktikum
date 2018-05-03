import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat

a0 = ufloat(2.99,0.0100)
a2 = ufloat(42087.3,2904.23)

l = np.array([656,589,486])

fraunhofer = unp.sqrt(a0 + (a2 / l**2))

print ("C,d,f = ", fraunhofer)

abbe = (fraunhofer[1]-1)/(fraunhofer[2]-fraunhofer[0])

print(abbe)

A = 3e+7 * a2/ l**3 * unp.sqrt( a0 + ( a2 / l**2))

print ("C,d,f = ", A)

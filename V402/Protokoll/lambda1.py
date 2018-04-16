import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

A0 = ufloat(2.99, 0.01)
A2 = ufloat(42087.3, 2904.23)

lambda1 = unp.sqrt(A2/(A0-1))
print (lambda1)

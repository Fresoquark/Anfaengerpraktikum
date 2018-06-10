import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
import scipy.constants as const
#nd gd dy
gj = np.array([0.72,2,1.33])
rho = np.array([7.24,7.40,7.8]) #g/cm3
M = np.array([336.48,362.5,372.998]) #g/mol
J = np.array([4.5,3.5,7.5])
mub = 0.5* const.hbar * const.e/const.m_e
T= 298.15

rho =rho*1000
M = M*0.001

N=rho/M*const.N_A
chi = (const.mu_0 * mub**2 * gj**2 * N * J * (J+1) ) / (3 * const.k * T)

print("Chi(Nd,Gd,Dy) in m^3/mol = ",chi)

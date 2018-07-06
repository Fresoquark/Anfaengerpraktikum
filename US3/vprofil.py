import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

µs, f1, s1, f2, s2 = np.genfromtxt("data/vprofil.csv",delimiter=",",unpack=True)

mm=((µs-(30.07*(2/5)))*(3/2)) # Umrechnung in mm und Abziehen der Vorlaufstrecke

alpha=np.array([80.06,70.53,54.74])
alpha=np.deg2rad(alpha)
nu0=2000000 #nu0 in Hz
cl=1800 #Schallgeschwindigkeit in m/s
v1=(f1*cl)/(2*nu0*np.cos(alpha[0]))
v2=(f2*cl)/(2*nu0*np.cos(alpha[0]))

np.savetxt("data/vprofiltab.csv",np.column_stack([µs,mm,f1,v1,s1,f2,v2,s2]),delimiter=",",fmt=["%2.1f","%2.2f","%3.0f","%2.2f","%2.1f","%3.0f","%2.2f","%2.1f"])


plt.plot(mm, v1, 'k.', label="Daten", ms=2.5)

plt.xlabel(r'z / $\si{\milli\metre}$')
plt.ylabel(r'$v_{70}$ / $\si{\metre\per\second}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/v1.pdf')
plt.clf()
plt.plot(mm, v2, 'k.', label="Daten", ms=2.5)

plt.xlabel(r'z / $\si{\milli\metre}$')
plt.ylabel(r'$v_{45}$ / $\si{\metre\per\second}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/v2.pdf')
plt.clf()
plt.plot(mm, s1, 'k.', label="Daten", ms=2.5)

plt.xlabel(r'z / $\si{\milli\metre}$')
plt.ylabel(r'$I_\text{Streu,70}$ / $\si{\percent}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/streu1.pdf')
plt.clf()
plt.plot(mm, s2, 'k.', label="Daten", ms=2.5)

plt.xlabel(r'z / $\si{\milli\metre}$')
plt.ylabel(r'$I_\text{Streu,45}$ / $\si{\percent}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/streu2.pdf')

import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

rpm,a,b,c=np.genfromtxt("data/duenn.csv",delimiter=",",unpack=True)    # a=15 b=30 c=60
vfluss=(100/9200)*rpm   #Fließgeschwindigkeit in Prozent
alpha=np.array([80.06,70.53,54.74])
alpha=np.deg2rad(alpha)
nu0=2000000 #nu0 in Hz
cl=1800 #Schallgeschwindigkeit in m/s
v15=(a*cl)/(2*nu0*np.cos(alpha[0]))
v30=(b*cl)/(2*nu0*np.cos(alpha[1]))
v60=(c*cl)/(2*nu0*np.cos(alpha[2]))

vm=np.array([np.mean([v15[0],v30[0],v60[0]]),np.mean([v15[1],v30[1],v60[1]]),np.mean([v15[2],v30[2],v60[2]]),np.mean([v15[3],v30[3],v60[3]]),np.mean([v15[4],v30[4],v60[4]])])
vmerr=np.array([sem([v15[0],v30[0],v60[0]]),sem([v15[1],v30[1],v60[1]]),sem([v15[2],v30[2],v60[2]]),sem([v15[3],v30[3],v60[3]]),sem([v15[4],v30[4],v60[4]])])



np.savetxt("data/duenntab.csv",np.column_stack([vfluss,a,v15,b,v30,c,v60,vm,vmerr]),delimiter=",",fmt=["%2.0f","%4.0f","%4.2f","%4.0f","%4.2f","%4.0f","%4.2f","%4.2f","%4.2f"])





yplot=b/np.cos(alpha[0])

plt.plot(v30, yplot, 'k.', label="Daten", ms=2.5)

plt.xlabel(r'v / $\si{\metre\per\second}$')
plt.ylabel(r'$\frac{\Delta\nu}{\cos(\alpha)}$ / $\si{\hertz}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/duenn30.pdf')
plt.clf()

yplot=a/np.cos(alpha[0])

plt.plot(v15, yplot, 'k.', label="Daten", ms=2.5)

plt.xlabel(r'v / $\si{\metre\per\second}$')
plt.ylabel(r'$\frac{\Delta\nu}{\cos(\alpha)}$ / $\si{\hertz}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/duenn15.pdf')
plt.clf()

yplot=c/np.cos(alpha[0])

plt.plot(v60, yplot, 'k.', label="Daten", ms=2.5)

plt.xlabel(r'v / $\si{\metre\per\second}$')
plt.ylabel(r'$\frac{\Delta\nu}{\cos(\alpha)}$ / $\si{\hertz}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/duenn60.pdf')

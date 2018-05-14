import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



x=np.genfromtxt("data/histo.txt")
mean=np.mean(x)
sem=sem(x)
std=np.std(x)
var=std**2
print(mean,"+-",sem,"Varianz=",var)
x1=np.linspace(np.min(x),np.max(x))

gaus=np.random.normal(loc=mean,scale=std,size=10000)
poii=np.random.poisson(lam=mean,size=10000)


plt.grid()
plt.hist(x,bins=10,density=True,label="Verteilung der Messwerte")
plt.hist(poii,bins=10,density=True,histtype="step",color="k",label="Poissonverteilung")
plt.hist(gaus,bins=10,density=True,histtype="step",color="r",label="Normalverteilung")
plt.xlabel(r'Counts pro 10 Sekunden')
plt.ylabel(r'Relative Häufigkeit')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/histo.pdf')

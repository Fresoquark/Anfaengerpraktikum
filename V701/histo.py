import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import laplace
from scipy.stats import norm


x=np.genfromtxt("data/histo.txt")
mean=np.mean(x)
sem=sem(x)
std=np.std(x)
var=std**2
print(mean,"+-",sem,"Varianz=",var)
x1=np.linspace(np.min(x),np.max(x))

lap=laplace.pdf(x1,loc=mean,scale=std)
gau=norm.pdf(x1,loc=mean,scale=std)



plt.hist(x,bins=10,density=True)
plt.plot(x1,gau,"r-",label="Normalverteilung")
plt.plot(x1,lap,"k-",label="Laplaceverteilung")
plt.xlabel(r'Counts pro 10 Sekunden')
plt.ylabel(r'Relative Häufigkeit')
plt.legend(loc='best')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/histo.pdf')

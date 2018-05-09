import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt

lpos, spos, B = np.genfromtxt("data/linse1.csv",delimiter=",", unpack = True)

g=lpos-20
b=spos-lpos

V1= B/3
V2= b/g
print("Durch Bildgroesse berechneter Massstab V=", V1)
print("Durch b und g berechneter Massstab V=", V2)

f= 1 / (1/b + 1/g)
print ("Berechnete Brennpunkte:",f)
fmitt = ufloat(np.mean(f),sem(f))
print("Gemittelter Brennpunkt mit Fehler:",fmitt)

x2=np.linspace(0,15,1000)

def f(x,a,c):
    return a * x + c

m= b/(-g)

plt.xlim(0,np.max(g)+2)
plt.ylim(0,np.max(b)+2)
plt.plot(x2, f(x2,m[0],b[0]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[1],b[1]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[2],b[2]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[3],b[3]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[4],b[4]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[5],b[5]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[6],b[6]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[7],b[7]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[8],b[8]), 'k-', linewidth=0.5)
plt.plot(x2, f(x2,m[9],b[9]), 'k-', linewidth=0.5)

plt.xlabel(r'g / cm')
plt.ylabel(r'b / cm')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/linse1.pdf')

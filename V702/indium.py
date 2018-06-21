import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

N=np.genfromtxt("data/indium.csv",delimiter=",",unpack=True)
t=np.arange(1,16,1)
t=t*240
#Muss den Nulleffekt noch abziehen, habe aber gerade die Daten nicht da
null=256/600*240 #Dieser Wert ist frei erfunden werde den Richtigen noch ergänzen
nullerr=np.sqrt(null)
N0=N
Nerr=np.sqrt(N)
N0err=Nerr
N=N-null
Nerr=Nerr-nullerr
lnN=np.log(N)
lnNerroben=np.log(N+Nerr)-np.log(N)
lnNerrunten=np.log(N)-np.log(N-Nerr)
lnNerr=np.stack((lnNerroben,lnNerrunten))


np.savetxt("data/indtab.csv",np.column_stack([t,N0,N0err,N,Nerr,lnN,lnNerroben,lnNerrunten]),delimiter=",",fmt=["%4.0f","%4.0f","%4.0f","%4.0f","%2.0f","%4.3f","%4.3f","%4.3f"])

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f,t,lnN)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])

plt.grid()
plt.errorbar(t, lnN, yerr=lnNerr, fmt='.k', label='Messdaten')
plt.plot(t, f(t, *params), 'r-', label='Linearer Fit')
#plt.plot(d, cts, 'k.', label="Messdaten", ms=2.5)
plt.legend(loc="best")
plt.xlabel(r"t / $\si{\second}$")
plt.ylabel(r'ln(N)') #Achsenbeschriftung zu lang und ln() immer ohne Einheit
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/indium.pdf')

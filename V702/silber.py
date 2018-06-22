import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

N=np.genfromtxt("data/silber.csv",delimiter=",",unpack=True)
t=np.arange(1,43,1)
t=t*10
null=223/900*10
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

#np.savetxt("data/silbertab.csv",np.column_stack([t,N0,N0err,N,Nerr,lnN,lnNerroben,lnNerrunten]),delimiter=",",fmt=["%3.0f","%3.0f","%2.1f","%3.0f","%2.1f","%1.3f","%1.3f","%1.3f"])
np.savetxt("data/silbtab.csv",np.column_stack([t,N0,N0err,N,Nerr,lnN,lnNerroben,lnNerrunten]),delimiter=",",fmt=["%4.0f","%4.0f","%4.1f","%4.1f","%2.1f","%4.3f","%4.3f","%4.3f"])

#def f(x, a, b):
#    return a*x+b

#params, covariance_matrix = curve_fit(f,t,lnN)
#errors = np.sqrt(np.diag(covariance_matrix))

#print('a=', params[0], '+-', errors[0])
#print('b=', params[1], '+-', errors[1])

plt.grid()
plt.errorbar(t, lnN, yerr=lnNerr, fmt='.k', label='Messdaten')
#plt.plot(t, f(t, *params), 'r-', label='Linearer Fit')
#plt.plot(d, cts, 'k.', label="Messdaten", ms=2.5)
plt.legend(loc="best")
plt.xlabel(r"t / $\si{\second}$")
plt.ylabel(r'ln(N)') #Achsenbeschriftung zu lang und ln() immer ohne Einheit
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/silber.pdf')

#Zweiter Plot für langlebiges Zeug
plt.gcf().clear()

lang = np.arange(0,10,1)
lnN2=np.delete(lnN,[lang])
lnN2erroben=np.delete(lnNerroben,[lang]) #ist unnötig
lnN2errunten=np.delete(lnNerroben,[lang]) #ist unnötig
lnN2err=np.stack((lnN2erroben,lnN2errunten)) #ist unnötig
t2 = np.delete(t, [lang])

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f,t2,lnN2)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])

plt.grid()
plt.errorbar(t, lnN, yerr=lnNerr, fmt='.k', label='Messdaten')
plt.plot(t2, f(t2, *params), color='tab:blue', label='Linearer Fit')
#plt.plot(d, cts, 'k.', label="Messdaten", ms=2.5)
plt.legend(loc="best")
plt.xlabel(r"t / $\si{\second}$")
plt.ylabel(r'ln(N)') #Achsenbeschriftung zu lang und ln() immer ohne Einheit
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/silber2.pdf')

#Dritter Plot für kurzlebiges Zeug
plt.gcf().clear()

kurz = np.arange(10,43,1)
lnN3=np.delete(lnN,[kurz])
#lnN3=lnN3-3.40
lnN3erroben =np.delete(lnNerroben,[kurz]) #ist unnötig
lnN3errunten=np.delete(lnNerroben,[kurz]) #ist unnötig
lnN3err=np.stack((lnN3erroben,lnN3errunten)) #ist unnötig
t3 = np.delete(t, [kurz])

params2, covariance_matrix2 = curve_fit(f,t3,lnN3)
errors2 = np.sqrt(np.diag(covariance_matrix2))

print('a2=', params2[0], '+-', errors2[0])
print('b2=', params2[1], '+-', errors2[1])

plt.grid()
plt.errorbar(t, lnN, yerr=lnNerr, fmt='.k', label='Messdaten')
plt.plot(t3, f(t3, *params2), color='tab:orange', label='Linearer Fit')
#plt.plot(d, cts, 'k.', label="Messdaten", ms=2.5)
plt.legend(loc="best")
plt.xlabel(r"t / $\si{\second}$")
plt.ylabel(r'ln(N)') #Achsenbeschriftung zu lang und ln() immer ohne Einheit
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/silber3.pdf')

#Finaler Plot
plt.gcf().clear()

lang2 = np.arange(0,7,1)
t2fit=np.delete(t,[lang2])
kurz2 = np.arange(13,43,1)
t3fit=np.delete(t,[kurz2])

plt.grid()
plt.errorbar(t, lnN, yerr=lnNerr, fmt='.k', label='Messdaten')
plt.plot(t3fit, f(t3fit, *params2), color='tab:orange', label='Kurzlebiger Fit')
plt.plot(t2fit, f(t2fit, *params), color='tab:blue', label='Langlebiger Fit')
#plt.plot(d, cts, 'k.', label="Messdaten", ms=2.5)
plt.legend(loc="best")
plt.xlabel(r"t / $\si{\second}$")
plt.ylabel(r'ln(N)') #Achsenbeschriftung zu lang und ln() immer ohne Einheit
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/silberf.pdf')

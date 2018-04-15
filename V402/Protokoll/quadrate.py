import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

l,r = np.genfromtxt("data/data2.txt")

eta = 180-l+r

ll,rr = np.genfromtxt("data/data1.txt")

Phi=(rr-ll)*0.5
phi0 = ufloat(np.mean(Phi),sem(Phi))
phi = np.mean(Phi)

eta = (np.pi)/180*eta
phi = (np.pi)/180*phi

n=(np.sin((eta+phi)/2))/(np.sin(phi/2))

n=n**2
lamda = np.genfromtxt("data/data3.txt")

st1= n -2.99 -(42087/(lamda**2))
st1=st1**2

sn1 = (1/6) * np.sum(st1)
print (sn1)

st2= n -3.36 -(7.6 * (10**(-7)) *(lamda**2))
st2 = st2**2
sn2 = (1/6) * np.sum(st2)
print (sn2)

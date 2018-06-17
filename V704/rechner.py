import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Für Zink:

t, cts, d = np.genfromtxt("data/zink.csv", delimiter=",", unpack=True)
ctserr = np.sqrt(cts)
print('d: ', d)
print('t: ', t)
print('cts: ', cts, '+-', ctserr)
cts = cts/t
null=950/900
akt=cts-null
akterr = (ctserr-np.sqrt(950))/t
print('akt: ', akt, '+-', akterr )

#Für Blei:

print('----------------------------------------------')
tb, ctsb, db = np.genfromtxt("data/blei.csv", delimiter=",", unpack=True)
ctsberr = np.sqrt(ctsb)
print('db: ', db)
print('tb: ', tb)
print('ctsb: ', ctsb, '+-', ctsberr)
ctsb = ctsb/tb
nullb=950/900
aktb=ctsb-nullb
aktberr = (ctsberr-np.sqrt(950))/tb
print('aktb: ', aktb, '+-', aktberr )

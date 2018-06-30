import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Generelle Abmessungen

oben, unten =np.genfromtxt("data/abmessungen.csv",delimiter=",",unpack=True)
dicke = 80.45-(oben+unten)
nummer = np.arange(1,12)
np.savetxt("data/abmessungentab.csv",np.column_stack([nummer,oben,unten,dicke]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f"])

#A-Scan

oben, unten = np.genfromtxt("data/ascan.csv",delimiter=",",unpack=True)
oben = oben-0.43
unten = unten-0.43
komplett = 60.55-0.43
c = 2730*0.001 #mm/μs

obenm = 1/2*c*oben
untenm = 1/2*c*unten
komplettm = 1/2*c*komplett
print('komplettm= ', komplettm)
dicke = komplettm-(obenm+untenm)
np.savetxt("data/ascantab.csv",np.column_stack([nummer,oben,obenm,unten,untenm,dicke]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f","%3.2f","%3.2f"])

#Auflösung

oben = np.array([15.12-0.43, 13.74-0.43])
unten = np.array([44.34-0.43, 45.60-0.43])
obenm = 1/2*c*oben
untenm = 1/2*c*unten
dicke = komplettm-(obenm+untenm)
nummer2 = np.delete(nummer,[2,3,4,5,6,7,8,9,10,11])
#frequenz = np.array([1,2])
np.savetxt("data/auflosungtab.csv",np.column_stack([nummer2,oben,obenm,unten,untenm,dicke]),delimiter=",",fmt=["%3.0f","%3.2f","%3.2f","%3.2f","%3.2f","%3.2f"])

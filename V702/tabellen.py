import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ind=np.genfromtxt("data/indium.csv",delimiter=",",unpack=True)
sil=np.genfromtxt("data/silber.csv",delimiter=",",unpack=True)

inderr=np.sqrt(ind)
silerr=np.sqrt(sil)
lnind=np.log(ind)
lnsil=np.log(sil)



inderr=np.round(inderr,2)
lnind=np.round(lnind,2)
np.savetxt("data/indtab.csv",np.column_stack([ind,inderr,lnind]),delimiter=",",fmt=["%4.0f","%2.0f","%2.2f"])

import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x=np.genfromtxt("data/histo.txt")
y= ufloat(np.mean(x),sem(x))
print("Mittelwert pm Standardabweichung = ",y)

import numpy as np
from uncertainties import ufloat
from scipy.stats import sem

f=np.array([39.92, 79.79, 159.55, 239.32])
f[0]= f[0]*2
f[2]= f[2]/2
f[3]= f[3]/3

print ("Die auf n=1 normierten Frequenzen:",f)

fmitt=ufloat(np.mean(f),sem(f))

print ("Die gemittelte Frequenz:",fmitt)

#alles in mm
p=10.3 #Kondesatorlänge
d=9.5 #Plattenabstand
L=143 #Weglänge nach Kondesator
D=14 #gmessene Ablenkung

e=(p*L)/(2*d*350) #Empfindlichkeit

Ud=D/e #Scheitelwert der Spannung
print ("Die Spannung betraägt:",Ud)

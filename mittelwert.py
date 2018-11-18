import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def mittel(a1, a2, t):
    am = np.mean(a1/a2)
    amf = np.std(a1/a2, ddof=1) /np.sqrt(len(a1))
    tm = np.mean(t)
    tmf = np.std(t, ddof=1) /np.sqrt(len(t))
    return am, tm, amf, tmf
def kappa(am, tm, rho, c, x):
    k = (rho * c * x**2)/( 2* unp.log(am) * tm)
    #dk = np.sqrt((rho * c * x**2)**2/( -2* np.log(4) * 66.66**2)**2 * 4.33**2 + (rho * c * x**2)**2/(-1* 2*4* (np.log(4))**2 * 66.67)**2 *0.15**2)
    return k


werte = csv_read("csv/edelstahl.csv")
data1 = np.zeros(3)
data2 = np.zeros(3)
datat = np.zeros(3)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        data1[i] = float(values[0])
        data2[i] = float(values[1])
        datat[i] = float(values[2])
        i+=1

a, t, af, tf = mittel (data1, data2, datat)
au = ufloat(a, af)
tu = ufloat(t,tf)
#ka = kappa (au, tu, 8520, 385, 0.032)
#ka = kappa(au,tu,2800,830,0.032)
ka = kappa (au,tu,8000,400,0.032)
print(a, af)
print(t, tf)
print(ka)
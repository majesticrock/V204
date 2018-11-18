import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def waermestrom(a, kappa, ta, tb, x):
    ergebnis = np.zeros(5)
    diff = np.zeros(5)
    i= 0
    for values in ta:
        ergebnis[i] = - ((ta[i] - tb[i]) / x )* kappa * a 
        diff[i] = ta[i] -tb[i]
        i=i+1
    return ergebnis, diff


werte = csv_read("csv/temperaturen.csv")
datat = np.zeros(5)
data1 = np.zeros(5)
data2 = np.zeros(5)
data3 = np.zeros(5)
data4 = np.zeros(5)
data5 = np.zeros(5)
data6 = np.zeros(5)
data7 = np.zeros(5)
data8 = np.zeros(5)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        datat[i] = float(values[0])
        data1[i] = float(values[1])
        data2[i] = float(values[2])
        data3[i] = float(values[3])
        data4[i] = float(values[4])
        data5[i] = float(values[5])
        data6[i] = float(values[6])
        data7[i] = float(values[7])
        data8[i] = float(values[8])
        i+=1

ergebnis1, diff1 = waermestrom(4.8*10**-5, 113, data2, data1, 0.032) 
ergebnis2, diff2 = waermestrom(2.8*10**-5, 113, data3, data4, 0.032)
ergebnis3, diff3 = waermestrom(4.8*10**-5, 235, data6, data5, 0.032)
ergebnis4, diff4 = waermestrom(4.8*10**-5, 20, data7, data8, 0.032)
print("messingbreit", ergebnis1, diff1)
print("messingschmal", ergebnis2, diff2)
print("alu", ergebnis3, diff3)
print("stahl", ergebnis4, diff4)
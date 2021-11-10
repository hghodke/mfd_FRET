# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:52:01 2021
This script fits exponentials to distributions
@author: bishnu
"""

from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
import numpy as np
from matplotlib import rc
import os
from natsort import natsorted
import glob
from scipy.optimize import curve_fit
import sympy as sym

#Load data using path for the list of files
path = src_path

all_files = glob.glob(path + "/*.dat")

li = []

# filtering data using for loop
for filename in all_files:
    
    df = pd.read_fwf(filename, index_col=None)
    df1 = pd.DataFrame(df)
    df1.columns = ["Time(s)", "Donor", "Acceptor", "FRET", "Idealized-FRET"]
    df2 = df1[(df1["FRET"]>0.35) & (df1["FRET"]<0.5)]
    
    length = len(df2)/5
 
    li.append(length)
# converting list inot dataframe
li1 = pd.DataFrame(li)
li2 = li1[li1[:]>1]
li3 = li2.dropna()

li3.to_csv(".csv", index=None) # provide path
# Making counts of histogram 
hist = np.histogram(li3, density=True)[0]

# choosing x length to fit entire histogram
x = np.arange(0, len(hist), 1)

x_fit = x + x/2

# Defining single exponential function
def exp_fit(x, a, b):
    return a*np.exp(-b*x)

# plotting and fitting data 
plt.figure(figsize=(5,4))
fit = curve_fit(exp_fit, x_fit, hist, p0=[2,0.5]) # parameter should optimize here
fit_eq = fit[0][0]*np.exp(-fit[0][1]*x_fit)
plt.bar(x_fit, hist, align="edge")
plt.plot(x_fit, fit_eq, color="red")
plt.xlabel("time (s)")
plt.ylabel("Density")
plt.xlim(0,40)

plt.show()

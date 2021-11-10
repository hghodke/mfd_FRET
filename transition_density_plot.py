# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:51:06 2021

This script creates transition density plots
@author: bishnu
"""

from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
import numpy as np

filename = “_dwelldata.txt”
A = pd.read_table(filename, header = None)
print(A.head(5))
A.columns = ['Molecule', 'FRET before transition', 'FRET after transition', 'Time']
print(A.head(5))
# Creating bins 
x = A['FRET before transition']
y = A['FRET after transition']
z = A['Molecule']
x_min = np.min(x) 
x_max = np.max(x)

plt.figure(figsize = (6, 6))
kdeplot = sns.jointplot(x, y, ratio = 6, gridsize = 100, xlim = (0, 1.2), kind = 'kde', ylim = (0, 1.2), color = 'skyblue', shade_lowest = False)

kdeplot.ax_joint.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
kdeplot.ax_joint.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

plt.show()

Plot Traces
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
from scipy.signal import savgol_filter

import numpy as np
filename = “ “  # provide path either .dat file or .csv file
x = np.loadtxt(filename)
D = x[:, 1]
A = x[:, 2]
F = x[:, 3]
IF = x[:, 4]
Time = x[:, 0]/5
# smoothing
F = savgol_filter(F, 5, 2)  
A = savgol_filter(A, 5, 2)
D = savgol_filter(D, 5, 3)

#Intensity-time plot
plt.figure(figsize = (5, 2))
sns.set(style = 'darkgrid', font_scale = 1.5)
plot1 = plt.figure(1)
sns.lineplot(Time, D, color = 'blue')
sns.lineplot(Time, A, color = 'purple')
plt.xlabel("Time (s)")
plt.ylabel("Intensity (a.u.)")
plt.xlim(0, 42, 10)
plt.ylim(-200, 6000, 2000)

#FRET-time plot
plt.figure(figsize = (5, 2))
plot2 = plt.figure(2)
plt.xlim(0, 42, 10)
plt.ylim(0, 1.1, 0.2)
sns.lineplot(Time, F, color = 'black')
sns.lineplot(Time, IF, color = 'red')
plt.xlabel("Time (s)")
plt.ylabel("FRET")
plt.legend()
plt.show()


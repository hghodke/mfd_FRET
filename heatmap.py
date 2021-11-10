# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:50:04 2021
This script creates a TIME-FRET density map (heat map)
@author: bishnu
"""

from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
import numpy as np
from matplotlib import rc

filename = “ ”   # provide path of .csv files for heat map saved from concate scripts above
x = pd.read_csv(filename)
x.columns = ['Time (s)', 'Donor', 'Acceptor', 'FRET', 'Idealized FRET']
x = x.loc[(x['FRET']<=1) & (x['FRET']>0)]
T = x['Time (s)']/5
FRET = x['FRET']
sns.set(style = 'whitegrid', font_scale = 1.5)
sns.jointplot(x = T, y = FRET, data=x, kind="kde", fill=True, gridsize = 100, color = 'skyblue', reverse = False, xlim = (0,160), ylim = (0, 1.1), shade_lowest = False)
plt.show()

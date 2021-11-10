# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:47:53 2021
This script concatenates dat files
@author: bishnu
"""

import os
from natsort import natsorted
import pandas as pd
import seaborn as sns
import matplotlib as plt
import glob
path = ("")  # location of .dat files
all_files = glob.glob(path + "/*.dat")
li = []
for filename in all_files:
    
    df = pd.read_fwf(filename, index_col=None)
    df1 = pd.DataFrame(df)
    df1.columns = ["Time(s)", "Donor", "Acceptor", "FRET", "Idealized-FRET"]
    li.append(df1)

frame = pd.concat(li, axis=0, join = 'outer', ignore_index=False)
frame = pd.DataFrame(frame)
frame.to_csv(" ", index=None) # provide location to save .csv file

 

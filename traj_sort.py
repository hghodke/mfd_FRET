# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:33:15 2021
This is the code used to analyze state-fitted trajectories from vbFRET to classify
into FRET regimes
@author: harshad

"""
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
import numpy as np
from matplotlib import rc
import os
import glob
from scipy.optimize import curve_fit
import sympy as sym
from shutil import copyfile


#Load data using path for the list of files
src_path = r"G:/Results/Merged traces/RNAPEC/Lifetime_analysis_compiled/500nM_NusG_wrong_NTPs/rename"

#Save file path
save_path_static = os.path.join(src_path, 'static')
print(save_path_static)
if not os.path.isdir(save_path_static):
    os.mkdir(save_path_static)

save_path_dynamic = os.path.join(src_path, 'dynamic')
if not os.path.isdir(save_path_dynamic):
    os.mkdir(save_path_dynamic)
    
save_path_dynamic_high = os.path.join(save_path_dynamic, 'dynamic_high')
if not os.path.isdir(save_path_dynamic_high):
    os.mkdir(save_path_dynamic_high)

save_path_dynamic_mid = os.path.join(save_path_dynamic, 'dynamic_mid')
if not os.path.isdir(save_path_dynamic_mid):
    os.mkdir(save_path_dynamic_mid)
    
save_path_dynamic_low = os.path.join(save_path_dynamic, 'dynamic_low')
if not os.path.isdir(save_path_dynamic_low):
    os.mkdir(save_path_dynamic_low)

save_path_dynamic_high_mid = os.path.join(save_path_dynamic, 'dynamic_high_mid')
if not os.path.isdir(save_path_dynamic_high_mid):
    os.mkdir(save_path_dynamic_high_mid)

save_path_dynamic_high_low = os.path.join(save_path_dynamic, 'dynamic_high_low')
if not os.path.isdir(save_path_dynamic_high_low):
    os.mkdir(save_path_dynamic_high_low)

save_path_dynamic_mid_low = os.path.join(save_path_dynamic, 'dynamic_mid_low')
if not os.path.isdir(save_path_dynamic_mid_low):
    os.mkdir(save_path_dynamic_mid_low)


#Open files
all_files = glob.glob(src_path + "/*.dat")

# filtering data using for loop
for filename in all_files:
# for filename in all_files[0:10]:
    with open(filename, 'r') as file:
        data = np.loadtxt(filename)
 
  

    #Sort trajectories
    #does trajectory have photobleaching step included? Classify trajectory as 'static' if only one other state exists, and it survives for less-equal 5 frames
    unique_states, counts = np.unique(data[:,4], return_counts = True)          #this seems to return unique_states in ascending order[!]
    # print(unique_states)
   
    if len(unique_states) == 1:
        print("static")
        np.savetxt(os.path.join(save_path_static,os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
    elif (len(unique_states) == 2) and (counts[0]<5):           
        # print("static_pb")
        np.savetxt(os.path.join(save_path_static,os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
    elif np.all(unique_states<0.3):     #Save as dynamic low
        # print("dynamic low")
        np.savetxt(os.path.join(save_path_dynamic_low, os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
    elif np.all((unique_states>0.4))&(np.all(unique_states<0.7)):
        # print("dynamic mid")
        np.savetxt(os.path.join(save_path_dynamic_mid,os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
    elif np.all(unique_states>0.7):
        # print("dynamic high")
        np.savetxt(os.path.join(save_path_dynamic_high, os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
    elif (np.any(unique_states<0.3))&(np.any(unique_states>0.3))&(np.all(unique_states<0.7)):
        # print("dynamic mid-low")
        np.savetxt(os.path.join(save_path_dynamic_mid_low, os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
    elif (np.all(unique_states>0.4))&(np.any(unique_states>0.7))&((np.any(unique_states<0.7))):
        # print("dynamic high-mid")
        np.savetxt(os.path.join(save_path_dynamic_high_mid,os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
    else:
        print("dynamic high-low")
        np.savetxt(os.path.join(save_path_dynamic_high_low,os.path.basename(filename)), data, fmt = '%15d % 14f %14f %14f %14f')
 
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:14:18 2021

@author: ribis
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

# dataset_name = "500nM_NusG_alone"
# dataset_name = "500nM_NusG_all_correct_NTPs"
dataset_name = "500nM_NusG_wrong_NTPs"

# dataset_name = "RNAP_alone"
# dataset_name = "RNAP_dNTPs"
# dataset_name = "RNAP_wrong_NTPs"
# dataset_name = "RNAP_all_NTPs"

# dataset_name =  "500nM_Mfd"
# dataset_name = "Mfd_ATPgS"
# dataset_name = "Mfd_10uMATP"
# dataset_name = "Mfd_100uMATP"
# dataset_name = "Mfd_1mMATP"
# dataset_name = "Mfd_10mMATP"
# dataset_name = "RNAP_Mfd_ATPgS_rG_rU"

# dataset_name = "MfdR953A_1mMATP"


#define range for FRET values
# a = 0.35
# b = 0.5

a = 0.4
b = 0.7

# spf = 0.2            #seconds per frame
#Load data using path for the list of files
src_path = os.path.join("G:/Results/Merged traces/RNAPEC/Lifetime_analysis_compiled/",dataset_name,"rename")
# src_path = r"G:/Results/Merged traces/RNAPEC/Lifetime_analysis_compiled/RNAP_wrong_NTPs/rename"

#Save file path
save_path_static = os.path.join(src_path, 'static')

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

li = []

# filtering data using for loop
for filename in all_files:
    
    df = pd.read_fwf(filename, index_col=None)
    df1 = pd.DataFrame(df)
    df1.columns = ["Time(s)", "Donor", "Acceptor", "FRET", "Idealized-FRET"]
    df2 = df1[(df1["FRET"]>a) & (df1["FRET"]<b)]
    
    length = len(df2)/5
 
    li.append(length)
# converting list inot dataframe
li1 = pd.DataFrame(li)
li2 = li1[li1[:]>1]
li3 = li2.dropna()

# li3.to_csv(os.path.join(src_path, 'lifetimes_p5_p35.csv'), index=None)
li3.to_csv(os.path.join(src_path, 'lifetimes_p7_p4.csv'), index=None) 
# 

# li3.to_csv("G:/Results/Merged traces/RNAPEC/1 uM MFD(R593A)_1mMATP/rename/R953A_1mMATP_p5_p35.csv", index=None)
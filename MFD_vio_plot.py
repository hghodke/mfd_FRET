# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:19:10 2021

@author: ribis
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/harshad/Dropbox/Mfd project/Mfd FRET paper/Data/Reviewer experiments/lifetimes/20211003_Lifetimes_summary_p35_p5.csv")
# df = pd.read_csv("C:/Users/harshad/Dropbox/Mfd project/Mfd FRET paper/Data/Reviewer experiments/lifetimes/20211003_Lifetimes_summary_p7_p4.csv")
# 
df1 = df.iloc[:,4:7]
# df1 = df.iloc[:,0:4]
# df1 = df.iloc[:,7:16]
print(df1.head)
sns.set_style("whitegrid")
plt.figure(figsize=(5,5))
sns.violinplot(data=df1, cut=0)
# sns.violinplot(data=df1, cut=0)
plt.xticks(rotation=45, ha="right")
plt.ylabel("Time (s)")
plt.ylim(0, 80)

plt.savefig("C:/Users/harshad/Dropbox/Mfd project/Mfd FRET paper/Data/Reviewer experiments/lifetimes/vioplot_p35_p5_NusG.eps", dpi=600)

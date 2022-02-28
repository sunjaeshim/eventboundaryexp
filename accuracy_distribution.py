# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:42:33 2020

@author: shims
"""


import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import numpy as np

df = pd.read_excel("everything_clock.xlsx")
df2 = pd.read_excel("everything_2back (Recovered)(AutoRecovered).xlsx")
clock = df["clock_only_acc"].dropna().to_numpy()
overall = df["clock_acc"].dropna().to_numpy()
back = df["back_only_acc"].dropna().to_numpy()


print(scipy.stats.pearsonr(clock, overall))





plt.hist(clock, bins = 10)
plt.xlabel('Accuracy',fontsize=13)
plt.ylabel('Frequency',fontsize=13)
plt.title("Background only accuracy",fontsize=13)
plt.show()
plt.hist(back, bins = 10)
plt.xlabel('Accuracy',fontsize=13)
plt.ylabel('Frequency',fontsize=13)
plt.title("2back only items accuracy",fontsize=13)
plt.show()
plt.plot(overall, clock, 'o')
#plt.plot(overall, m*overall + b)
plt.xlabel("Overall Accuracy", fontsize=13)
plt.ylabel("Segment Only Accuracy", fontsize=13)
plt.ylim([-0.05,1.05])
plt.title()

plt.show()
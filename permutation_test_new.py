# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:01:37 2020

@author: shims
"""


from statistics import mean
import random
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_excel("clock_perm.xlsx")

cw_list = df["within_avg"].dropna().values.tolist()
cb_list= df["between_avg"].dropna().values.tolist()
#clock_acc = df["clock_acc"].values.tolist()

df2 = pd.read_excel("2back_perm.xlsx")

backw_list = df2["within_avg"].dropna().values.tolist()
backb_list = df2["between_avg"].dropna().values.tolist()
#back_acc = df2["clock_acc"].values.tolist()

print(cw_list)
print(len(cw_list))

print(backw_list)


#clock w vs b

cond_clock = []
cond_back = []

clock_w_min_b= []
noclock_w_min_b = []


for n in range(len(cw_list)):
    clock_w_min_b.append(cw_list[n] - cb_list[n])
    
for n in range(len(backw_list)):
    noclock_w_min_b.append(backw_list[n] - backb_list[n])


x1 = list(clock_w_min_b)
y1 = list(noclock_w_min_b)
    
#cond_diff = (within_clock - between_clock) - (within_noclock - between_noclock) # size=N
#for n in range(len(cw)):
#    cond_c.append(cw[n] - cb[n])
#    cond_nc.append(cnw[n] - cnb[n])
    
#for n in range(len(cw_list_a)):
#    cond_c_a.append(cw_list_a[n] - cb_list_a[n])
#    cond_nc_a.append(cnw_list_a[n] - cnb_list_a[n])
#    cond_c_b.append(cw_list_b[n] - cb_list_b[n])
#    cond_nc_b.append(cnw_list_b[n] - cnb_list_b[n])


def perm_test(list1, list2, trial):
    diff = []
    for n in range(len(list1)):
        diff.append(list1[n] - list2[n])
    diff_arr = np.array(diff)
    real_meandiff = mean(diff)
    
    perm_meandiff = np.zeros(trial)
    for p in range(trial):
        perm_meandiff[p] = ((np.random.randint(2, size = diff_arr.size)*2-1)*diff_arr).mean()
    df = pd.DataFrame(perm_meandiff)
    df.plot.hist(legend=False)
    plt.axvline(real_meandiff, color='red', linewidth=1)
    
    p = (perm_meandiff > real_meandiff).mean()
    #print(real_meandiff)
    #print(p)
    return real_meandiff, p

real_meandiff, p = perm_test(cw_list, cb_list,10000)
print(p)

real_meandiff, p = perm_test(backw_list, backb_list,10000)
print(p)

real, p = perm_test(x1, y1, 10000)
print(p)
#def test_perm_test(list1, list2, trial, real_meandiff):
#    diff = []
#    for n in range(len(list1)):
#        diff.append(list1[n] - list2[n])
#    diff_arr = np.array(diff)
#    real_meandiff = mean(diff)
    
#    perm_meandiff = np.zeros(trial)
#    for p in range(trial):
#        perm_meandiff[p] = ((np.random.randint(2, size = diff_arr.size)*2-1)*diff_arr).mean()
#    df = pd.DataFrame(perm_meandiff)
    #df.plot.hist(legend=False)
    #plt.axvline(real_meandiff, color='red', linewidth=1)
    
#    p = (perm_meandiff > real_meandiff).mean()
    #print(p)
#    return p

allp = []
for n in range(100):
    
    clock_test = []
    noclock_test = []
    for n in range(60):
        clock_test.append(random.choice(cw_list))
        noclock_test.append(random.choice(cb_list))

    a = test_perm_test(clock_test, noclock_test, 10000, real_meandiff)
    allp.append(a)
#plt.hist(allp)
perm = perm_test(cw_list, cb_list, 10000)
print("Clock within vs. between = ", perm)
#perm = perm_test(cnw, cnb, 10000)
#print("Noclock within vs. between = ", perm)

#a = perm_test(cw_list_a, cb_list_a, 10000) 
#print("clock within vs. between version a = ", a)
#anc = perm_test(cnw_list_a, cnb_list_a, 10000)
#print("noclock within vs. between ver a = ", anc)
#bc = perm_test(cw_list_b, cb_list_b, 10000)
#print("clock within vs. between ver b = ", bc)
#b = perm_test(cnw_list_a, cnb_list_a, 10000)
#print("noclock within vs. between version b = ", b)
#ca = perm_test(cond_c_a, cond_nc_a, 10000)
#print("version a clock vs. noclock = ", ca)
#cb = perm_test(cond_c_b, cond_nc_b, 10000)
#print("version b clock vs. noclock = ", cb)

#x = perm_test(clock_w_min_b_a, clock_w_min_b_b, 10000)
#print("w - b diff by version for clock condition = ", x)
#y = perm_test(noclock_w_min_b_a, noclock_w_min_b_b, 10000)
#print("w - b diff by version for noclock condition = ", y)



#z = perm_test(x1,y1,10000)
#print("w - b diff (clock vs. noclock) total = ",z)

def boot(list1, list2, trial):
    
    diff = []
    for n in range(len(list1)):
        diff.append(list1[n] - list2[n])
    diff_arr = np.array(diff)
    sample = np.random.choice(diff_arr, size=diff_arr.size)
    
    sample_props = []
    for n in range(trial):
        sample = np.random.choice(diff_arr, size=diff_arr.size)
        sample_props.append(sample.mean())

    plt.hist(sample_props)
    boot_sort = np.array(sample_props)
    p = np.percentile(boot_sort, 2.5) 
    p2 = np.percentile(boot_sort, 97.5)

    print("0.025 is ", p)
    print("0.975 is ", p2)
    
    
#boot(cw, cb, 10000)    
#boot(cnw, cnb, 10000)

#boot(cond_c, cond_nc, 10000)
#boot(cond_c_a, cond_nc_a, 10000)
#boot(cond_c_b, cond_nc_b, 10000)


#acc_avsb_perm = perm_test(tot_acc_a, tot_acc_b, 10000)
#print("A vs. B accuracy = ", acc_avsb_perm)




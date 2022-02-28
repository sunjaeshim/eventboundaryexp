# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:58:12 2020

@author: shims
"""


import pandas as pd

def rate (info):
    hr = 0
    hr_count = 0
    fa = 0
    fa_count = 0
    #HR = frac of Old items correctly labeled Old
    #FA = frac of New items incorrectly labeled Old

    for i in range(len(info)):
        #if item is old
        if info[i][1] == 1:
            hr_count = hr_count + 1
            #if response is correct
            if info[i][0] == 1:
                hr = hr + 1
        #if item is new
        if info[i][1] == 0:
            fa_count = fa_count + 1
            #if response is incorrect
            if info[i][0] == 0:
                fa = fa + 1

    
    return hr, hr_count, fa, fa_count

def open_file (file_name):

    df = pd.read_csv(file_name, usecols = ["answer", "key_resp.corr"])
    df = df.dropna()
    corr_clock = df["key_resp.corr"].values.tolist()
    total_acc = sum(corr_clock)/324
    repeat_clock = df.values.tolist()
    
    
    clock_hr, clock_hr_count, clock_fa, clock_fa_count = rate(repeat_clock)

    return total_acc, clock_hr, clock_hr_count, clock_fa, clock_fa_count

def by_trial (file_name):
    #n=0 for clock, n=1 for noclock
    df = pd.read_csv(file_name, usecols = ["answer", "key_resp.corr"])

    segment_clock = df.head(386)

    segment_clock = segment_clock.dropna()

    seg_1 = segment_clock.loc[0:35]
    seg_2 = segment_clock.loc[43:78]
    seg_3 = segment_clock.loc[86:121]
    seg_4 = segment_clock.loc[129:164]
    seg_5 = segment_clock.loc[172:207]
    seg_6 = segment_clock.loc[215:250]
    seg_7 = segment_clock.loc[257:292]
    seg_8 = segment_clock.loc[300:335]
    seg_9 = segment_clock.loc[343:378]
    seg_1 = seg_1.values.tolist()
    seg_2 = seg_2.values.tolist()
    seg_3 = seg_3.values.tolist()
    seg_4 = seg_4.values.tolist()
    seg_5 = seg_5.values.tolist()
    seg_6 = seg_6.values.tolist()
    seg_7 = seg_7.values.tolist()
    seg_8 = seg_8.values.tolist()
    seg_9 = seg_9.values.tolist()
    
    trials = [seg_1, seg_2, seg_3, seg_4, seg_5, seg_6, seg_7, seg_8, seg_9]
    results = []
    for items in trials:
        a, b, c, d = rate(items)
        if b == 0:
            hr = "none"
        else:
            hr = a / b
        if d == 0:
            fa = "none"
        else:
            fa = c / d
        results.append([hr, fa])
    return results



def main(file_input, output):
    df = pd.read_excel(file_input)
    files = df.values.tolist()
    data = []
    for item in files:
        csv_file = item[0]
        total_acc, clock_hr, clock_hr_count, clock_fa, clock_fa_count = open_file(csv_file)
        clock_hitrate = clock_hr / clock_hr_count
        clock_falsealarm = clock_fa / clock_fa_count
        tmp = [total_acc, clock_hitrate, clock_falsealarm]
        result_clock = by_trial(csv_file)
        for i in range(len(result_clock)):
            tmp.append(result_clock[i][0])
            tmp.append(result_clock[i][1])
        data.append(tmp)
    table = pd.DataFrame(data, columns = ["clock_acc", "clock_hitrate", "clock_falsealarm", "seg_1_hr", "seg_1_fa", "seg_2_hr", "seg_2_fa","seg_3_hr", "seg_3_fa","seg_4_hr", "seg_4_fa", "seg_5_hr", "seg_5_fa", "seg_6_hr", "seg_6_fa", "seg_7_hr", "seg_7_fa", "seg_8_hr", "seg_8_fa", "seg_9_hr", "seg_9_fa"])
    table.to_excel(output)
    
main ("all_files_2back.xlsx", "2back_hr_fa.xlsx")
#main ("all_files_clock.xlsx", "clock_hr_fa.xlsx")
#open_file("PARTICIPANT_2back_pavlovia_VerB_2nd_2021-01-17_16h59.40.015.csv")
#by_trial("PARTICIPANT_2back_pavlovia_VerB_2nd_2021-01-17_16h59.40.015.csv")
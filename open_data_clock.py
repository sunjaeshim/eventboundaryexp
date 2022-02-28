# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:16:42 2020

@author: shims
"""
import pandas as pd

def get_file(file_name):
    df = pd.read_csv(file_name, usecols = ["pictures", "segment"])
    df = df.dropna()
    df2 = pd.read_csv(file_name, usecols = ["key_resp_2.corr", "item_a", "item_b", "key_resp_2.rt"])
    df2 = df2.dropna()
    
    segment_list = df.values.tolist()
    item_a_tot = []
    item_b_tot = []
    corr_tot = []
    rt_tot = []
    n = 36
    while n < 381:
        item_a_clock = []
        item_b_clock = []
        corr_clock = []
        rt_total = []
        tmp = df2["item_a"].loc[n:n+7].values.tolist()
        for item in tmp:
            item_a_clock.append(item)
        tmp = df2["item_b"].loc[n:n+7].values.tolist()
        for item in tmp:
            item_b_clock.append(item)
        tmp = df2["key_resp_2.corr"].loc[n:n+7].values.tolist()
        for item in tmp:
            corr_clock.append(item)
        tmp = df2["key_resp_2.rt"].loc[n:n+7].values.tolist()
        for item in tmp:
            rt_total.append(item)
        item_a_tot.append(item_a_clock)
        item_b_tot.append(item_b_clock)
        corr_tot.append(corr_clock)
        rt_tot.append(rt_total)
        n = n + 43

        

    
    def segment_check (item_a, item_b, corr, rt_tot, segment_list):
           seg_1 = []
           seg_2 = []
           rt_w = []
           rt_b = []
           trial_tot = []
           
           for i in range(len(item_a)):
               within = 0
               within_count = 0
               between = 0
               between_count = 0
               seg_1 = []
               seg_2 = []
               rt_within = []
               rt_between = []
               for k in range(6):
                   first = item_a[i][k]
                   second = item_b[i][k]
                   trial = []
                   for n in range(len(segment_list)):
                       if segment_list[n][0] == first:
                           seg_1 = segment_list[n][1]
                       if segment_list[n][0] == second:
                           seg_2 = segment_list[n][1]
                   #within segment condition
                   if seg_1 == seg_2:
                       within_count = within_count + 1
                       #rt_within.append(rt_tot[i][k])
                       #print(rt_tot[k])
                       if corr[i][k] == 1:
                           within = within + 1
                           rt_within.append(rt_tot[i][k])
                   if seg_1 != seg_2:
                       between_count = between_count + 1
                       if corr[i][k] == 1:
                           between = between + 1
                           rt_between.append(rt_tot[i][k])
               trial.append(within)
               trial.append(within_count)
               trial.append(between)
               trial.append(between_count)
               rt_w.append(rt_within)
               rt_b.append(rt_between)
               trial_tot.append(trial)
        
           return trial_tot, rt_w, rt_b
       
    trial_clock, rt_within, rt_between= segment_check(item_a_tot, item_b_tot, corr_tot, rt_tot, segment_list)

    def get_avg_within (rt_list, trial_list):
        avg_list = []
        for item in rt_list:
            if trial_list[rt_list.index(item)][0] == 0:
                avg_list.append(0)
            else:
                avg = sum(item)/trial_list[rt_list.index(item)][0]
                avg_list.append(avg)
        return avg_list
    def get_avg_between (rt_list, trial_list):
        avg_list = []
        for item in rt_list:
            if trial_list[rt_list.index(item)][2] == 0:
                avg_list.append(0)
            else:
                avg = sum(item)/trial_list[rt_list.index(item)][2]
                avg_list.append(avg)
        return avg_list
    rt_w_avg = get_avg_within(rt_within,trial_clock)
    print(rt_w_avg, "avg")
    rt_b_avg = get_avg_between(rt_between,trial_clock)
    rt_w = sum(rt_w_avg) / 9
    rt_b = sum(rt_b_avg) / 9

    def get_sum (trial_clock):
        within_corr = 0
        between_corr = 0
        for item in trial_clock:
            within_corr = within_corr + item[0]
            between_corr = between_corr + item[2]
        return within_corr, between_corr
    
    within_corr, between_corr = get_sum(trial_clock)
    #print(within_corr, between_corr)
    return within_corr, between_corr, rt_w, rt_b

def main(complete_file, output):
    within = []
    between = []
    within_tot = []
    between_tot = []
    w_avg = []
    b_avg = []
    rt_w = []
    rt_b = []
    df = pd.read_excel(complete_file).values.tolist()
    for item in df:
        within_corr, between_corr, rt_within, rt_between = get_file(item[0])
        within.append(within_corr)
        between.append(between_corr)
        w_avg.append(within_corr / 27)
        b_avg.append(between_corr / 27)
        rt_w.append(rt_within)
        rt_b.append(rt_between)
    count = 0
    while count < len(df):
        within_tot.append(27)
        between_tot.append(27)
        count = count + 1
    #print(within_tot)
    data = []
    table = pd.DataFrame(data)
    table["within_corr"] = within
    table["within_tot"] = within_tot
    table["between_corr"] = between
    table["between_tot"] = between_tot
    table["within_avg"] = w_avg
    table["between_avg"] = b_avg
    table["within_rt"] = rt_w
    table["between_rt"] = rt_b
    table.to_excel(output)


#get_file('5c49e951bd42830001dbae9d_2back_pavlovia_VerA_2nd_2021-01-20_12h15.37.207.csv')    
main("all_files_clock.xlsx","clock_acc.xlsx")
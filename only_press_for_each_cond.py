# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 11:13:31 2021

@author: shims
"""


import pandas as pd

def data_open(open_file):
    df = pd.read_csv(open_file)
    df1 = df[0:36]
    df2 = df[43:79]
    df3 = df[86:122]
    df4 = df[129:165]
    df5 = df[172:208]
    df6 = df[215:251]
    df7 = df[258:293]
    df8 = df[300:336]
    df9 = df[343:380]
    frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9]
    df = pd.concat(frames)
    
    pic = df["pictures"].values.tolist()
    resp = df["key_resp.keys"].values.tolist()
    corr = df["key_resp.corr"].values.tolist()
    ans = df["answer"]
    back_only = []
    clock_only = []
    both = []
    i = 0
    for tmp in range(54):
        pool = []
        for n in range(6):
            if pic[n+i] in pool:
                if n+i > 1:
                    if pic[n+i] == pic[n+i-2]:
                        both.append(corr[n+i])
                    else:
                        clock_only.append(corr[n+i])
            if pic[n+i] not in pool:
                if n+i > 1:
                    if pic[n+i] == pic[n+i-2]:
                        back_only.append(corr[n+i])
                    
            pool.append(pic[n+i])
        i = i + 6
        
    
    
    #k = 2
    #while k < 324:
    #    if pic[k-2] == pic[k]:
    #        back_only.append(corr[k])
    #    
    #    k = k + 1
        
    print(back_only)        
    back_acc = sum(back_only) / len(back_only)
    print(back_acc)
    
    print(clock_only)
    clock_acc = sum(clock_only) / len(clock_only)
    print(clock_acc)
    
    print(both)
    both_acc = sum(both) / len(both)
    print(both_acc)
    
    return back_acc, clock_acc, both_acc

def main(file_input, file_output):
    df = pd.read_excel(file_input)
    files = df.values.tolist()
    data = []
    for item in files:
        csv_file = item[0]
        back, clock, both = data_open(csv_file)
        tmp = [back, clock, both]
        data.append(tmp)
    table = pd.DataFrame(data, columns = ["back_only_acc", "clock_only_acc", "both_acc"])
    table.to_excel(file_output)

main("all_files_2back.xlsx", "separate_acc.xlsx")
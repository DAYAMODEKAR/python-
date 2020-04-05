# -*- coding: utf-8 -*-
"""
PYTHON CASE STUDY
NAME:DAYA MODEKAR
EMP ID:142900
DATASET:AIRLINE DATA

"""
import pandas as pd
import matplotlib.pyplot as plt

def read_input_datafile():
    '''Read Excel File'''
    air_data = pd.read_excel("flightdata.xlsx")
    fra_me = pd.DataFrame(air_data)
    return fra_me
#
def sort_by_attribute(dd_f):
    '''Sorting of a particular attribute as mentioned by user'''
    att = input("Enter the attribute to be sorted:")
    dd_f = dd_f.sort_values(by=att)
    print(dd_f)
#
def avg_taxout_value(dd_f):
    '''Average Tax Out value'''
    avg_1 = dd_f['TaxiOut'].mean()
    print("Average taxout value of the total data:", avg_1)
#
def flight_with_mindist(dd_f):
    '''Minimum distance Journey'''
    mind = dd_f['Distance'].min()
    print("Shortest distance flight:", mind)
#
def insert_avg_elapsed_time(dd_f):
    new_avg = dd_f.loc[:, ['ActualElapsedTime', 'CRSElapsedTime']]
    df2 = {'TimeAvg':new_avg.mean(1)}
    dd_f['TimeAvg'] = df2['TimeAvg']
    print(dd_f)
#
def display_by_src_dest(dd_f, keys, keyd):
    '''Business Inference:Find flight details for particular origin and destination'''
    x_a = dd_f[(dd_f['Origin'] == keys) & (dd_f['Dest'] == keyd)]
    print(x_a)
#
def plot_elapsedtime_avg(dd_f):
    '''Business Inference:Analysis of elapsed time to improve and take measure by plot'''
    plt.plot(dd_f['TimeAvg'])
    plt.xlabel('Entries')
    plt.ylabel('TimeAvg')
#    
def update_taxin_writeto_excel(dd_f):
    '''Business Inference:Update tax in by 10%'''
    for i in range(len(dd_f)):
        dd_f.loc[i, "TaxiIn"] = (dd_f.loc[i, 'TaxiIn'] + (dd_f.loc[i, 'TaxiIn']/10))
    print("\nData with Updated TaxiIn:\n")
    print(dd_f)
    return dd_f
#
def write_to_excel(dd_f):
    '''excel update and generation'''
    dd_f.to_excel('output.xlsx')
    
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:58:33 2019

@author: DELL
"""
import collections
def readfile(file_name):
    with open(file_name) as f:
        #fo=f.read(fie_name) converts to raw string , dificut to processs
       fo= f.readlines()
       return fo
   
def getfield(data,line,position):
    return data[line].split(':')[position].strip()


#def processtransaction(data,line,position):
def text_to_num(str):
    return float(str)
    
def calc_mean(list1):
    return sum(list1)/len(list1)
'''
def calc_count(list):
    count=0
    for i in list:
        for j in list:
            if (i == j):
                count+=1
    return count
            '''
def calc_median(list1):
    s= sorted(list1)
    n=len(list1)
    if (n/2==0):
        n1=s[n//2-1]
        n2=s[n//2+1]
        return sum(n1,n2)/2
    else:
        return s[n//2]

def calc_mode(list1):
       # max(set(list)),key=list.count()
       data=collections.counter(list1)
       datadic=dict(data)
       max_value=max(datadic.values())
       mode=[num for num,freq in datadic if freq==max_value]
       return mode
       
   
#def calc_ess(list1):
    
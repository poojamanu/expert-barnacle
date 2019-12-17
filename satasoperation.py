# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:52:51 2019

@author: DELL
"""

from BasicStats import BasicStats
#dataset=dataset.txt

data1=BasicStats('dataset.txt')
data1.load_data()
print(data1.raw_data)
#print(dir(data1))
data1.create_list()
#print(data_list)
data1.get_numbers()
mean=data1.find_mean()
print(mean)
#print(mean)
#count=data1.count(numbers)
#print(count)


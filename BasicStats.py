# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:16:18 2019

@author: DELL
"""

#read dataset file
#make two ists good dta and bad data
#mean median,mode,size,count of each number
#distribution,standard error,deviation
#percentile of given number
from utils import text_to_num,calc_mean,calc_mode
class BasicStats:
    def __init__(self,dataset):
        self.dataset=dataset
        
    def load_data(self):
        with open(self.dataset) as ds:
            raw_data=ds.read()
            self.raw_data=raw_data
            
   # def clean_cases(self):
    def create_list(self):
       # self._data_list=self.raw_data.split()
        self.data_list=self.raw_data.split()
        
    def get_numbers(self):
        #self._numbers=[text_to_num(i) for i in self._data_list]
        self.numbers=[text_to_num(i) for i in self.data_list]
        
    
    def find_mean(self):
       # self._mean=calc_mean(self._numbers)
         self.mean=calc_mean(self.numbers)
         
    #def count(self,numbers):
    #    self.count=calc_count(self.numbers)
        
    def find_mode(self,numbers)  :
         self.mode=calc_mode(self.numbers)
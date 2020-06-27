# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:54:28 2020

@author: dhaar01
"""

for i in range(1,int(input())): 
    #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(round(i * (10**i -1)/9))
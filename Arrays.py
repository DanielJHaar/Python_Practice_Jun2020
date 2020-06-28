# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:43:04 2020

@author: danie
"""


import numpy

def arrays(arr):
    return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
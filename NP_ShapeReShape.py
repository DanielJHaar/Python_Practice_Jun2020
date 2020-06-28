# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:45:40 2020

@author: danie
"""


import numpy as np
arr = list(map(int, input().split()))
change_arr = np.array(arr)
change_arr.shape = (3,3)
print(change_arr)
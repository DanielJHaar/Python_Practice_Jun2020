# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:36:00 2020

@author: danie
"""


import numpy as np
arr = list(map(float, input().split()))

np.set_printoptions(legacy='1.13')
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
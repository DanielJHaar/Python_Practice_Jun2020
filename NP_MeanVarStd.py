# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:12:44 2020

@author: danie
"""


import numpy as np
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]

np.set_printoptions(legacy='1.13')
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.std(arr))
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:09:10 2020

@author: danie
"""


import numpy as np
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]
print(max(np.min(arr, axis = 1)))

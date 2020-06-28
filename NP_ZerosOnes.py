# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:09:18 2020

@author: danie
"""


import numpy as np
dim = tuple(map(int,input().split()))

print(np.zeros(dim, dtype = np.int))
print(np.ones(dim, dtype = np.int))
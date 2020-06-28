# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:16:33 2020

@author: danie
"""


import numpy as np

np.set_printoptions(legacy='1.13')
n, m = map(int,input().split())
print(np.eye(n, m))
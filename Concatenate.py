# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:55:17 2020

@author: danie
"""


import numpy as np
n, m, p = map(int, input().split())

N = np.array([list(map(int, input().split())) for _ in range(n)])
M = np.array([list(map(int, input().split())) for _ in range(m)])

print(np.concatenate((N, M)))
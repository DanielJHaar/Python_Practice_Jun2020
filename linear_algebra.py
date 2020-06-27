# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:53:50 2020

@author: danie
"""

import numpy as np

rows = int(input())
arr = np.array([[float(x) for x in input().split()] for i in range(rows)])
print(round(np.linalg.det(arr),2))
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:17:50 2020

@author: danie
"""


import numpy as np
n = int(input())

arr_A = [list(map(int, input().split())) for _ in range (n)]
arr_B = [list(map(int, input().split())) for _ in range (n)]

print(np.dot(arr_A, arr_B))
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:48:35 2020

@author: danie
"""


import numpy as np
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

print(np.transpose(arr))
my_array = np.array(arr)
print(my_array.flatten())
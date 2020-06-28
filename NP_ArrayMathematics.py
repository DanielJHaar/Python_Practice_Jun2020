# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:20:25 2020

@author: danie
"""


import numpy as np

n, m = map(int, input().split())

A = np.array([list(map(int,input().split())) for _ in range (n)])
B = np.array([list(map(int,input().split())) for _ in range (n)])

print(A + B)                   
print(A - B)                     
print(A * B)                    
print(A // B)                   
print(A % B)                   
print(A**B)      
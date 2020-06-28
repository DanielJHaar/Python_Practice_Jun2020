# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:33:11 2020

@author: danie
"""


import numpy
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(numpy.prod(numpy.sum(arr,axis=0)))

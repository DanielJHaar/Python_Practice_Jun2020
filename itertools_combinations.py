# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 07:39:20 2020

@author: danie
"""

from itertools import combinations

x = input().split()

string = sorted(x[0])
size = int(x[1])

for i in range(1, size + 1):
    items = list(combinations(string,i))
    for item in items:
        print(''.join(item))
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:50:50 2020

@author: dhaar01
"""

from itertools import permutations

x = input().split()
y = list(permutations(sorted(x[0]), int(x[1])))

for item in y:
    print(''.join(item))
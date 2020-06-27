# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 07:44:34 2020

@author: danie
"""

from itertools import combinations_with_replacement

x = input().split()

string = sorted(x[0])
size = int(x[1])

items = list(combinations_with_replacement(string,size))

for item in items:
    print(''.join(item))
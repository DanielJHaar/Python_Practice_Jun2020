# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:42:57 2020

@author: dhaar01
"""

A = set(map(int, input().split()))
Other_Sets = int(input())
false_count = 0 

for i in range(Other_Sets):
    X = set(map(int, input().split()))
    if A.intersection(X) == X:
        false_count += 0
    else:
        false_count += 1

if false_count == 0:
    print('True')
else:
    print('False')
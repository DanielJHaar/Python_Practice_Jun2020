# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:43:09 2020

@author: dhaar01
"""

n = int(input())
s = set(map(int, input().split()))

commands = int(input())

for x in range(commands):
    x = input().split()
    y = set(map(int, input().split()))
    if x[0] == 'intersection_update':
        s.intersection_update(y)
    elif x[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(y)
    elif x[0] == 'difference_update':
        s.difference_update(y)
    elif x[0] == 'update':
        s.update(y)
        
print(sum(s))
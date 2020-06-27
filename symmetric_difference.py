# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:27:32 2020

@author: dhaar01
"""

M = int(input())
Alpha = set(map(int, input().split()))
N = int(input())
Bravo = set(map(int, input().split()))

SymDif = Alpha.union(Bravo) - Alpha.intersection(Bravo)

Sorted = sorted(list(SymDif))

for i in Sorted:
    print(i)
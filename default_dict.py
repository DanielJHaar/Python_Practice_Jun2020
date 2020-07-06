# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:05:50 2020

@author: danie
"""


from collections import defaultdict

n, m = map(int,input().split())
A = [input() for i in range(n)]
B = [input() for i in range(m)]
d = defaultdict(list)
index = 0

for i in A:
    d[i].append(A.index(i, index) + 1)
    index +=1

for i in B:
    if i not in A:
        print(-1)
    else:
        print(" ".join(map(str,d[i])))
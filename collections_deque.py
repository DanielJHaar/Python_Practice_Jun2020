# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:36:31 2020

@author: dhaar01
"""

from collections import deque
d = deque()

n = int(input())

for i in range(n):
    operation = input().split()
    getattr(d,operation[0])(*operation[1] if len(operation) > 1 else [])

print(*[item for item in d])
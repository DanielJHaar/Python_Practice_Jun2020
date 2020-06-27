# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:49:38 2020

@author: dhaar01
"""

from itertools import product

A = map(int, input().split())
B = map(int, input().split())

print(*product(A,B))
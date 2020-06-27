# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:43:02 2020

@author: dhaar01
"""

n = int(input())
english =set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

combined = english.union(french)
print(len(combined))
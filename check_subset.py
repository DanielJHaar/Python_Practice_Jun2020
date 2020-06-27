# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:11:12 2020

@author: dhaar01
"""

tests = int(input())
for i in range(tests):
    x = int(input())
    A = set(map(int,input().split()))
    y = int(input())
    B = set(map(int,input().split()))   
    print(A.intersection(B) == A)
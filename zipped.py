# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:02:51 2020

@author: danie
"""

students, subjects = map(int, input().split())

subject = []
for _ in range (subjects):
    subject.append(map(float, input().split()))

for score in zip(*subject): 
    print(sum(score)/len(score))
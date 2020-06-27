# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:19:10 2020

@author: dhaar01
"""

n = int(input())
s = set(map(int, input().split()))

commands = int(input())

for i in range(commands):
    x = input().split()
    if x[0] == 'pop':
        s.pop()
    elif x[0] == 'remove':
        s.remove(int(x[1]))
    elif x[0] == 'discard':
        s.discard(int(x[1]))
print(sum(s))


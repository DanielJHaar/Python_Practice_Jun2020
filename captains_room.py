# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:56:01 2020

@author: dhaar01
"""

groups = int(input())
roomlist = list(map(int,input().split()))
roomset = set(roomlist)

Remainder = groups*sum(roomset) - sum(roomlist)
Captains_Room = int((Remainder)/(groups - 1))

print(Captains_Room)
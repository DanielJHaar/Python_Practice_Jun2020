# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 06:44:18 2020

@author: danie
"""

tests = int(input())
for i in range(tests):
    try:
        (a, b) = map(int, input().split())
        if b == 0:
            print("Error Code: integer division or modulo by zero")
        else:
            print (int(a/b))
    except ValueError as e:
        print("Error Code:",e)
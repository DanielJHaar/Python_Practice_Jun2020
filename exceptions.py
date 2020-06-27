# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:32:45 2020

@author: dhaar01
"""

tests = int(input())

for i in range(tests):
    (a, b) = map(str,(input().split()))
    try:
        print(int(int(a)/int(b)))
    except:
        try:
            if int(b) == 0:
                print('Error Code: integer division or modulo by zero')
        except ValueError as e:
            print("Error Code: invalid literal for int() with base 10:", e)

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:52:50 2020

@author: danie
"""


n = int(input())
numbers = list(map(int,input().split()))
numbers = sorted(numbers)
if(numbers[0]<=0):
    print(False)
else:
    check = False
    for i in numbers:
        s = str(i)
        if (s==s[::-1]):
            check = True
            break
    print(check)
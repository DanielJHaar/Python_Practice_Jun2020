# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:17:06 2020

@author: danie
"""


from collections import OrderedDict

items = int(input())
sales = OrderedDict()

for sale in range(items):
    item = input().split()
    price = int(item[-1])
    name = ' '.join(item[:-1])
    
    if sales.get(name):
        sales[name] += price
    else:
        sales[name] = price

for i in sales.keys():
    print(i, sales[i]) 
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:13:28 2020

@author: dhaar01
"""

from collections import Counter

n = int(input())

sizes = map(int, input().split())
inventory = Counter(sizes)

customers = int(input())

money = 0

for i in range(customers):
    (sizes, price) = map(int, input().split())
    if inventory[sizes] > 0:
        inventory[sizes] -= 1
        money += price

print(money)

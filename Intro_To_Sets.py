# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:17:10 2020

@author: dhaar01
"""

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
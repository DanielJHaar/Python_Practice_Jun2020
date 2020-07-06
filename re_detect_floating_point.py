# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:17:35 2020

@author: danie
"""


from re import match, compile

pattern = compile('^[+-]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(pattern.match(input())))
 
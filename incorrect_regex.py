# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 06:55:22 2020

@author: danie
"""

import re

tests = int(input())
for i in range(tests):
    try:
        re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:38:17 2020

@author: danie
"""

import numpy as np
 
poly = [float(x) for x in input().split()]
value = int(input())

print(np.polyval(poly, value))
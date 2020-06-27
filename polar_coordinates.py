# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:13:54 2020

@author: dhaar01
"""

from cmath import phase
#complex() function can be used in python to convert the input as a complex number.
z = input()
print(abs(complex(z)))
print(phase(complex(z)))
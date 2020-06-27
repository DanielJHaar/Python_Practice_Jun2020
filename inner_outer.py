# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:10:27 2020

@author: danie
"""

import numpy

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(numpy.inner(A,B))
print(numpy.outer(A,B))
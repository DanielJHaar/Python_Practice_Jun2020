# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:02:25 2020

@author: dhaar01
"""

def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

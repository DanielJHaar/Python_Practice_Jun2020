# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:56:04 2020

@author: dhaar01
"""

import calendar
date = list(map(int, input().split()))
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(days[calendar.weekday(date[2],date[0],date[1])].upper())
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:06:56 2023

@author: yash
"""
import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
b=a>4
print (b)
print (a[b])
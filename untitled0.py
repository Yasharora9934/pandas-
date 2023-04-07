# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:15:20 2023

@author: yash
"""
import numpy as np
a=np.array([[1,2],[3,4],[5,6]
           ])
b=np.array([[1,2],[3,4],[5,6]
           ])
b=b>4
print(b)
a[b]=-1
print (a)


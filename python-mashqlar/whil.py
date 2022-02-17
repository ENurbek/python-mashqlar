# -*- coding: utf-8 -*-
"""
Created on Fri May 28 23:49:31 2021

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
def f(x,a,b,c):
    return a*x**2+b*x*c
xlist=np.linspace(-10,10,num=1000)
xlist=np.arange(-10,10,.1)
ylist=f(xlist,3,1,4)
plt.figure(num=0,dpi=130)
plt.plot(xlist,ylist)
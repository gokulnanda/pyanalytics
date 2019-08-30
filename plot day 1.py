# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:31:25 2019

@author: Gokul Nanda
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100) #0 to 10 in 100 parts
x
np.sin(x)

plt.plot(x,np.sin(x)).savefig('plot2.jpg') #save should be before show
plt.savefig('C:/pyWork/pyProjects/pyanalytics')
plt.show(); #mean completed plot, can plot next one

import matplotlib.image as mpimg
img = mpimg.imread('plot1.jpg')
print(img)
imgplot = plt.imshow(img)

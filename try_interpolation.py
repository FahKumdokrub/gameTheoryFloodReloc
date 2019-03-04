#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:14:41 2019

@author: tikumporn
"""

import numpy as np
from scipy import interpolate

def getInter(x):
    years = np.array([0,10,20,30,40,50,60,70,80,90,100])
    flood_prob = np.array([0,0.1,0.2,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1])
    f = interpolate.interp1d(years,flood_prob)
    flood_prob_inter = f(x)
    print flood_prob_inter
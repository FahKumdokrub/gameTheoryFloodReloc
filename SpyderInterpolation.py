#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:48:53 2019

@author: tikumporn
"""
import numpy as np
from scipy import interpolate

def getInter(x):
    years = np.array([0,10,20,30,40,50,60,70,80,90,100])
    flood_prob = np.genfromtxt('file_name', delimeter=',')
    f = interpolate.interp1d(years,flood_prob)
    flood_prob_inter = f(x)
    print flood_prob_inter


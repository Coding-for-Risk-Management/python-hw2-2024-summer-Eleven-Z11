#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:10:26 2024

@author: didi
"""
import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t=np.arange(0,ppy*m+1)
    cpn=couponRate*face
    df=(1/(1+y/ppy))
    dft=[df**i for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    return(bondPrice)
    

# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy=1

price = getBondPrice(y, face, couponRate, m, ppy=1)

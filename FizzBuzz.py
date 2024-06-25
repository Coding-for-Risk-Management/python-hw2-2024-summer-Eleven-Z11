#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:07:24 2024

@author: didi
"""
import numpy as np

def FizzBuzz(start, finish):
    
    numvec=np.arange(start,finish+1)
    objvec=np.array(numvec,dtype = object)
    
    fizz_mask=(numvec % 3 == 0)&(numvec % 5 != 0)
    buzz_mask=(numvec % 5 == 0)&(numvec % 3 != 0)
    fizzbuzz_mask=(numvec % 3 == 0)&(numvec % 5 == 0)
    
    objvec[fizzbuzz_mask]="fizzbuzz"
    objvec[buzz_mask]="buzz"
    objvec[fizz_mask]="fizz"
                  
    return(objvec)



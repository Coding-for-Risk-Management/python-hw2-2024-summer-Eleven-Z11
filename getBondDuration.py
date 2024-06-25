#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:37:13 2024

@author: didi
"""

import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    # Number of periods
    periods = m * ppy
    # Time periods array
    t = np.arange(1, periods + 1)
    # Coupon payment per period
    coupon = face * couponRate / ppy
    # Discount factors for each period
    discount_factors = 1 / (1 + y / ppy) ** t
    # Present value of each cash flow
    pv_cf = coupon * discount_factors
    pv_cf[-1] += face * discount_factors[-1]  # Add face value to the last cash flow
    # Weight (w) for each period
    w = pv_cf / np.sum(pv_cf)
    # Duration calculation
    duration = np.sum(w * t)
    return duration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10

# Call the function
duration = getBondDuration(y, face, couponRate, m, ppy=2)
print(f"Bond Duration with ppy=2: {duration:.2f}")

# Call the function with ppy = 1
duration = getBondDuration(y, face, couponRate, m, ppy=1)
print(f"Bond Duration with ppy=1: {duration:.2f}")

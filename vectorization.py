#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:37:12 2020

@author: raghav
"""

import time
import numpy as np

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print(c)
print("Vectorized version : " + str(1000 * (tic-toc)) + "ms")

c = 0
tic = time.time()
for i in range(1000000):
	c += a[i] * b[i]
toc = time.time()

print(c)
print("Non Vectorized version : " + str(1000 * (tic - toc)) + "ms")
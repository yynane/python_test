#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 
@author: yuying
@file: test_pyplot.py
@time: 2016/10/16 13:52
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y, 'r--')
plt.show()

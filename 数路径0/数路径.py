# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:39:19 2019

@author: yumi
动态规划
"""
def uniquePath(m, n):
    if m==1 or n==1:
        return 1
    else:
        return uniquePath(m-1, n)+uniquePath(m, n-1)

assert uniquePath(1, 2) == 1
assert uniquePath(3, 3) == 6
assert uniquePath(10, 20) == 6906900

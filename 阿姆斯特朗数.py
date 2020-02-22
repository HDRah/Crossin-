# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:39:19 2019

@author: yumi
阿姆斯特朗数是指一个等于其各个位n次方和的数，其中n为该数的位数
本程序中第一个函数用于求解阿姆斯特朗数，第二个用于求解输入一个正整数后
距离最近的阿姆斯特朗数
"""
def judge_Amu(n):
    if sum([int(k)**len(str(n)) for k in str(n)])==n:
        return True

    
def Amu(n=1000):
    result = []
    for i in range(n):
        if judge_Amu(i):
            result.append(i)
    return result

def near_Amu(n):
    down, up=n, n
    while True:
        if judge_Amu(down):
            return down
        elif judge_Amu(up):
            return up
        down-=1
        up+=1
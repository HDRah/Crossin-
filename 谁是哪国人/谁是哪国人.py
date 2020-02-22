# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:39:19 2019

@author: yumi

"""
import itertools

countries = ['Ameria', 'Germany', 'England', 'France', 'Russia', 'Italy']
persons = ['A', 'B', 'C', 'D', 'E', 'F']

for res in itertools.permutations(persons, 6):
    # A,E,C不是美国人，俄国人，德国人
    if res[0] in 'AEC' or res[4] in 'AEC' or res[1] in 'AEC':
        continue
    # B,F不是德国人
    if res[1] == 'B' or res[1] == 'F':
        continue
    # A不是法国人，C不是意大利人
    if res[3] == 'A' or res[5] == 'C':
        continue
    # B不是美国人，C不是法国人
    if res[0] == 'B'or res[3] == 'C':
        continue

    print(sorted(zip(res, countries), key=lambda t: t[0]))
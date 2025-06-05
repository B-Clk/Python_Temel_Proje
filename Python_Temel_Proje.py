# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 21:24:55 2025

@author: asus
"""


liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(m):
    flatten_m=[]
    for i in m:
        if isinstance(i, list):
            flatten_m.extend(flatten(i))
        else:
            flatten_m.append(i)
    return flatten_m

a= flatten(liste)
print(a)

def reverseList(m):
    reverse_m =[]
    for i in range(len(m)):
        if isinstance(m[-1-i], list):
            reverseList(m[-1-i])
            reverse_m.append(m[-1-i])
            
        else:
            if i<len(m)//2:
                temp= m[i]
                m[i]=m[-1-i]
                m[-1-i]=temp
                reverse_m.append(m[i])
    return reverse_m

m=[[1, 2], [3, 4], [5, 6, 7]]
a= reverseList(m)
print(a)
        
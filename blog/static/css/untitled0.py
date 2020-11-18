# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:50:17 2019

@author: Mohit bhardwaj
"""

N=int(input())
s=input()
p=s.split('')

total=0
for i in p:
    total=total+int(i)
mean=total/N
print(mean)    


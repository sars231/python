#!/usr/bin/python
#coding:utf-8

"""
冒泡法排序
"""

def maopao(l):
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    print l

l=[4,5,2,3,7,1,9,6]

maopao(l)

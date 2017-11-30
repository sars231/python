#!/usr/bin/python
#coding:utf-8
"""
插入排序
"""

def inst(l):
    key=0
    for i in range(1,len(l)):
        j=i-1
        key=l[i]
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    print l

l=[10,5,19,8,7,3,12,0]

inst(l)

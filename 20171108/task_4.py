#!/usr/bin/python
#coding:utf-8
"""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""

a=raw_input("请输入整数a：")
b=raw_input("请输入整数b：")
c=raw_input("请输入整数c：")

def comp(i,j,k):
    l=sorted([i,j,k])
    for n in l:
        print n,

i=int(a)
j=int(b)
k=int(c)

comp(i,j,k)
print
def cmp(i,j,k):
    if i>j:
        if k>i:
            print j,i,k
        elif k<j:
            print k,j,i
        else:
            print j,k,i
    else:
        if k>j:
            print i,j,k
        elif k<i:
            print k,i,j
        else:
            print i,k,j

cmp(i,j,k)


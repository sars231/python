#!/usr/bin/python
#coding:utf-8
"""
一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程 　　　找出1000以内的所有完数。
"""

def wanshu(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return True

for n in range(1,1001):
    if wanshu(n)==True:
        print n,

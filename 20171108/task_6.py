#!/usr/bin/python
#coding:utf-8
"""
判断101-200之间有多少个素数，并输出所有素数。
"""
def zhishu(j):
    for n in range(2,j):
        if j%n==0:
            return False
    return True


m=0
for i in range(101,201):
    if zhishu(i)==True:
        m=m+1
        print i,
print
print m

